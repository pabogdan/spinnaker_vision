from nengo.utils.functions import piecewise

__author__ = 'bogdanp'

from utilities.gabor import generate_gabor, make_random_gabor_at_orientation
import nengo
import numpy as np
from nengo.utils.connection import target_function

model = nengo.Network("Small training scenario")


def generate_eval_points_and_targets(no_training_examples=1000):
    eval_points = []
    targets = []
    theta_values = [0, np.pi / 4., np.pi / 2., 3 * np.pi / 4.]
    for theta in theta_values:
        for no in range(no_training_examples):
            eval_points.append(tuple(make_random_gabor_at_orientation(5, 5, theta).ravel()))
            if np.isclose(theta, np.pi / 4.):
                targets.append((1, 1))
            else:
                targets.append((0, 0))
    return eval_points, targets


with model:
    inp = nengo.Node(output=piecewise({0: make_random_gabor_at_orientation(5, 5, 0).ravel(),
                                       10: make_random_gabor_at_orientation(5, 5, np.pi / 4.).ravel(),
                                       20: make_random_gabor_at_orientation(5, 5, np.pi / 2.).ravel(),
                                       30: make_random_gabor_at_orientation(5, 5, 3 * np.pi / 4.).ravel()}))

    input_ensemble = nengo.Ensemble(1000, 25)
    nengo.Connection(inp, input_ensemble)

    orientation = nengo.Ensemble(1000, 2)

    eval_points, targets = generate_eval_points_and_targets()

    nengo.Connection(input_ensemble, orientation, **target_function(eval_points, targets))
