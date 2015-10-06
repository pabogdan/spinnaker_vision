__author__ = 'Petrut Bogdan'

import nengo
import numpy as np


class Retina(nengo.Node):
    def __init__(self, focus_point, image_size=np.asarray([128, 128]),
                 label=None):
        self.focus_point = focus_point
        self.image_size = image_size
        self.image = np.zeros((self.image_size[0], self.image_size[1]))
        super(Retina, self).__init__(output=self.retina_output,
                                     size_out=self.image_size[0] *
                                              self.image_size[1],
                                     label=label)

    def asymetric_pad(self, rand_array):
        start_point = self.focus_point - np.asarray([10, 10])
        for i in range(21):
            for j in range(21):
                rand_array[start_point[0] + i][start_point[1] + j] = \
                    np.random.rand() * .2 + .8
        return rand_array

    def retina_output(self, time):
        self.image = self.asymetric_pad(np.random.rand(self.image_size[0],
                                                       self.image_size[
                                                           1]) * 0.1 + .3)
        return self.image.ravel()

    def set_focus(self, new_focus_point):
        self.focus_point = np.asarray(new_focus_point)
