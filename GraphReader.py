from Color import Color
from ColorNode import ColorNode


class GraphReader:

    @staticmethod
    def read_graph(filename: str):
        """
        Reads a file with graph data
        and returns a graph.
        Comments are ignored

        File must have lines with any of the formats below:
        id# id#
        id# Color
        'nodes' #-of-numbers

        List colors definition after link

        :param filename:
        :return ColorNode: that is connected
        """
        nodes = {}

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()

                if line.startswith("#"):
                    continue

                if len(line) == 0:
                    continue

                left, right = line.split(' ')

                # init nodes
                if left.lower() == 'nodes':
                    GraphReader.init_map(nodes, int(right))
                    continue

                # connect node
                if right.isnumeric():
                    node_a = int(left)
                    node_b = int(right)
                    GraphReader.link_nodes(nodes, node_a, node_b)
                    continue

                # init color
                node_a = int(left)
                color = Color[right]
                nodes[node_a].color = color

        return nodes

    @staticmethod
    def init_map(nodes: dict, node_nums: int):
        for i in range(1, node_nums + 1):
            nodes[i] = ColorNode(i)

    @staticmethod
    def link_nodes(nodes: dict, node_a: int, node_b: int):
        """
        Adds a two-way link between two nodes
        Both nodes should exist
        :param nodes: dict of ColorNodes
        :param node_a: id number
        :param node_b: id number
        :return:
        """

        GraphReader.link_node_helper(nodes, node_a, node_b)
        GraphReader.link_node_helper(nodes, node_b, node_a)

    @staticmethod
    def link_node_helper(nodes: dict, node_a: int, node_b: int):
        """
        Links one way
        :param nodes: dict of ColorNode
        :param node_a: id
        :param node_b: id
        :return:
        """
        color_node_a = nodes[node_a]
        color_node_b = nodes[node_b]

        color_node_a.neighbors[node_b] = color_node_b
