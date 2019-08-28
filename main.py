# solves the 4-color-map game on Mobaxterm
# python 3.7
# author lk00100100
from FourMapSolver import FourMapSolver
from GraphReader import GraphReader
from datetime import datetime

from ImageReader import ImageReader


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


def solve(unsolved_graph: dict):
    print("start:", datetime.now())
    solution = FourMapSolver().solve(unsolved_graph)
    print("end  :", datetime.now())
    return solution


# get graph
# filename = 'samples/graph1.txt'
# graph = GraphReader.read_graph(filename)

filename = 'samples/map-sample1.png'
img_reader = ImageReader()
graph = img_reader.convert_to_graph(filename)

print("input: ")
print_graph(graph)

print("\nsolve: ")
solved_graph = solve(graph)

print("\noutput: ")
print_graph(solved_graph)

# id_grid = ImageReader.last_id_grid
# for r in range(len(id_grid)):
#     print(id_grid[r])
