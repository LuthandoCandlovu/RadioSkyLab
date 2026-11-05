import matplotlib.pyplot as plt
import numpy as np

from astropy.wcs import WCS
from astropy.wcs.utils import proj_plane_pixel_scales


def plot_radio_image(data, header=None):
    """
    Display a radio astronomy image.

    If a valid FITS header is supplied, display
    celestial Right Ascension and Declination axes.
    """

    image_data = np.asarray(data)

    if image_data.ndim != 2:
        raise ValueError(
            f"Expected a 2D image, received {image_data.ndim}D data."
        )

    if header is not None:
        try:
            wcs = WCS(header).celestial

            if wcs.has_celestial:
                fig = plt.figure(figsize=(10, 8))
                ax = fig.add_subplot(111, projection=wcs)

                image = ax.imshow(
                    image_data,
                    origin="lower",
                    cmap="inferno",
                    interpolation="nearest"
                )

                ax.set_xlabel("Right Ascension (J2000)")
                ax.set_ylabel("Declination (J2000)")

                ax.coords[0].set_axislabel(
                    "Right Ascension (J2000)"
                )
                ax.coords[1].set_axislabel(
                    "Declination (J2000)"
                )

                ax.coords.grid(
                    color="white",
                    linestyle=":",
                    alpha=0.5
                )

                ax.set_title(
                    "FIRST Radio Astronomy Image - WCS Coordinates"
                )

                unit = header.get("BUNIT", "Intensity")

                fig.colorbar(
                    image,
                    ax=ax,
                    label=f"Flux Density ({unit})"
                )

                fig.tight_layout()
                return fig

        except Exception as error:
            print(f"WCS unavailable, using pixel coordinates: {error}")

    # Fallback for images without valid celestial WCS
    fig, ax = plt.subplots(figsize=(10, 8))

    image = ax.imshow(
        image_data,
        origin="lower",
        cmap="inferno",
        interpolation="nearest"
    )

    ax.set_title("Radio Astronomy Intensity Image")
    ax.set_xlabel("Pixel X")
    ax.set_ylabel("Pixel Y")

    unit = header.get("BUNIT", "Pixel intensity") if header else "Pixel intensity"

    fig.colorbar(image, ax=ax, label=unit)
    fig.tight_layout()

    return fig
