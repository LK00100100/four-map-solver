from PIL import ImageGrab


class ScreenReader:

    @staticmethod
    def get_image_from_screen():
        """
        detects and returns the Mobxterm 4-map game image from
        the screen
        :return: the game's Image if found. Else None
        """
        screen_img = ImageGrab.grab(bbox=None)

        logo_coordinates = get_logo_coordinate(screen_img)

        if logo_coordinates is None:
            error_msg = "cannot find logo. is the game on? is it unobstructed?"
            raise Exception(error_msg)

        print(screen_img)

    @staticmethod
    def get_logo_coordinate(screen_img) -> tuple:
        """

        :param screen_img:
        :return: (x, y) of upper-left corner
        None, if not found
        """
        logo_filename = "GraphReader/logo.png"



