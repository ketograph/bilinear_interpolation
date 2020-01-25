#!/usr/bin env python3
# coding=utf-8

import numpy as np
from math import floor, ceil


def interpolate(first_value: float, second_value: float, ratio: float) -> float:
    """Interpolate with a linear weighted sum."""
    return first_value * (1 - ratio) + second_value * ratio


def get_array_value(x: int, y: int, array: np.ndarray):
    """Returns the value of the array at position x,y."""
    return array[y, x]


def bilinear_interpolation(x: float, y: float, img: np.ndarray) -> float:
    """Returns the bilinear interpolation of a pixel in the image.

    :param x: x-position to interpolate
    :param y: y-position to interpolate
    :param img: image, where the pixel should be interpolated
    :returns: value of the interpolated pixel
    """
    if x < 0 or y < 0:
        raise ValueError("x and y pixel position have to be positive!")
    if img.shape[1] - 1 < x or img.shape[0] - 1 < y:
        raise ValueError(
            "x and y pixel position have to be smaller than image" "dimensions."
        )

    x_rounded_up = int(ceil(x))
    x_rounded_down = int(floor(x))
    y_rounded_up = int(ceil(y))
    y_rounded_down = int(floor(y))

    ratio_x = x - x_rounded_down
    ratio_y = y - y_rounded_down

    interpolate_x1 = interpolate(
        get_array_value(x_rounded_down, y_rounded_down, img),
        get_array_value(x_rounded_up, y_rounded_down, img),
        ratio_x,
    )
    interpolate_x2 = interpolate(
        get_array_value(x_rounded_down, y_rounded_up, img),
        get_array_value(x_rounded_up, y_rounded_up, img),
        ratio_x,
    )
    interpolate_y = interpolate(interpolate_x1, interpolate_x2, ratio_y)

    return interpolate_y


if __name__ == "__main__":
    image = np.arange(0, 9).reshape((3, 3))
    print(bilinear_interpolation(0.5, 1.5, image))
