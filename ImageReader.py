from PIL import Image

from Color import ColorRGB
from GraphReader import GraphReader


class ImageReader:
    """
    reads an image from MobaXterm's 4-color map game
    """
    # TODO probably change this later for the whole screen
    # this is the first color pixel in the game zone
    # upper-left pixel (x, y)
    start_pixel = (22, 72)

    # bottom-right pixel (x, y)
    end_pixel = (420, 370)

    @staticmethod
    def convert_to_graph(file_name: str):
        pixel_grid = ImageReader.get_image_pixel_grid(file_name)
        return ImageReader.get_color_node_graph(pixel_grid)

    @staticmethod
    def get_image_pixel_grid(file_path: str):
        """
        converts an image into a 2d grid of RGBA tuples
        :param file_path: -
        :return: a 2d grid of tuples (Red, Green, Blue, Alpha)
        """
        im = Image.open(file_path)

        print(im.format)
        print(im.size)
        print(im.mode)

        rgb_im = im.convert('RGB')
        r, g, b = rgb_im.getpixel((10, 10))
        print(r, g, b)

        game_length = ImageReader.end_pixel[0] - ImageReader.start_pixel[0] + 1
        game_height = ImageReader.end_pixel[1] - ImageReader.start_pixel[1] + 1

        # get image into grid
        grid = []
        for x in range(0, game_length):
            row = []
            for y in range(0, game_height):
                pixel = im.getpixel((ImageReader.start_pixel[0] + x, ImageReader.start_pixel[1] + y))
                row.append(pixel)

            grid.append(row)

        return grid

    @staticmethod
    def get_color_node_graph(grid: list):
        """
        converts a 2d array of tuple (RGBA)
        into a dict/graph of ColorNode
        :param grid: 2d array of (R, G, B, A)
        :return: dict/graph of ColorNode
        """
        id_grid = ImageReader.convert_pixel_grid_to_id_grid(grid)
        nodes = ImageReader.convert_id_grid_to_graph(grid, id_grid)

        return nodes

    @staticmethod
    def convert_pixel_grid_to_id_grid(grid: list):
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

        return id_grid

    @staticmethod
    def init_id_grid(px_grid: list):
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
                if pixel == (0, 0, 0, 255):
                    val = -1

                row.append(val)

            id_grid.append(row)

        return id_grid

    @staticmethod
    def convert_id_grid_to_graph(grid: list, id_grid: list):
        """
        converts a grid and id_grid to a graph of ColorNode
        :param grid: 2d array of tuple of ints (r,g,b,a)
        :param id_grid: 2d array of ids
        :return: dict of ColorNode
        """
        max_id = ImageReader.get_max_id(id_grid)

        nodes = GraphReader.init_map(max_id)
        # todo: slow. add dict
        # assign color
        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                current_id = id_grid[row][col]

                if current_id == -1:
                    continue

                current_color_tuple = grid[row][col]
                current_color = ColorRGB.convert_rgb_tuple_to_color(current_color_tuple)

                nodes[current_id].color = current_color

        # get neighbors
        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                current_id = id_grid[row][col]

                if current_id == -1:
                    continue

                # get the down neighbor
                for r in range(row, len(id_grid)):
                    # we hit a black border
                    if id_grid[r][col] == -1:
                        if r + 1 >= len(id_grid):
                            continue

                        neighbor_id = id_grid[r + 1][col]

                        if neighbor_id == -1:
                            continue

                        GraphReader.link_nodes(nodes, current_id, neighbor_id)
                        continue

                # get the right neighbor
                for c in range(col, len(id_grid[0])):
                    # we hit a black border
                    if id_grid[row][c] == -1:
                        if c + 1 >= len(id_grid[0]):
                            continue

                        neighbor_id = id_grid[row][c + 1]

                        if neighbor_id == -1:
                            continue

                        GraphReader.link_nodes(nodes, current_id, neighbor_id)
                        continue

        return nodes

    @staticmethod
    def get_max_id(id_grid: list):
        max_id = -1

        for row in range(len(id_grid)):
            for col in range(len(id_grid[0])):
                x = id_grid[row][col]
                if x > max_id:
                    max_id = x

        return max_id

# image_name = 'samples/map-sample1.png'
# img_reader = ImageReader()
# nodes = img_reader.convert_to_graph(image_name)
