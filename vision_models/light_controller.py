__author__ = 'Petrut Bogdan'

import nengo
import numpy as np


class LightController(nengo.Node):
    def __init__(self, retina,
                 label=None):
        self.retina = retina
        super(LightController, self).__init__(output=self.controller_output,
                                              size_in=2,
                                              label=label)

    def controller_output(self, time, value):
        self.retina.set_focus(np.asarray(value))
