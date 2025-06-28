import numpy as np
import matplotlib.pyplot as plt
import math
from PIL import Image

# -------------------------
# Load Image as RGB
# -------------------------
def ft_load(path: str) -> np.ndarray:
    img = Image.open(path).convert("RGB")
    array = np.array(img)
    print("Image shape:", array.shape)
    return array

# -------------------------
# Channel Rotation (Forward)
# -------------------------
def rotate_channel_forward(channel, angle_deg):
    angle_rad = math.radians(angle_deg)
    h, w = channel.shape
    out = np.zeros_like(channel)
    cx, cy = w // 2, h // 2

    for y in range(h):
        for x in range(w):
            x_rel, y_rel = x - cx, y - cy
            x_rot = int(round(x_rel * math.cos(angle_rad) - y_rel * math.sin(angle_rad)))
            y_rot = int(round(x_rel * math.sin(angle_rad) + y_rel * math.cos(angle_rad)))
            x_new = x_rot + cx
            y_new = y_rot + cy
            if 0 <= x_new < w and 0 <= y_new < h:
                out[y_new][x_new] = channel[y][x]
    return out

# -------------------------
# Channel Rotation (Inverse)
# -------------------------
def rotate_channel_inverse(channel, angle_deg):
    angle_rad = math.radians(angle_deg)
    h, w = channel.shape
    out = np.zeros_like(channel)
    cx, cy = w // 2, h // 2

    for y_new in range(h):
        for x_new in range(w):
            x_rel, y_rel = x_new - cx, y_new - cy
            x_old = x_rel * math.cos(angle_rad) + y_rel * math.sin(angle_rad)
            y_old = -x_rel * math.sin(angle_rad) + y_rel * math.cos(angle_rad)
            x_old = int(round(x_old + cx))
            y_old = int(round(y_old + cy))
            if 0 <= x_old < w and 0 <= y_old < h:
                out[y_new][x_new] = channel[y_old][x_old]
    return out

# -------------------------
# Full RGB Rotation Function
# -------------------------
def rotate_rgb_image(img: np.ndarray, angle_deg: float, inverse: bool) -> np.ndarray:
    channels = []
    for i in range(3):
        channel = img[:, :, i]
        if inverse:
            rotated = rotate_channel_inverse(channel, angle_deg)
        else:
            rotated = rotate_channel_forward(channel, angle_deg)
        channels.append(rotated)
    return np.stack(channels, axis=2)

# -------------------------
# Plotting Comparison
# -------------------------
def plot_rgb_comparison(original, forward, inverse, angle):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    axes[0].imshow(original)
    axes[0].set_title("Original")
    axes[1].imshow(forward)
    axes[1].set_title(f"Forward Mapping ({angle}°)")
    axes[2].imshow(inverse)
    axes[2].set_title(f"Inverse Mapping ({angle}°)")

    for ax in axes:
        ax.axis("off")
    plt.tight_layout()
    plt.show()

# -------------------------
# Run It All
# -------------------------
if __name__ == "__main__":
    # Load and crop image for speed
    img = ft_load("/home/achraf/42-projects/pythonpicine/images/animal.jpeg")
    # img = img[0:150, 0:150, :]  # Optional: small patch

    angle = 45  # Try 90, 180, -45
    forward_rotated = rotate_rgb_image(img, angle, inverse=False)
    inverse_rotated = rotate_rgb_image(img, angle, inverse=True)

    plot_rgb_comparison(img, forward_rotated, inverse_rotated, angle)
