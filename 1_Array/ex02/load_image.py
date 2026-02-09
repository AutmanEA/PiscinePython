import numpy as np
import matplotlib.image as mpimg


def ft_load(path: str) -> np.array:
    """
    ft_load loads an image and returns all pixels in RGB array
    and prints his format
    - raises Exception on bad image
    """
    if (not isinstance(path, str)):
        raise Exception("Bad path format for image")
    try:
        img = mpimg.imread(path)
    except Exception:
        raise Exception("No file to read or not an image")
    print('The shape of image is :', img.shape)
    return img
