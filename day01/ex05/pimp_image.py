from PIL import Image
import numpy as np

def ft_invert(array):
    inverted_array = 255 - array
    return inverted_array

def ft_red(array):
    result = array * [1, 0, 0]
    return result

def ft_green(array):
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 2] = 0
    return result

def ft_blue(array):
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result

def ft_grey(array):
    grey = (array[:, :, 0] + array[:, :, 1] + array[:, :, 2]) / 3
    # return np.repeat(grey[:, :, None], 3, axis=2)
    return grey