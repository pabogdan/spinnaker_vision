from nengo.utils.functions import piecewise

__author__ = 'bogdanp'

import nengo
import numpy as np
import nengo_spinnaker
import nengo_pushbot
from nengo.dists import Uniform

model = nengo.Network("Pushbot motor control")


with model:
    bot_network = nengo_pushbot.PushBotNetwork("10.162.177.57")

    positions = nengo.Node(piecewise({0:[0,0], 1:[.5,-.5], 2:[0, 0], 3:[-.5, .5] , 4:[0, 0]}))

    motor_signal = nengo.Ensemble(200, dimensions=2, radius=1)


    nengo.Connection(positions, motor_signal)

    nengo.Connection(motor_signal, bot_network.motor)


sim = nengo_spinnaker.Simulator(model)

with sim:
    print "Starting sim"

    sim.run(5)

    print "Bye!"
