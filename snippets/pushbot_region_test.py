__author__ = 'bogdanp'

import nengo
import numpy as np
import nengo_spinnaker
import nengo_pushbot
from nengo.dists import Uniform

model = nengo.Network("Efficient slicing")

positions = np.arange(128 ** 2).reshape(128, 128)
no_regions = 9

with model:
    bot_network = nengo_pushbot.PushBotNetwork("10.162.177.57")

    bot_network.show_image()


    def send_image(t):
        im = bot_network.bot.image.ravel()
        return im


    image = nengo.Node(send_image)

    regions = []
    max_population = nengo.Ensemble(600, 1, radius=400, label="Maximum")

    for x in range(3):
        for y in range(3):
            # Populations integrating over region of the visual field
            region = nengo.Ensemble(600, 1, radius=400, label="Region {}".format(str(3 * x + y)))
            regions.append(region)

            # Image connections
            positions[:, :] = 0
            positions[x * (128 // 3):(x + 1) * (128 // 3), y * (128 // 3):(y + 1) * (128 // 3)] = 1
            nengo.Connection(image, region, transform=np.asarray([positions.ravel()]),
                             function=lambda x: np.abs(x))

            # Connection to max population

            nengo.Connection(region, max_population)

            # Recurrent connection for temporary memory

            nengo.Connection(region, region, transform=[[.2]], synapse=0.2)

# Inhibitory connections
for pop_pre in regions:
    for pop_post in regions:
        if pop_pre is not pop_post:
            with model:
                nengo.Connection(pop_pre, pop_post.neurons, transform=[[-.5]] * pop_post.n_neurons)


sim = nengo_spinnaker.Simulator(model)
with sim:
    print "Sim started"
    sim.run(10)
    print "Byebye"
