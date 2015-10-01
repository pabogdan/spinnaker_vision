import nengo
from nengo.processes import WhiteNoise
from nengo.utils.functions import piecewise
import numpy as np
import numpy as np

model = nengo.Network(label="NetworkName")

with model:
    inp = nengo.Node(piecewise({0:.5, 0.5:0}))
    pop = nengo.Ensemble(100, 1)
    nengo.Connection(inp, pop)
    nengo.Connection(pop, pop, synapse=0.1)

    inhib = nengo.Node(1)

    nengo.Connection(inhib, pop.neurons, transform=[[-0.2]]*pop.n_neurons, synapse=0.1)


