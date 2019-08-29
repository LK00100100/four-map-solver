# solves the 4-color-map game on Mobaxterm
# python 3.7
# reads a still image of the game and returns a solution image
# author lk00100100
from Graph import ColorNode
from GraphWriter.ImagePrinter import ImagePrinter
from GraphSolver.FourMapSolver import FourMapSolver
from datetime import datetime

from GraphReader.ImageReader import ImageReader

filename = "map-sample1.png"
input_file_path = 'input_samples/' + filename

print("start:", datetime.now())
unsolved_graph = ImageReader.convert_to_graph(input_file_path)
print("end  :", datetime.now())

print("\ninput: ")
ColorNode.print_graph(unsolved_graph)

print("\nsolve: ")
print("start:", datetime.now())
solved_graph = FourMapSolver().solve(unsolved_graph)
print("end  :", datetime.now())

print("\noutput: ")
ColorNode.print_graph(solved_graph)

# output picture
output_path = "output/" + filename
id_grid = ImageReader.last_id_grid
ImagePrinter.save_png_image(output_path, id_grid, solved_graph)

