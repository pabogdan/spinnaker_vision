import vision_models.retina
import vision_models.visualizer

vision_models.retina = reload(vision_models.retina)
vision_models.visualizer = reload(vision_models.visualizer)

__author__ = 'Petrut Bogdan'

import nengo
import numpy as np

model = nengo.Network("Mock retina")

with model:
    mock_retina = vision_models.retina.Retina(np.asarray([10, 10]))
    visual_cortex = nengo.Ensemble(1800, 400)
    # nengo.Connection(mock_retina, visual_cortex)


sim = nengo.Simulator(model)

visualizer = vision_models.visualizer.Visualizer(mock_retina)
visualizer.start()

sim.run(5)
visualizer.close()
