from Graph.ColorNode import ColorNode
"""
Helper methods for the ColorNode Graph
"""


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


def link_nodes(nodes: dict, node_a: int, node_b: int):
    """
    Adds a two-way link between two nodes
    Both nodes should exist
    :param nodes: dict of ColorNodes
    :param node_a: id number
    :param node_b: id number
    :return:
    """

    __link_node_helper(nodes, node_a, node_b)
    __link_node_helper(nodes, node_b, node_a)


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
