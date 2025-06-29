import numpy as np
from PIL import Image


def ft_load(path: str) -> any:
    """
    Loads an image from the given file path, prints its shape, and returns
    the image as a nested list.
    """
    img = Image.open(path)
    # print("Mode:", img.mode)
    array = np.array(img)
    # print("My shape is:", array.shape)
    # print(array)
    return array
