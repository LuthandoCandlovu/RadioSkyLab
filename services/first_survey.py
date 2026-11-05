from pathlib import Path

import astropy.units as u
from astropy.coordinates import SkyCoord
from astropy.io import fits
from astroquery.image_cutouts.first import First


def download_first_image(ra, dec, image_size=3, output_dir="data/raw"):
    """Download a real FITS image cutout from the FIRST survey."""

    coordinates = SkyCoord(
        ra=float(ra) * u.deg,
        dec=float(dec) * u.deg,
        frame="icrs"
    )

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    result = First.get_images(
        coordinates,
        image_size=float(image_size) * u.arcmin
    )

    if result is None:
        raise RuntimeError("The FIRST survey returned no image.")

    if isinstance(result, fits.HDUList):
        hdul = result
    elif isinstance(result, (list, tuple)) and len(result) > 0:
        first_result = result[0]

        if isinstance(first_result, fits.HDUList):
            hdul = first_result
        elif isinstance(first_result, fits.PrimaryHDU):
            hdul = fits.HDUList([first_result])
        else:
            raise RuntimeError("Unexpected FITS response format.")
    else:
        raise RuntimeError("No usable FITS image was returned.")

    filename = output_path / "first_survey_cutout.fits"
    hdul.writeto(filename, overwrite=True)

    return filename


if __name__ == "__main__":
    path = download_first_image(162.530, 30.677, 3)
    print(f"Downloaded FITS image: {path}")
