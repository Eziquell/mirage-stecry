import cv2
import numpy as np

from skimage.metrics import (
    peak_signal_noise_ratio as psnr_metric
)

from skimage.metrics import (
    mean_squared_error as mse_metric
)


def calculate_psnr(original, stego):

    return psnr_metric(original, stego)


def calculate_mse(original, stego):

    return mse_metric(original, stego)


def generate_error_map(original, stego):

    diff = cv2.absdiff(original, stego)

    heatmap = cv2.applyColorMap(
        diff * 50,
        cv2.COLORMAP_JET
    )

    return heatmap


def calculate_lsb_density(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    lsb = gray & 1

    ones = np.sum(lsb)

    density = (ones / lsb.size) * 100

    return density


def generate_bit_planes(image):

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    planes = []

    for i in range(8):

        plane = (gray >> i) & 1

        planes.append(plane * 255)

    return planes