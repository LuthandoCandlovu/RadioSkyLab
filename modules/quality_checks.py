import numpy as np

def check_image_quality(data):
    """Check basic numerical image quality."""
    values = np.asarray(data, dtype=float)

    return {
        "shape": values.shape,
        "finite_pixels": int(np.isfinite(values).sum()),
        "non_finite_pixels": int((~np.isfinite(values)).sum()),
        "has_valid_data": bool(np.isfinite(values).any())
    }
