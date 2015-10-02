from nengo.networks import EnsembleArray, BasalGanglia, Thalamus

__author__ = 'bogdanp'

import nengo
import nengo_spinnaker
import nengo_pushbot
import numpy

no_rows = 3
no_columns = 3
image_size = 128 ** 2

frequency = 100  # Hz

model = nengo.Network("Splitting image into regions")


def quick_check(x):
    print x

with model:
    bot_network = nengo_pushbot.PushBotNetwork("10.162.177.57")
    bot_network.show_image()
    image_input = nengo.Node(bot_network.bot.image.ravel())
    regions = EnsembleArray(n_neurons=100, n_ensembles=no_rows * no_columns, ens_dimensions=1,
                            radius=image_size / (no_rows * no_columns))

    for row in range(no_rows):
        for column in range(no_columns):
            for actual_row in range(128 / no_rows * row, 128 / no_rows * (row + 1)):
                for actual_column in range(128 / no_rows * row, 128 / no_rows * (row + 1)):
                    nengo.Connection(image_input[actual_row + 128 * actual_column], regions.input[row + column])

    bg = BasalGanglia(no_rows * no_columns)

    nengo.Connection(regions.output, bg.input)

    thalamus = Thalamus(no_rows * no_columns, 100)

    nengo.Connection(bg.output, thalamus.input)

    output = nengo.Ensemble(600, dimensions=no_rows*no_columns)

    nengo.Connection(bg.output, output, function=quick_check)


sim = nengo_spinnaker.Simulator(model)
with sim:
    sim.run(60)
