from load_image import ft_load
import matplotlib.pyplot as plt


def main():
    """
    zooms on a pretty animal and shows it in grey scales
    """
    path = "/home/ael-atmi/Cursus/PicPython/1_Array/res/animal.jpeg"
    try:
        img = ft_load(path)
        print(img)
        zoom = img[100:500, 450:850, :1]
        print('New shape after slicing :', zoom.shape)
        print(zoom)
        plt.imshow(zoom, cmap='grey')
        plt.show()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("Program interrupted")


if __name__ == "__main__":
    main()
