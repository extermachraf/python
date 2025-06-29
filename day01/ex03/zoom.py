from PIL import Image


def zoom(image: any, start_y: int, end_y: int, start_x: int,
         end_x: int) -> list:
    """
    Zooms into a specific region of the image.
    """
    zommed = image[start_y:end_y, start_x:end_x]
    if zommed.size == 0:
        msg = ("The zoomed area is empty. Please check the start and end "
               "indices.")
        raise ValueError(msg)
    print("Zoomed shape is:", zommed.shape)
    print(zommed)
    IMG = Image.fromarray(zommed)
    IMG.show()  # Display the zoomed image
    return zommed.tolist()
