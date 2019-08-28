from Graph.Color import Color
from Graph.ColorNode import ColorNode


class TextReader:
    """
    Reads a file and turns it into a ColorNode graph
    """

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
                    nodes = TextReader.init_map(int(right))
                    continue

                # connect node
                if right.isnumeric():
                    node_a = int(left)
                    node_b = int(right)
                    TextReader.link_nodes(nodes, node_a, node_b)
                    continue

                # init color
                node_a = int(left)
                color = Color[right]
                nodes[node_a].color = color

        return nodes

    # TODO: move these graph-related methods out

    @staticmethod
    def init_map(node_nums: int):
        """
        init a graph from 1 to node_nums (inclusive)
        :param node_nums: number of nodes in the graph
        :return: graph of nodes
        """
        nodes = {}
        for i in range(1, node_nums + 1):
            nodes[i] = ColorNode(i)

        return nodes

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

        TextReader.__link_node_helper(nodes, node_a, node_b)
        TextReader.__link_node_helper(nodes, node_b, node_a)

    @staticmethod
    def __link_node_helper(nodes: dict, node_a: int, node_b: int):
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
