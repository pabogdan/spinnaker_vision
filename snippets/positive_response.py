from nengo.dists import Uniform

__author__ = 'bogdanp'

import nengo
import numpy as np

model = nengo.Network("Positive response")

with model:
    sine = nengo.Node(np.sin)

    A = nengo.Ensemble(50, 1, encoders=Uniform(0, 1.), intercepts=Uniform(0, 0))

    nengo.Connection(sine, A)
