import numpy as np
import matplotlib.pyplot as plt


def set_image_colors(img: np.array, r=None, g=None, b=None, grey=False) -> np.array:
    """
    Changes image colors pixel by pixel
    applying a function for each colors rgb based.
    """
    new_img = img.copy()
    for x in new_img:
        for y in x:
            if r:
                y[0] = r(y[0])
            if g:
                y[1] = g(y[1])
            if b:
                y[2] = b(y[2])
            if grey:
                y[0] = y[1] = y[2] = np.mean(y)
    return new_img


def ft_invert(arr: np.array) -> np.array:
    """Inverts the color of the image received."""
    new_arr = set_image_colors(arr,
                               lambda x: 255 - x,
                               lambda x: 255 - x,
                               lambda x: 255 - x)
    print(new_arr)
    plt.imshow(new_arr)
    plt.show()
    return new_arr


def ft_red(arr: np.array) -> np.array:
    """Applies red filter to the image received."""
    new_arr = set_image_colors(arr, g=lambda x: 0, b=lambda x: 0)
    print(new_arr)
    plt.imshow(new_arr)
    plt.show()
    return new_arr


def ft_green(arr: np.array) -> np.array:
    """Applies green filter to the image received."""
    new_arr = set_image_colors(arr, r=lambda x: 0, b=lambda x: 0)
    print(new_arr)
    plt.imshow(new_arr)
    plt.show()
    return new_arr


def ft_blue(arr: np.array) -> np.array:
    """Applies blue filter to the image received."""
    new_arr = set_image_colors(arr, r=lambda x: 0, g=lambda x: 0)
    print(new_arr)
    plt.imshow(new_arr)
    plt.show()
    return new_arr


def ft_grey(arr: np.array) -> np.array:
    """Applies grey scale to the image received."""
    new_arr = set_image_colors(arr, grey=True)
    print(new_arr)
    plt.imshow(new_arr)
    plt.show()
    return new_arr
