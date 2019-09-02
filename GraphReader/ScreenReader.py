from PIL import ImageGrab, Image


# TODO work in progress


class ScreenReader:

    @staticmethod
    def get_game_img_from_screen() -> Image:

        logo_file_name = 'game_imgs/logo.png'
        logo_coord = ScreenReader.get_sub_img_coordinate_on_screen(logo_file_name)

        if logo_coord is None:
            return None

        coord_ul = ScreenReader.get_sub_img_coordinate_on_screen('game_imgs/corner-ul.png', logo_coord)
        if coord_ul is None:
            return None

        coord_lr = ScreenReader.get_sub_img_coordinate_on_screen('game_imgs/corner-lr.png', logo_coord)
        if coord_lr is None:
            return None

        print(True)

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
        the_corner = None

        is_match = False
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
                    the_corner = (screen_x, screen_y)
                    break

            if is_match:
                break

        return the_corner


ScreenReader.get_game_img_from_screen()

