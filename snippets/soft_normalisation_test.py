__author__ = 'bogdanp'


import nengo
import numpy as np

model = nengo.Network("Soft normalisation")

with model:
    some_input = nengo.Node(400)

    A = nengo.Ensemble(50, 1, .5)

    nengo.Connection(some_input, A)