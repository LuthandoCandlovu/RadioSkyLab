from astropy.io import fits
import numpy as np

def load_fits(file_path):
    """Load a FITS astronomical image."""
    with fits.open(file_path) as hdul:
        hdul.verify("silentfix")
        for hdu in hdul:
            if hdu.data is not None:
                data = np.squeeze(np.asarray(hdu.data))
                if data.ndim == 2:
                    return data, dict(hdu.header)

    raise ValueError("No 2D image found in FITS file.")

