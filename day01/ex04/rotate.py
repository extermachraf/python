from PIL import Image
import math
import numpy as np


def rotate_image(image: any, angle: int) -> any:
    angle_rad = math.radians(angle)
    print(image.shape)
    h, w, c = image.shape
    out = np.zeros_like(image)

    cx, cy = w // 2, h // 2
    for y_new in range(h):
        for x_new in range(w):
            # Translate to center
            x_rel = x_new - cx
            y_rel = y_new - cy

            # Apply inverse rotation
            x_old = x_rel * math.cos(angle_rad) + y_rel * math.sin(angle_rad)
            y_old = -x_rel * math.sin(angle_rad) + y_rel * math.cos(angle_rad)

            # Translate back to image coordinates
            x_old = int(round(x_old + cx))
            y_old = int(round(y_old + cy))

            # Copy RGB channels if source is inside image
            if 0 <= x_old < w and 0 <= y_old < h:
                out[y_new, x_new] = image[y_old, x_old]

    return out


def zoom_and_rotate(image: any, start_y: int, end_y: int, start_x: int,
                    end_x: int, angle: int) -> list:
    """
    Zooms into a specific region of the image.
    """
    zommed = image[start_y:end_y, start_x:end_x]
    if zommed.size == 0:
        msg = ("The zoomed area is empty. Please check the start and end "
               "indices.")
        raise ValueError(msg)
    # print("Zoomed shape is:", zommed.shape)
    rotated_image = rotate_image(zommed, angle)
    IMG = Image.fromarray(rotated_image)
    IMG.show()  # Display the zoomed image
    return zommed.tolist()
