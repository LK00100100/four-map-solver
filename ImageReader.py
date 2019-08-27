from PIL import Image


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
    def get_image_pixel_grid(filepath: str):
        """
        converts an image into a 2d grid of RGBA tuples
        :param filepath: -
        :return: a 2d grid of tuples (Red, Green, Blue, Alpha)
        """
        im = Image.open(filepath)

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

    def get_color_node_graph(self, grid: list):
        """
        converts a 2d array of tuple (RGBA)
        into a dict/graph of ColorNode
        :param grid: 2d array of (R, G, B, A)
        :return: dict/graph of ColorNode
        """
        id_grid = self.convert_pixel_grid_to_id_grid(grid)
        graph = self.convert_id_grid_to_graph(id_grid)

        return graph

    def convert_pixel_grid_to_id_grid(self, grid: list):
        """
        convert a pixel-grid to an id-grid
        :param grid: the 2d grid of tuple (R, G, B, A)
        :return: None
        """

        current_id = 1

        id_grid = self.init_id_grid(grid)

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

    def convert_id_grid_to_graph(self, id_grid: list):
        """
        converts an id_grid to a graph of ColorNode
        :param id_grid:
        :return:
        """

        graph = id_grid

        return graph


image_name = 'samples/map-sample1.png'

img_reader = ImageReader()
pixel_grid = img_reader.get_image_pixel_grid(image_name)

graph = img_reader.get_color_node_graph(pixel_grid)
