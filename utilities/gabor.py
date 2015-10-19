"""
This module's contents have been created by Terry Stewart, Postdoc at University of
Waterloo, Canada.

Original code available at
https://github.com/tcstewar/testing_notebooks/blob/master/Gabor.ipynb
"""

import numpy as np


def generate_gabor(width, height, lambd, theta, psi, sigma, gamma, x_offset, y_offset):
    """
    Generate a linear filter used for edge detection. Frequency and orientation representations of Gabor
    filters are similar to those of the human visual system.

    :param width: width of the resulting filter
    :param height: height of the resulting filter
    :param lambd: wavelength of the sinusoidal factor
    :param theta: orientation of the normal to the parallel stripes of a Gabor function
    :param psi: phase offset
    :param sigma: sigma/standard deviation of the Gaussian envelope
    :param gamma: is the spatial aspect ratio
    :param x_offset: horizontal offset from center
    :param y_offset: vertical offset from center
    :return:
    """
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    X = X - x_offset
    Y = Y + y_offset

    cosTheta = np.cos(theta)
    sinTheta = np.sin(theta)
    xTheta = X * cosTheta + Y * sinTheta
    yTheta = -X * sinTheta + Y * cosTheta
    e = np.exp(-(xTheta ** 2 + yTheta ** 2 * gamma ** 2) / (2 * sigma ** 2))
    cos = np.cos(2 * np.pi * xTheta / lambd + psi)

    return e * cos


def make_random_gabor(width, height):
    """
    Generate a Gabor filter with slightly randomised variables.

    :param width: width of the resulting filter
    :param height: height of the resulting filter
    :return:
    """
    return generate_gabor(width, height,
                          lambd=np.random.uniform(0.3, 0.8),
                          theta=np.random.uniform(0, 2 * np.pi),
                          psi=np.random.uniform(0, 2 * np.pi),
                          sigma=np.random.uniform(0.2, 0.5),
                          gamma=np.random.uniform(0.4, 0.8),
                          x_offset=np.random.uniform(-1, 1),
                          y_offset=np.random.uniform(-1, 1))
