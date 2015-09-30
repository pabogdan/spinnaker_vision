__author__ = 'Petrut Bogdan'


import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.cm as cm
from threading import Thread
import numpy as np

class Visualizer(Thread):
    def __init__(self, mock_retina):
        self.mock_retina = mock_retina
        super(Visualizer, self).__init__(name="Mock retina visualizer thread")
        self.halt = False

    def run(self):
        print "Running viz thread"
        self.fig = plt.figure()
        self.im = plt.imshow(self.f(), cmap=cm.Greys_r)
        self.ani = animation.FuncAnimation(self.fig, self.updatefig, interval=10, blit=True)
        plt.show()
        while not self.halt:
            pass
        print "Stopped viz thread"

    def close(self):
        self.halt = True

    def f(self):
        return self.mock_retina.image

    def updatefig(self, *args):
        self.im.set_array(self.f())
        return self.im,

