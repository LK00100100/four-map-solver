from PIL import ImageGrab, Image
import pyautogui

from Graph.Color import Color
from Graph.ColorNode import ColorNode


class AutoClicker:
    """
    Assumes that a game instance is on the screen.
    Automatically clicks in a solution
    """

    @staticmethod
    def solve(game_ul: tuple, id_grid: list, solved_graph: dict):
        """
        auto clicks the game for you
        :param game_ul: tuple (x, y) upper left corner
        :param id_grid: 2d grid of id for the shapes
        :param solved_graph: a solved graph <id, color node>
        :return:
        """
        # get color coord relative to screen
        color_coords = {
            Color.BROWN: AutoClicker.get_color_coord(game_ul, id_grid, solved_graph, Color.BROWN),
            Color.GREEN: AutoClicker.get_color_coord(game_ul, id_grid, solved_graph, Color.GREEN),
            Color.RED: AutoClicker.get_color_coord(game_ul, id_grid, solved_graph, Color.RED),
            Color.YELLOW: AutoClicker.get_color_coord(game_ul, id_grid, solved_graph, Color.YELLOW)
        }

        screen_img = ImageGrab.grab()

        # color each unsolved node
        for node_id, current_solved_node in solved_graph.items():
            current_coord = AutoClicker.find_id_coord(game_ul, id_grid, node_id)
            current_pixel = screen_img.getpixel((current_coord[0], current_coord[1]))[0:3]
            unsolved_graph_color = Color.convert_rgb_tuple_to_color(current_pixel)

            if unsolved_graph_color != Color.NONE:
                continue

            solved_color = current_solved_node.color
            solved_color_coord = color_coords[solved_color]

            diff_x = current_coord[0] - solved_color_coord[0]
            diff_y = current_coord[1] - solved_color_coord[1]

            # move the color
            pyautogui.moveTo(solved_color_coord[0], solved_color_coord[1])
            pyautogui.dragRel(diff_x, diff_y)

    @staticmethod
    def get_color_coord(game_ul: tuple, id_grid: list, solved_graph: dict,
                        target_color: Color) -> tuple:
        """
        returns some pixel coordinate that has the target Color
        relative to screen
        :param game_ul: game's upper-left screen coordinates
        :param id_grid: 2d array of ids of nodes
        :param solved_graph: dict <id, ColorNode>
        :param target_color: The Color  you want
        :return: tuple (x, y) relative to screen
        """
        screen_img = ImageGrab.grab()

        # find a node with the target color
        for node_id, color_node in solved_graph.items():
            if color_node.color == target_color:
                id_with_color = node_id
                id_coord = AutoClicker.find_id_coord(game_ul, id_grid, id_with_color)
                current_pixel = screen_img.getpixel((id_coord[0], id_coord[1]))[0:3]
                current_color = Color.convert_rgb_tuple_to_color(current_pixel)

                if current_color == target_color:
                    return id_coord

        return None

    @staticmethod
    def find_id_coord(game_ul: tuple, id_grid: list, target_id: int) -> tuple:
        """
        returns coord of target_id relative to screen
        :param game_ul: game upper left corner (x, y)
        :param id_grid: 2d array of ids of ColorNode
        :param target_id: -
        :return: (x, y) relative to screen
        """
        for r in range(len(id_grid)):
            for c in range(len(id_grid[0])):
                if id_grid[r][c] == target_id:
                    # TODO +1 for hack fix. off by one. probably image reader
                    return game_ul[0] + c + 1, game_ul[1] + r + 1

        return None
