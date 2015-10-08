__author__ = 'bogdanp'

import nengo
import numpy as np

model = nengo.Network("Negative inhibition test")

with model:
    some_input = nengo.Node(lambda t: np.sin(t))

    A = nengo.Ensemble(100, 1)

    control = nengo.Node(np.cos)

    nengo.Connection(some_input, A)

    nengo.Connection(control, A.neurons, transform=[[-2.5]]*A.n_neurons, function=lambda x: np.abs(x))