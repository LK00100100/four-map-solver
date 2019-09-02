# solves the 4-color-map game on Mobaxterm
# python 3.7
# reads the screen for a game and returns a solution image
# author lk00100100
import sys
from Graph import ColorNode
from GraphReader.ImageReader import ImageReader
from GraphReader.ScreenReader import ScreenReader
from GraphSolver.FourMapSolver import FourMapSolver
from GraphWriter.ImagePrinter import ImagePrinter
from Stopwatch import Stopwatch

game_img = ScreenReader.get_game_img_from_screen()

with Stopwatch():
    unsolved_graph = ImageReader.convert_img_to_graph(game_img)

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
output_path = "output/current_screen"
id_grid = ImageReader.last_id_grid
ImagePrinter.save_png_image(output_path, id_grid, solved_graph)
