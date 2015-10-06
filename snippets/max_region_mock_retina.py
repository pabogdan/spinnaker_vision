__author__ = 'bogdanp'

import vision_models.reduced_retina
vision_models.retina = reload(vision_models.reduced_retina)
import nengo
import numpy as np

model = nengo.Network("Max region of reduced dimensions retina")

with model:
    mock_retina = vision_models.reduced_retina.ReducedRetina(np.asarray([10, 10]))
    regions = []
    max_population = nengo.Ensemble(500, 1, radius=900, label="Maximum")
    for index in range(mock_retina.size_out):
        # Populations integrating over region of the visual field
        region = nengo.Ensemble(500, 1, radius=900, label="Region {}".format(str(index)))
        regions.append(region)

        # Excitatory connections
        nengo.Connection(mock_retina[index], regions[index])
        nengo.Connection(regions[index], max_population)

# Inhibitory connections
for pop_pre in regions:
    for pop_post in regions:
        if pop_pre is not pop_post:
            with model:
                nengo.Connection(pop_pre, pop_post.neurons, transform=[[-.01]] * pop_post.n_neurons)

sim = nengo.Simulator(model)

sim.run(10)
