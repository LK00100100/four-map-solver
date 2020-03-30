from Graph.Color import Color
from Graph.ColorNode import ColorNode


class FourMapSolver:

    @staticmethod
    def solve(nodes: dict):
        """
        Given an incomplete 4-color-graph,
        it will return a graph solution.

        argument: one connected ColorNode from a 4-color map

        :param nodes: dict of ColorNode
        :return: dict: of solution
        """
        # TODO: check if graph is valid to begin with

        unprocessed_nodes = FourMapSolver.__get_unprocessed_nodes(nodes)

        return FourMapSolver.__solve(nodes, unprocessed_nodes)

    @staticmethod
    def __get_unprocessed_nodes(nodes: dict):
        """
        Gets a list of nodes with no color
        :param nodes:
        :return: a list of ids of nodes with no Color
        """
        unprocessed = []
        for node in nodes.values():
            if node.color == Color.NONE:
                unprocessed.append(node.id)

        return unprocessed

    @staticmethod
    def __solve(nodes: dict, unprocessed: list):
        """
        Helper for solve.
        For each spot, there SHOULD be an answer
        :param nodes: dict <id, ColorNode>
        :param unprocessed: list of node ids
        :return: if solution, dict of ColorNode. Else, None.
        """

        if FourMapSolver.is_solution(unprocessed):
            return nodes

        current_index = 0
        node_id = unprocessed[current_index]
        node = nodes[node_id]

        # fill one color
        unprocessed.pop(current_index)
        for color in Color:
            if color == Color.NONE or color == Color.BLACK:
                continue

            # try to apply a color
            node.color = color
            if not FourMapSolver.is_valid(node):
                continue

            answer = FourMapSolver.__solve(nodes, unprocessed)
            if answer is not None:
                return answer

        # undo
        node.color = Color.NONE
        unprocessed.insert(current_index, node_id)

        return None

    @staticmethod
    def is_solution(unprocessed: list):
        """
        True if this graph nothing else to process
        :param unprocessed: list of ids
        :return: True if good
        """
        if len(unprocessed) == 0:
            return True

        return False

    @staticmethod
    def is_valid(node: ColorNode):
        """
        checks to see if node_id has a valid color
        :param node: ColorNode
        :return: True if valid. False otherwise
        """
        used_color = node.color

        for neighbor in node.neighbors.values():
            if neighbor.color == used_color:
                return False

        return True
