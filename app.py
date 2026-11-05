import streamlit as st
import tempfile
import os

from pathlib import Path

from modules.fits_loader import load_fits
from modules.data_analysis import analyze_image
from modules.visualization import plot_radio_image
from modules.quality_checks import check_image_quality
from services.first_survey import download_first_image

st.set_page_config(
    page_title="RadioSkyLab",
    page_icon="🔭",
    layout="wide"
)

st.title("RadioSkyLab")
st.caption("Radio Astronomy Data Analysis and Visualisation Platform")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select module",
    [
        "Dashboard",
        "FIRST Survey Explorer",
        "FITS Explorer",
        "Image Analysis",
        "About"
    ]
)

if page == "Dashboard":
    st.header("Radio Astronomy Research Workspace")

    st.write(
        "Explore real radio astronomy observations, "
        "inspect FITS images and analyse scientific data."
    )

    col1, col2, col3 = st.columns(3)
    col1.metric("Data format", "FITS")
    col2.metric("Analysis", "Python")
    col3.metric("Survey", "FIRST / VLA")

    st.info("Select FIRST Survey Explorer to retrieve a real radio image.")

elif page == "FIRST Survey Explorer":
    st.header("FIRST Radio Survey")
    st.write(
        "Retrieve radio image cutouts from the FIRST "
        "1.4 GHz Very Large Array survey."
    )

    with st.form("first_query"):
        ra = st.number_input(
            "Right Ascension (degrees)",
            value=162.530,
            format="%.6f"
        )

        dec = st.number_input(
            "Declination (degrees)",
            value=30.677,
            min_value=-90.0,
            max_value=90.0,
            format="%.6f"
        )

        size = st.select_slider(
            "Image size (arcminutes)",
            options=[1, 2, 3, 4, 5],
            value=3
        )

        submitted = st.form_submit_button(
            "Retrieve FIRST observation"
        )

    if submitted:
        try:
            with st.spinner("Contacting FIRST survey..."):
                image_path = download_first_image(
                    ra, dec, size
                )

            st.session_state["first_image_path"] = str(image_path)
            st.success("FIRST survey image retrieved successfully!")

        except Exception as error:
            st.error(f"Survey retrieval failed: {error}")

    image_path = st.session_state.get("first_image_path")

    if image_path and Path(image_path).exists():
        st.subheader("Retrieved Radio Image")

        try:
            data, header = load_fits(image_path)

            st.pyplot(plot_radio_image(data))

            st.subheader("Image Statistics")
            stats = analyze_image(data)

            c1, c2, c3 = st.columns(3)
            c1.metric("Mean intensity", f"{stats['mean']:.6g}")
            c2.metric("Image standard deviation", f"{stats['std']:.6g}")
            c3.metric("Pixel count", f"{stats['pixels']:,}")

            with st.expander("FITS metadata"):
                st.json({
                    str(k): str(v)
                    for k, v in header.items()
                })

            st.json(check_image_quality(data))

            with open(image_path, "rb") as file:
                st.download_button(
                    "Download FITS observation",
                    data=file,
                    file_name="first_survey_cutout.fits",
                    mime="application/fits"
                )

        except Exception as error:
            st.error(f"Could not display image: {error}")

elif page in ["FITS Explorer", "Image Analysis"]:
    st.header(page)

    uploaded_file = st.file_uploader(
        "Upload astronomical FITS image",
        type=["fits", "fit", "fts"]
    )

    if uploaded_file is not None:
        temp_path = None

        try:
            with tempfile.NamedTemporaryFile(
                suffix=".fits", delete=False
            ) as temp:
                temp.write(uploaded_file.getvalue())
                temp_path = temp.name

            data, header = load_fits(temp_path)

            if page == "FITS Explorer":
                st.success("FITS image loaded successfully.")
                st.pyplot(plot_radio_image(data))

                with st.expander("FITS metadata"):
                    st.json({
                        str(k): str(v)
                        for k, v in header.items()
                    })

            else:
                st.subheader("Image Statistics")
                st.json(analyze_image(data))

                st.subheader("Quality Checks")
                st.json(check_image_quality(data))

                st.pyplot(plot_radio_image(data))

        except Exception as error:
            st.error(f"Could not process FITS image: {error}")

        finally:
            if temp_path and os.path.exists(temp_path):
                os.unlink(temp_path)

elif page == "About":
    st.header("About RadioSkyLab")

    st.write(
        "RadioSkyLab is a scientific computing project "
        "for radio astronomy data exploration and visualisation."
    )

    st.markdown("""
    **Technologies**

    - Python
    - Astropy
    - Astroquery
    - NumPy
    - Matplotlib
    - Streamlit

    **Data source:** FIRST VLA Radio Survey.
    """)
