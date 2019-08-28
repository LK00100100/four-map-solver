from PIL import Image
import numpy as np

from Graph.Color import Color


class ImagePrinter:
    """
    saves an image into the output folder
    """

    @staticmethod
    def save_png_image(file_name: str, id_grid: list, solution_graph: dict):
        """
        Save solution_graph
        :param file_name: the filename
        :param id_grid: 2d array of ids
        :param solution_graph: dict of ColorNode
        :return:
        """
        # convert to np_array
        # it has to be 'uint8' or it'll freak out
        solution_grid = ImagePrinter.__create_image_grid(id_grid, solution_graph)
        solution_grid = np.asarray(solution_grid)
        solution_grid = solution_grid.astype('uint8')

        # save image
        solution_img = Image.fromarray(solution_grid, "RGB")
        solution_img.save(file_name)

    @staticmethod
    def __create_image_grid(id_grid: list, solution_graph: dict) -> list:
        """
        Replaces ids from the id_grid with colors
        :param id_grid: 2d array of ids
        :param solution_graph: dict of ColorNode
        :return:
        """
        solution_grid = []
        for r in range(len(id_grid)):
            row = []
            for c in range(len(id_grid[0])):
                current_id = id_grid[r][c]

                color = Color.BLACK.value
                if current_id != -1:
                    color = solution_graph[current_id].color.value

                row.append(color)

            solution_grid.append(row)

        return solution_grid
