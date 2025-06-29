import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list from start to end index and prints shapes before and
    after slicing.
    """
    if not all(len(row) == len(family[0]) for row in family):
        raise AssertionError("All rows in the list must have the same length")
    array = np.array(family)
    print("My shape is:", array.shape)
    new_array = array[start:end]
    print("My new shape is:", new_array.shape)
    return new_array.tolist()
