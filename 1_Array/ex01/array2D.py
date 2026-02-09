import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    - slice_me takes an array family and :
      - prints his shape
      - slices it with start and end
      - prints and returns his new shape
    - raises exception on failure
    """
    if not (isinstance(family, list)):
        raise Exception("Parameter family must be a list")
    if not (isinstance(start, int) and isinstance(end, int)):
        raise Exception("Parameters start and/or end must be integers")
    arr = np.array(family)
    print('My shape is :', arr.shape)
    slice_arr = arr[start:end]
    print('My new shape is :', slice_arr.shape)
    return slice_arr.tolist()
