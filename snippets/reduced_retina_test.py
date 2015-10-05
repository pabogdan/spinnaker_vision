import vision_models.reduced_retina
vision_models.retina = reload(vision_models.reduced_retina)

__author__ = 'bogdanp'

import nengo
import numpy as np

model = nengo.Network("Reduced dimensions retina")

with model:
    mock_retina = vision_models.reduced_retina.ReducedRetina(np.asarray([10, 10]))
    visual_cortex = nengo.Ensemble(800, 9, radius=1900)

    nengo.Connection(mock_retina, visual_cortex)


sim = nengo.Simulator(model)

sim.run(10)
