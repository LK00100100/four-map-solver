from PIL import ImageGrab, Image


# TODO work in progress


class ScreenReader:

    @staticmethod
    def get_game_img_from_screen() -> Image:

        logo_file_name = 'game_imgs/logo.png'
        logo_coord = ScreenReader.get_sub_img_coordinate_on_screen(logo_file_name)

        if logo_coord is None:
            print("can't find game logo")
            return None

        coord_screen_left = ScreenReader.__get__game_screen_left_pixel(logo_coord)

        if coord_screen_left is None:
            print("cant find left border of game")
            return None

        coord_screen_right = ScreenReader.__get__game_screen_right_pixel(logo_coord)

        if coord_screen_right is None:
            print("cant find right border of game")
            return None

        coord_screen_bottom = ScreenReader.__get__game_screen_bottom_pixel(logo_coord)

        if coord_screen_bottom is None:
            print("cant find bottom border of game")
            return None

    @staticmethod
    def __get_image_from_screen() -> Image:
        """
        detects and returns the Mobxterm 4-map game image from
        the screen
        :return: the game's Image if found. Else None
        """
        return ImageGrab.grab(bbox=None)

    @staticmethod
    def get_sub_img_coordinate_on_screen(file_name: str, start_coord: tuple = (0, 0)) -> tuple:
        """
        attempts to find a sub_image on the screen
        :param file_name: of sub_image
        :param start_coord: (x, y) scan everything below and to the right of this
        :return: (x, y) of upper-left corner
        None, if not found
        """
        screen_img = ScreenReader.__get_image_from_screen()

        logo_img = Image.open(file_name)

        screen_width = screen_img.size[0]
        screen_height = screen_img.size[1]
        logo_width = logo_img.size[0]
        logo_height = logo_img.size[1]

        start_x = start_coord[0]
        start_y = start_coord[1]

        # upper left corner of the logo (if found)
        for screen_y in range(start_y, screen_height):
            for screen_x in range(start_x, screen_width):
                is_match = True
                for logo_y in range(logo_height):
                    for logo_x in range(logo_width):
                        screen_pixel = screen_img.getpixel((screen_x + logo_x, screen_y + logo_y))
                        logo_pixel = logo_img.getpixel((logo_x, logo_y))
                        # compare (R, G, B)
                        if screen_pixel[0:3] != logo_pixel[0:3]:
                            is_match = False
                            break

                    if not is_match:
                        break

                if is_match:
                    return screen_x, screen_y

        return None

    @staticmethod
    def __get__game_screen_left_pixel(logo_coord: tuple) -> tuple:
        """
        gets the tuple of the left of the game screen
        :param: logo_coord: (x, y)
        :return: tuple coordinate or None as default
        """
        screen_img = ScreenReader.__get_image_from_screen()

        logo_x = logo_coord[0]
        logo_y = logo_coord[1]

        white_pixel = (255, 255, 255)

        white_x = 0
        # go into white zone
        for x in range(logo_x, 0, -1):
            screen_pixel = screen_img.getpixel((x, logo_y))
            if screen_pixel[0:3] == white_pixel:
                white_x = x
                break

        # go into the non white-zone (the end)
        for x in range(white_x, 0, -1):
            screen_pixel = screen_img.getpixel((x, logo_y))
            if screen_pixel[0:3] != white_pixel:
                return x, logo_y

        return None

    @staticmethod
    def __get__game_screen_right_pixel(logo_coord: tuple) -> tuple:
        """
        gets the tuple of the right of the game screen
        :param: logo_coord: (x, y)
        :return: tuple coordinate or None as default
        """
        screen_img = ScreenReader.__get_image_from_screen()

        screen_width = screen_img.size[0]

        logo_x = logo_coord[0]
        logo_y = logo_coord[1]

        start_y = logo_y - 3 if logo_y - 3 >= 0 else 0

        white_pixel = (255, 255, 255)

        # go into the non white-zone (the end)
        for x in range(logo_x, screen_width):
            screen_pixel = screen_img.getpixel((x, start_y))
            if screen_pixel[0:3] != white_pixel:
                return x, logo_y

        return None

    @staticmethod
    def __get__game_screen_bottom_pixel(logo_coord: tuple) -> tuple:
        """
        gets the tuple of the bottom of the game screen
        :param: logo_coord: (x, y)
        :return: tuple coordinate or None as default
        """
        screen_img = ScreenReader.__get_image_from_screen()

        screen_height = screen_img.size[1]

        tool_bar_height = 45

        logo_x = logo_coord[0]
        logo_y = logo_coord[1]

        start_x = logo_x - 5 if logo_x - 5 >= 0 else 0

        white_pixel = (255, 255, 255)
        grey_pixel = (240, 240, 240)
        grey2_pixel = (242, 242, 242)

        # go into the non white-zone, non-grey (the end)
        for y in range(logo_y, screen_height - tool_bar_height):
            screen_pixel = screen_img.getpixel((start_x, y))[0:3]

            if screen_pixel != white_pixel and screen_pixel != grey_pixel and screen_pixel != grey2_pixel:
                return logo_x, y

        return None


ScreenReader.get_game_img_from_screen()
