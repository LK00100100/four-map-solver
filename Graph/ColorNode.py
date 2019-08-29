from Graph.Color import Color


class ColorNode:
    """
    A ColorNode for a graph
    """

    def __init__(self, node_id: int):
        self.id = node_id
        self.neighbors = {}  # {id#, ColorNode}
        self.color = Color.NONE

    def __str__(self):
        neighbor_str = self.neighbors_to_string()
        return '[{}, {}, {} '.format(self.id, self.color, neighbor_str)

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


def print_graph(color_graph: dict):
    """
    prints a dict of ColorNode
    :param color_graph: dict of ColorNode
    :return:
    """
    if color_graph is None:
        print("Empty graph")
        return

    for color_node in color_graph.values():
        print(color_node)

