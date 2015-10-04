from nengo.networks import BasalGanglia
import light.region_splitting
import vision_models.retina
import vision_models.visualizer

vision_models.retina = reload(vision_models.retina)
vision_models.visualizer = reload(vision_models.visualizer)
light.region_splitting = reload(light.region_splitting)


__author__ = 'bogdanp'


import nengo
import numpy as np

model = nengo.Network("Region splitter test")



with model:
    mock_retina = vision_models.retina.Retina(np.asarray([10, 10]))
    splitter = light.region_splitting.RegionSplitter(mock_retina)

    basal_ganglia = BasalGanglia(9, 100)

    for x in range(splitter.regions.shape[0]):
        for y in range(splitter.regions.shape[1]):
            nengo.Connection(splitter.regions[x][y], basal_ganglia.input[x+y])