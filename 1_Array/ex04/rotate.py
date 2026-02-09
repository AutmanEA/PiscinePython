from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def my_transpose(arr2D: list) -> list:
    """
    takes an array 2D and reverses or permutes the axes of an array
    """
    return [[arr2D[y][x] for y in range(len(arr2D))]
            for x in range(len(arr2D[0]))]


def main():
    """
    rotates a pretty animal and shows it in grey scales
    """
    path = "/home/ael-atmi/Cursus/PicPython/1_Array/res/animal.jpeg"
    try:
        img = ft_load(path)
        print(img)
        rotate = np.array(my_transpose(img[:, :, 0]))
        print('New shape after Transpose :', rotate.shape)
        print(rotate)
        plt.imshow(rotate, cmap='grey')
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interrupted")


if __name__ == "__main__":
    main()
