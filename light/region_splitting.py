import nengo
import numpy as np


class RegionSplitter(nengo.Network):
    def __init__(self, input_node, array_like_regions=np.zeros((3, 3)), label=None, seed=None,
                 add_to_container=None):
        super(RegionSplitter, self).__init__(label, seed,
                                             add_to_container)
        self.input_node = input_node
        self.array_like_regions = array_like_regions
        if type(array_like_regions) != np.ndarray:
            self.array_like_regions = np.asarray(array_like_regions)

        # Positions I'm looking for

        all_positions = np.arange(input_node.size_out).reshape(np.round(np.sqrt(input_node.size_out)), np.round(np.sqrt(input_node.size_out)))

        with self:
            self.regions = np.array(np.zeros((self.array_like_regions.shape[0], self.array_like_regions.shape[1])),
                                    dtype=nengo.Ensemble)

            for x in range(self.regions.shape[0]):
                for y in range(self.regions.shape[1]):
                    self.regions[x][y] = nengo.Ensemble(
                        n_neurons=800, dimensions=1,
                        radius=(all_positions.shape[1] // self.regions.shape[1]) * (all_positions.shape[0] // self.regions.shape[0]))

                    for position in all_positions[(all_positions.shape[0] // self.regions.shape[0]) * x : (all_positions.shape[1] // self.regions.shape[1]) * y,
                                                  (all_positions.shape[0] // self.regions.shape[0]) * (x + 1) : (all_positions.shape[1] // self.regions.shape[1]) * (y + 1)].ravel():
                        nengo.Connection(self.input_node[position], self.regions[x][y])





