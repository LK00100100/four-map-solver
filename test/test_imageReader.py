from unittest import TestCase

from Graph.Color import Color
from Graph.ColorNode import ColorNode
from GraphReader.TextReader import TextReader
from GraphSolver.FourMapSolver import FourMapSolver


class TestFourMapSolverReader(TestCase):

    def test_should_return_correct_solution(self):
        # Arrange
        filename = "sample_input.txt"
        nodes = TextReader.read_graph(filename)

        # Act
        solved_nodes = FourMapSolver.solve(nodes)

        # Assert
        # make sure each node's color is good
        for color_node in solved_nodes.values():  # type: ColorNode
            current_color = color_node.color
            self.assertNotEqual(Color.NONE, current_color)

            # make sure the neighbors use a different color
            for child_node in color_node.neighbors.values():  # type: ColorNode
                child_color = child_node.color
                self.assertNotEqual(current_color, child_color)
