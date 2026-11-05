import numpy as np

def analyze_image(data):
    """Calculate basic astronomical image statistics."""
    values = np.asarray(data, dtype=float)
    valid = values[np.isfinite(values)]

    if valid.size == 0:
        raise ValueError("Image contains no finite pixel values.")

    return {
        "mean": float(np.mean(valid)),
        "median": float(np.median(valid)),
        "std": float(np.std(valid)),
        "minimum": float(np.min(valid)),
        "maximum": float(np.max(valid)),
        "pixels": int(valid.size)
    }
