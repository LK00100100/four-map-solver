from PIL import ImageGrab, Image


class ScreenReader:

    @staticmethod
    def get_logo_coordinate_from_screen():
        """
        finds an instance of the game by finding the game logo
        :return:(x, y) of the upper-left corner of the game
        """
        screen_img = ScreenReader.__get_image_from_screen()

        logo_coordinate = ScreenReader.__get_logo_coordinate(screen_img)

        if logo_coordinate is None:
            error_msg = "cannot find logo. is the game on? is it unobstructed?"
            raise Exception(error_msg)

        return logo_coordinate

    @staticmethod
    def __get_image_from_screen() -> Image:
        """
        detects and returns the Mobxterm 4-map game image from
        the screen
        :return: the game's Image if found. Else None
        """
        return ImageGrab.grab(bbox=None)

    @staticmethod
    def __get_logo_coordinate(screen_img: Image) -> tuple:
        """
        :param screen_img:
        :return: (x, y) of upper-left corner
        None, if not found
        """
        logo_filename = "logo.png"
        logo_img = Image.open(logo_filename)

        screen_width = screen_img.size[0]
        screen_height = screen_img.size[1]
        logo_width = logo_img.size[0]
        logo_height = logo_img.size[1]

        # upper left corner of the logo (if found)
        the_corner = None

        is_match = False
        for screen_y in range(screen_height):
            for screen_x in range(screen_width):
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
                    the_corner = (screen_x, screen_y)
                    break

            if is_match:
                break

        return the_corner


logo_coord = ScreenReader.get_logo_coordinate_from_screen()

print(logo_coord)
