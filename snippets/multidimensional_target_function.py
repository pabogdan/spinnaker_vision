from nengo.utils.connection import target_function

__author__ = 'bogdanp'

import numpy as np
import nengo


model = nengo.Network()

with model:
    inp = nengo.Node(lambda x: [np.cos(x), np.sin(x)])
    ens1 = nengo.Ensemble(200, 2)

    eval_points = [(-1, 1)]
    targets = [(1, 0)]
    nengo.Connection(inp, ens1)

    ens2 = nengo.Ensemble(200, 2)
    nengo.Connection(ens1, ens2, **target_function(eval_points, targets))