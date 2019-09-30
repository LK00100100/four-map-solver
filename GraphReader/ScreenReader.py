import win32gui
from PIL import ImageGrab, Image


class ScreenReader:
    """
    note: handle is the 'window id' or 'process id'
    """
    GAME_APPLICATION_TITLE = "Map"

    # the value which was set previously
    last_game_ul = None  # game upper left
    last_game_lr = None  # game lower right

    @staticmethod
    def get_game_img_from_screen() -> Image:
        """
        Gets the screen and
        returns an Image of the inner game area
        The game should be open and fully visible.
        :return: PIL Image of the inner game area. None if nothing found.
        """
        handle = ScreenReader.detect_game_window()
        print("handle:", handle)

        ScreenReader.move_to_origin(handle)

        # +8 for the invisible windows border
        outer_upper_left_game_coord = (8, 8)

        left_mid_y = ScreenReader.__get_game_screen_left_outer_border_tuple(outer_upper_left_game_coord)

        if left_mid_y is None:
            print("cant find left border of game")
            return None

        game_ul = ScreenReader.__get_upper_left_inner_game_pixel(left_mid_y)
        game_br = ScreenReader.__get_bottom_right_inner_game_pixel(left_mid_y)

        ScreenReader.last_game_ul = game_ul
        ScreenReader.last_game_lr = game_br

        # calculate inner game corners
        left_x = game_ul[0]
        top_y = game_ul[1]
        right_x = game_br[0]
        bottom_y = game_br[1]

        bounding_box = (left_x, top_y, right_x, bottom_y)
        return ImageGrab.grab(bounding_box)

    @staticmethod
    def detect_game_window():
        """
        returns
        :return: returns the handle (process id)
        """
        handle = win32gui.FindWindow(None, ScreenReader.GAME_APPLICATION_TITLE)
        if handle == 0:
            raise ProcessLookupError("Game not found")

        return handle

    @staticmethod
    def move_to_origin(handle: int):
        """
        moves the game window to 0, 0
        :param handle: process id
        :return:
        """
        win32gui.SetForegroundWindow(handle)

        rect = ScreenReader.get_game_rect(handle)
        x = rect[0]
        y = rect[1]
        width = rect[2] - x
        height = rect[3] - y

        # x, y, width, height, repaint
        win32gui.MoveWindow(handle, 0, 0, width, height, True)

    @staticmethod
    def get_game_rect(handle: int):
        """
        returns game window measurements (see below)
        :param handle: process id
        :return:
        x = rect[0]
        y = rect[1]
        width = rect[2] - x
        height = rect[3] - y
        """
        rect = win32gui.GetWindowRect(handle)
        return rect

    @staticmethod
    def __get_image_from_screen() -> Image:
        """
        detects and returns the Mobxterm 4-map game image from
        the screen
        :return: the game's Image if found. Else None
        """
        return ImageGrab.grab(bbox=None)

    @staticmethod
    def __get_game_screen_left_outer_border_tuple(outer_ul_coord: tuple) -> tuple:
        """
        gets the tuple coordinate of the outer left border of the game screen
        :param: outer_ul_coord: (x, y) outer upper left coordinate of the game
        :return: (x, y) tuple coordinate or None as default. y is the mid point of the game
        """
        x = outer_ul_coord[0]
        y = outer_ul_coord[1]

        handle = ScreenReader.detect_game_window()
        rect = ScreenReader.get_game_rect(handle)
        if rect is None:
            return None

        height = rect[3] - y
        mid = int((y + height) / 2)

        return x, mid

    @staticmethod
    def __get_upper_left_inner_game_pixel(left_mid_y: tuple) -> tuple:
        """
        returns the the upper-left coordinates of the actual inner game
        area (just inside the black border)
        :param left_mid_y: the starting location for searching
        (game outer left border, mid_y of game)
        :return: tuple (x, y)
        """
        screen_img = ScreenReader.__get_image_from_screen()

        start_x = left_mid_y[0]
        start_y = left_mid_y[1]

        screen_img_length = screen_img.size[0]

        black_pixel = (0, 0, 0)

        black_border_x = None

        # go right until you hit the black border
        for x in range(start_x, screen_img_length):
            screen_pixel = screen_img.getpixel((x, start_y))[0:3]
            if screen_pixel == black_pixel:
                black_border_x = x
                break

        if black_border_x is None:
            print("reeeEEE")
            return None

        # go up until you get out of the border
        for y in range(start_y, 0, -1):
            screen_pixel = screen_img.getpixel((black_border_x, y))[0:3]
            if screen_pixel != black_pixel:
                return black_border_x + 1, y + 2

        if black_border_x is None:
            print("reeeEEE")
            return None

        return None

    @staticmethod
    def __get_bottom_right_inner_game_pixel(left_mid_y: tuple) -> tuple:
        """
        returns the the bottom-right coordinates of the actual inner game
        area (just inside the black border)
        :param left_mid_y: the starting location for searching
        (game outer left border, mid_y of game)
        :return: tuple (x, y)
        """
        screen_img = ScreenReader.__get_image_from_screen()

        screen_img_length = screen_img.size[0]
        screen_img_height = screen_img.size[1]

        start_x = left_mid_y[0]
        start_y = left_mid_y[1]

        black_pixel = (0, 0, 0)

        black_border_left_x = None
        black_border_bottom_y = None

        # go right until you hit the black border
        for x in range(start_x, screen_img_height):
            screen_pixel = screen_img.getpixel((x, start_y))[0:3]
            if screen_pixel == black_pixel:
                black_border_left_x = x
                break

        if black_border_left_x is None:
            print("reeeEEE")
            return None

        # go down until you get out of the black border
        for y in range(start_y, screen_img_height):
            screen_pixel = screen_img.getpixel((black_border_left_x, y))[0:3]
            if screen_pixel != black_pixel:
                black_border_bottom_y = y - 1
                break

        if black_border_bottom_y is None:
            print("reeeEEE")
            return None

        # go right until you get out of the border
        for x in range(black_border_left_x, screen_img_length):
            screen_pixel = screen_img.getpixel((x, black_border_bottom_y))[0:3]
            if screen_pixel != black_pixel:
                return x - 2, black_border_bottom_y - 1

        if black_border_bottom_y is None:
            print("reeeEEE")
            return None

        return None
