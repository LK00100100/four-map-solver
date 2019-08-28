# solves the 4-color-map game on Mobaxterm
# python 3.7
# author lk00100100
from GraphPrinter.ImagePrinter import ImagePrinter
from GraphSolver.FourMapSolver import FourMapSolver
from datetime import datetime

from GraphReader.ImageReader import ImageReader


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
# filename = 'input_samples/graph1.txt'
# graph = GraphReader.read_graph(filename)

filename = "map-sample2.png"
input_file_path = 'input_samples/' + filename

print("\nstart:", datetime.now())

graph = ImageReader.convert_to_graph(input_file_path)
print("end  :", datetime.now())

print("\ninput: ")
print_graph(graph)

print("\nsolve: ")
solved_graph = solve(graph)

print("\noutput: ")
print_graph(solved_graph)

# output picture
output_path = "output/" + filename
id_grid = ImageReader.last_id_grid
ImagePrinter.save_png_image(output_path, id_grid, solved_graph)
