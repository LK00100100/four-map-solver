from Color import Color


class ColorNode:
    def __init__(self, node_id):
        self.id = node_id
        self.neighbors = {}  # {id#, ColorNode}
        self.color = Color.NONE

    def __str__(self):
        neighbor_str = self.neighbors_to_string()
        return '[{} {} {} '.format(self.id, self.color, neighbor_str)

    def neighbors_to_string(self):
        """
        returns the list of neighbors
        :return: a neighbor of ids
        """
        neighbors_str = 'neighbors['
        for key in self.neighbors.keys():
            neighbors_str += str(key) + ' '

        neighbors_str = neighbors_str.strip()

        neighbors_str += ']'

        return neighbors_str
