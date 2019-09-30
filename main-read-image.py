# solves the 4-color-map game on Mobaxterm
# python 3.7
# reads a still image of the game and returns a solution image
# author lk00100100
import os
import sys
from Graph import ColorNode
from GraphWriter.ImagePrinter import ImagePrinter
from GraphSolver.FourMapSolver import FourMapSolver

# TODO lower case file name

from GraphReader.ImageReader import ImageReader
from Stopwatch import Stopwatch

filename = "map-sample1.png"
input_file_path = 'input_samples/' + filename

with Stopwatch():
    unsolved_graph = ImageReader.convert_img_file_to_graph(input_file_path)

print("\ninput: ")
ColorNode.print_graph(unsolved_graph)

print("\nsolve: ")
with Stopwatch():
    solved_graph = FourMapSolver().solve(unsolved_graph)

if solved_graph is None:
    print("no solution")
    sys.exit(0)

print("\noutput: ")
ColorNode.print_graph(solved_graph)

# output picture
if not os.path.exists("output"):
    os.mkdir("output")
    
output_path = "output/" + filename
id_grid = ImageReader.last_id_grid
ImagePrinter.save_png_image(output_path, id_grid, solved_graph)
print("check output folder")
