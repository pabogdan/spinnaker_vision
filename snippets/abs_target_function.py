from nengo.utils.connection import target_function

__author__ = 'bogdanp'

import numpy as np
import nengo


model = nengo.Network()

with model:
    inp = nengo.Node(lambda x: np.cos(x))
    ens1 = nengo.Ensemble(100, 1)

    eval_points = np.arange(-1, 1, .001)
    targets = np.abs(eval_points)
    nengo.Connection(inp, ens1)

    ens2 = nengo.Ensemble(100, 1)
    nengo.Connection(ens1, ens2, **target_function(eval_points, targets))