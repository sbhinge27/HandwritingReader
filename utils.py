import numpy as np

def normalize_images(images):
    """Normalize images to have pixel values between 0 and 1."""
    return np.array(images) / 255.0
