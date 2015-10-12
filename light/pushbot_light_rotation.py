__author__ = 'bogdanp'

import nengo
import numpy as np
import nengo_spinnaker
import nengo_pushbot

model = nengo.Network("Efficient slicing")

positions = np.arange(128 ** 2).reshape(128, 128)
no_regions = 9

with model:
    bot_network = nengo_pushbot.PushBotNetwork("10.162.177.57")

    bot_network.show_image()

    region_network = nengo.Network("Regions")


    def send_image(t):
        im = bot_network.bot.image.ravel()
        return im


    image = nengo.Node(send_image)

    regions = []
    max_population = nengo.Ensemble(600, 1, radius=400, label="Maximum")

    for x in range(3):
        for y in range(3):
            # Populations integrating over region of the visual field
            with region_network:
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


# Pooling
with model:
    motor_control = nengo.Ensemble(400, 1, radius=.3)

    for index in range(len(regions)):
        if index % 3 == 0:
            nengo.Connection(regions[index], motor_control, synapse=0.1, transform=[[.01]])
        elif index % 3 == 2:
            nengo.Connection(regions[index], motor_control, synapse=0.1, transform=[[-.01]])

    nengo.Connection(motor_control, bot_network.motor, synapse=0.1, transform=[[-1], [1]])

sim = nengo_spinnaker.Simulator(model)
with sim:
    print "Sim started"
    sim.run(10)
    print "Byebye"
