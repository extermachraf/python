from PIL import Image
from load_image import ft_load
import pimp_image
import numpy as np


def main():
    array = ft_load("/home/achraf/42-projects/pythonpicine/images/image.png")
    # result = pimp_image.ft_invert(array)
    result = pimp_image.ft_grey(array)
    result = np.clip(result, 0, 255).astype(np.uint8)
    IMG = Image.fromarray(result)
    IMG.show()
    return


if __name__ == "__main__":
    main()
