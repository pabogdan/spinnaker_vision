__author__ = 'bogdanp'

from retina import Retina
import nengo
import numpy as np


class ReducedRetina(Retina):
    def __init__(self, focus_point, output_size=np.asarray([3, 3]), image_size=np.asarray([128, 128]),
                 label=None):
        self.output_size = output_size
        super(ReducedRetina, self).__init__(focus_point, image_size, label)
        self.size_out = output_size[0] * output_size[1]

    def retina_output(self, time):
        original_image = super(ReducedRetina, self).retina_output(time)

        output_raveled_size = self.output_size[0] * self.output_size[1]

        image = original_image[0:
        ((self.image_size[0] * self.image_size[1]) // output_raveled_size * output_raveled_size)].reshape(
            self.output_size[0],
            self.output_size[1],
            (self.image_size[0] * self.image_size[1]) // (
                output_raveled_size))

        reduced_image = np.sum(image, axis=2)
        print np.max(reduced_image)
        return reduced_image.ravel()
