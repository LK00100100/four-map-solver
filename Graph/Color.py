from enum import Enum


class Color(Enum):
    # R, G, B, Alpha
    NONE = (240, 240, 240)
    BROWN = (140, 114, 89)
    GREEN = (127, 153, 102)
    RED = (178, 127, 102)
    YELLOW = (204, 178, 102)
    BLACK = (0, 0, 0)

    @staticmethod
    def convert_rgb_tuple_to_color(val: tuple):
        # ignore alpha value (4th value)
        for color in Color:
            if val[0:3] == color.value[0:3]:
                return color
