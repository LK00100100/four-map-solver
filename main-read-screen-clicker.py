# solves the 4-color-map game on Mobaxterm
# python 3.7
# reads the screen for a game and clicks the game to solve it
# author lk00100100
import sys
from Graph import ColorNode
from GraphReader.ImageReader import ImageReader
from GraphReader.ScreenReader import ScreenReader
from GraphSolver.FourMapSolver import FourMapSolver
from GraphWriter.AutoClicker import AutoClicker
from GraphWriter.ImagePrinter import ImagePrinter
from Stopwatch import Stopwatch

print("\nReading game image from screen: ")
with Stopwatch():
    game_img = ScreenReader.get_game_img_from_screen()

print("\nConverting image to graph: ")
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

# auto solver

# ImagePrinter.save_png_image(output_path, id_grid, solved_graph)
id_grid = ImageReader.last_id_grid
game_ul = ScreenReader.last_game_ul
AutoClicker.solve(game_ul, id_grid, solved_graph)


