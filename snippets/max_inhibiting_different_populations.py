from nengo.utils.functions import piecewise

__author__ = 'bogdanp'

import nengo

model = nengo.Network("Maximum")

with model:
    values = nengo.Node(output=piecewise({0:[0, 0, 0, 1], 1:[1, 0.6, -1, 0], 2:[0.8, 1, 0.6, 0.7], 3:[0.8, 1, 0.6, 0],
                                          4:[0.3, .4, .5, .6]}))
    pop1 = nengo.Ensemble(200, 1)
    pop2 = nengo.Ensemble(200, 1)
    pop3 = nengo.Ensemble(200, 1)
    pop4 = nengo.Ensemble(200, 1)
    pops = [pop1,pop2,pop3,pop4]
    # Excitatory connections
    nengo.Connection(values[0], pop1)
    nengo.Connection(values[1], pop2)
    nengo.Connection(values[2], pop3)
    nengo.Connection(values[3], pop4)

    # Inhibitory connections
    for pop_pre in pops:
        for pop_post in pops:
            if pop_pre is not pop_post:
                nengo.Connection(pop_pre, pop_post.neurons, transform=[[-2]] * pop_post.n_neurons)

    # Max
    max_pop = nengo.Ensemble(200, 1)
    nengo.Connection(pop1, max_pop)
    nengo.Connection(pop2, max_pop)
    nengo.Connection(pop3, max_pop)
    nengo.Connection(pop4, max_pop)


