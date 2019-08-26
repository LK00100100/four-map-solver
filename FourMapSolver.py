from Color import Color
from ColorNode import ColorNode


class FourMapSolver:

    def solve(self, nodes: dict):
        """
        Given an incomplete 4-color-graph,
        it will return a graph solution.

        argument: one connected ColorNode from a 4-color map

        :param nodes: dict of ColorNode
        :return: dict: of solution
        """
        # TODO: check if graph is valid to begin with

        unprocessed_nodes = self.__get_unprocessed_nodes(nodes)

        return self.__solve(nodes, unprocessed_nodes)

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

    def __solve(self, nodes: dict, unprocessed: list):
        """
        Helper for solve
        :param nodes: dict of ColorNode
        :param unprocessed: list of node ids
        :return: if solution, dict of ColorNode. Else, None.
        """

        if self.is_solution(unprocessed):
            return nodes

        for i in range(0, len(unprocessed)):
            node_id = unprocessed[i]
            node = nodes[node_id]

            # TODO: implement ez-answers (only 1 possible answer)

            # fill one color
            unprocessed.remove(node_id)
            for color in Color:
                if color == Color.NONE:
                    continue

                # try to apply a color
                node.color = color
                if not self.is_valid(node):
                    continue

                answer = self.__solve(nodes, unprocessed)
                if answer is not None:
                    return answer

            # undo
            unprocessed.insert(i, node_id)

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
        used_colors = {node.color}

        for neighbor in node.neighbors.values():
            color = neighbor.color

            if color == Color.NONE:
                continue

            if color in used_colors:
                return False

            used_colors.add(color)

        return True
