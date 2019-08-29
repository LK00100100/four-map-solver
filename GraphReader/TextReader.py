from Graph import GraphHelper
from Graph.Color import Color


class TextReader:
    """
    Reads a file and turns it into a ColorNode graph

    It's recommended that you use the ImageReader
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
                    nodes = GraphHelper.init_map(int(right))
                    continue

                # connect node
                if right.isnumeric():
                    node_a = int(left)
                    node_b = int(right)
                    GraphHelper.link_nodes(nodes, node_a, node_b)
                    continue

                # init color
                node_a = int(left)
                color = Color[right]
                nodes[node_a].color = color

        return nodes
