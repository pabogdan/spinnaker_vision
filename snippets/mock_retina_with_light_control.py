from nengo.utils.functions import piecewise
import vision_models.retina
import vision_models.visualizer
import vision_models.light_controller

vision_models.retina = reload(vision_models.retina)
vision_models.visualizer = reload(vision_models.visualizer)
vision_models.light_controller = reload(vision_models.light_controller)

__author__ = 'Petrut Bogdan'

import nengo
import numpy as np
import nengo_spinnaker

model = nengo.Network("Mock retina")

with model:
    mock_retina = vision_models.retina.Retina(np.asarray([10, 10]))
    visual_cortex = nengo.Ensemble(1800, 400)

    retina_light_control = vision_models.light_controller.LightController(
        mock_retina)

    move_box = nengo.Node(
        piecewise({0: [10, 10], 1: [50, 10], 2: [100, 10], 3: [10, 100], 4:[100,100],
                   5: [50, 50], 6:[120,120], 7:[0,128], 8:[0,0]}))
    nengo.Connection(move_box, retina_light_control)

sim = nengo_spinnaker.Simulator(model)

visualizer = vision_models.visualizer.Visualizer(mock_retina)
visualizer.start()

with sim:
    sim.run(9)
visualizer.close()
