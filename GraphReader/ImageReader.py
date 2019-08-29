from PIL import Image

from Graph import GraphHelper
from Graph.Color import Color


class ImageReader:
    """
    reads an image from MobaXterm's 4-color map game
    """
    # gets the last set grids
    last_id_grid = None
    last_pixel_grid = None

    @staticmethod
    def convert_img_to_graph(img):
        pixel_grid = ImageReader.__get_pixel_grid(img)
        return ImageReader.get_color_node_graph(pixel_grid)

    @staticmethod
    def convert_img_file_to_graph(file_name: str) -> dict:
        pixel_grid = ImageReader.get_img_file_pixel_grid(file_name)
        return ImageReader.get_color_node_graph(pixel_grid)

    @staticmethod
    def get_img_file_pixel_grid(file_path: str) -> list:
        """
        converts an image into a 2d grid of RGBA tuples
        :param file_path: -
        :return: a 2d grid of tuples (Red, Green, Blue, Alpha)
        """
        img = Image.open(file_path)
        print("image format:", img.format)
        print("img size:", img.size)
        print("img mode:", img.mode)

        return ImageReader.__get_pixel_grid(img)

    @staticmethod
    def __get_pixel_grid(img) -> list:
        """
        gets a pixel grid from an image
        :param img:
        :return: 2d grid of pixel tuples (R, G, B, A)
        Each value is [0 - 255] (inclusive)
        """
        # this is the first color pixel in the game zone
        # upper-left pixel (x, y)
        start_pixel = (22, 72)

        # bottom-right pixel (x, y)
        end_pixel = (img.size[0] - 23, img.size[1] - 23)

        game_length = end_pixel[0] - start_pixel[0] + 1
        game_height = end_pixel[1] - start_pixel[1] + 1

        # get image into grid
        grid = []
        for y in range(0, game_height):
            row = []
            for x in range(0, game_length):
                pixel = img.getpixel((start_pixel[0] + x, start_pixel[1] + y))
                row.append(pixel)

            grid.append(row)

        ImageReader.last_pixel_grid = grid
        return grid

    @staticmethod
    def get_color_node_graph(grid: list) -> dict:
        """
        converts a 2d array of tuple (RGBA)
        into a dict/graph of ColorNode
        :param grid: 2d array of (R, G, B, A)
        :return: dict/graph of ColorNode
        """
        id_grid = ImageReader.convert_pixel_grid_to_id_grid(grid)
        the_nodes = ImageReader.convert_id_grid_to_graph(grid, id_grid)

        return the_nodes

    @staticmethod
    def convert_pixel_grid_to_id_grid(grid: list) -> list:
        """
        convert a pixel-grid to an id-grid
        :param grid: the 2d grid of tuple (R, G, B, A)
        :return: None
        """
        current_id = 1

        id_grid = ImageReader.init_id_grid(grid)

        process_queue = []

        for r in range(len(id_grid)):
            for c in range(len(id_grid[0])):
                process_queue.append((r, c))
                just_set_new_id = False

                while len(process_queue) > 0:
                    coord = process_queue.pop()
                    row = coord[0]
                    col = coord[1]

                    # out of bounds
                    if row < 0 or row >= len(id_grid):
                        continue

                    # out of bounds
                    if col < 0 or col >= len(id_grid[0]):
                        continue

                    # assigned an id OR a wall
                    if id_grid[row][col] != 0:
                        continue

                    # spread the current_id everywhere
                    id_grid[row][col] = current_id

                    process_queue.append((row - 1, col))
                    process_queue.append((row + 1, col))
                    process_queue.append((row, col - 1))
                    process_queue.append((row, col + 1))

                    just_set_new_id = True

                if just_set_new_id:
                    current_id = current_id + 1

        ImageReader.last_id_grid = id_grid
        return id_grid

    @staticmethod
    def init_id_grid(px_grid: list) -> list:
        """
        from a pixel_grid
        :param px_grid: 2d array of (R, G, B, A).
        R, G, B, A are values from 0 to 255
        :return: 2d array of ids. -1 is invalid. 0 is empty. >0 = assigned
        """
        # TODO: a bit slow

        id_grid = []

        for r in range(len(px_grid)):
            row = []
            for c in range(len(px_grid[0])):
                pixel = px_grid[r][c]
                val = 0
                if pixel[0:3] == (0, 0, 0):
                    val = -1

                row.append(val)

            id_grid.append(row)

        return id_grid

    @staticmethod
    def convert_id_grid_to_graph(grid: list, id_grid: list) -> dict:
        """
        converts a grid and id_grid to a graph of ColorNode
        :param grid: 2d array of tuple of ints (r,g,b,a)
        :param id_grid: 2d array of ids
        :return: dict of ColorNode
        """
        max_id = ImageReader.get_max_id(id_grid)

        nodes = GraphHelper.init_map(max_id)

        # assign color
        checked_ids = set()
        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                current_id = id_grid[row][col]

                if current_id == -1:
                    continue

                if current_id in checked_ids:
                    continue

                checked_ids.add(current_id)

                current_color_tuple = grid[row][col]
                current_color = Color.convert_rgb_tuple_to_color(current_color_tuple)

                nodes[current_id].color = current_color
        # todo: slow. add dict?
        # get neighbors
        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                current_id = id_grid[row][col]

                if current_id == -1:
                    continue

                # get the down neighbor
                for r in range(row + 1, len(id_grid)):
                    # we hit a black border
                    if id_grid[r][col] == -1:
                        if r + 1 >= len(id_grid):
                            break

                        neighbor_id = id_grid[r + 1][col]

                        if neighbor_id == -1:
                            break

                        if current_id == neighbor_id:
                            break

                        GraphHelper.link_nodes(nodes, current_id, neighbor_id)
                        break

                # get the right neighbor
                for c in range(col + 1, len(id_grid[0])):
                    # we hit a black border
                    if id_grid[row][c] == -1:
                        if c + 1 >= len(id_grid[0]):
                            break

                        neighbor_id = id_grid[row][c + 1]

                        if neighbor_id == -1:
                            break

                        if current_id == neighbor_id:
                            break

                        GraphHelper.link_nodes(nodes, current_id, neighbor_id)
                        break

        return nodes

    @staticmethod
    def get_max_id(id_grid: list) -> int:
        max_id = -1

        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                x = id_grid[row][col]
                if x > max_id:
                    max_id = x

        return max_id
