import colorsys
import random


class Color:
    """
    Saves HLS values of a color, and can generate other Color objects & representations
    HLS values generated and saved as floats in [0,1]
    H natively [0,360], LS natively [0,100]

    Colors might be immutable, "changes" generate new Colors which are returned?
    """

    _BLUE_HUE = 235 / 360

    def __init__(self, h, i, s):
        """
        :param h,i,s: float in [0,1]
        """
        self._hue = h
        self._lightness = i
        self._saturation = s

    @classmethod
    def from_hex(cls, hex_code):
        """
        Generate a Color object from a hex code

        :param hex_code: color hex, with or without leading # ex: "123456" or "#123456"
        :return: Color
        """

        hex_code = hex_code.lstrip("#")
        r = int(hex_code[:2], 16) / 255
        g = int(hex_code[2:4], 16) / 255
        b = int(hex_code[4:], 16) / 255
        h, i, s = colorsys.rgb_to_hls(r, g, b)
        return cls(h, i, s)

    @staticmethod
    def hue_addition(hue, shift):
        new_hue = hue + shift
        if new_hue > 1:
            return new_hue - 1
        if new_hue < 0:
            return new_hue + 1
        return new_hue

    def gen_reg_scheme(self, n):
        """
        Produce a scheme of n colors, including the base, which are evenly distributed around the hue wheel
        The points form a regular shape (or line) hence the name

        Saturation and Luminosity are IRRELEVANT to this process

        :param n: number of colors in scheme
        :return: list of colors
        """
        colors = [self]
        new_hue = self._hue
        hue_shift = 1 / n
        for i in range(n - 1):
            new_hue = Color.hue_addition(new_hue, hue_shift)
            colors.append(Color(new_hue, self._lightness, self._saturation))
        new_scheme = Scheme(colors)
        return new_scheme

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        new_hue = self._hue + 0.5 if self._hue < 0.5 else self._hue - 0.5
        return Color(new_hue, self._lightness, self._saturation)

    def gen_analog_scheme(self, degree=30):
        """
        Get colors flanking self, at a specified number of degrees of hue change, with same S & L
        ... default semi-arbitrarily chosen, it looks ok but maybe should be modified?

        :param degree: angular distance between base and analogs
        :return: a list of 2 colors
        """
        colors = [self]
        shift = degree / 360

        new_hue = Color.hue_addition(self._hue, shift)
        colors.append(Color(new_hue, self._lightness, self._saturation))

        new_hue = Color.hue_addition(self._hue, -shift)
        colors.append(Color(new_hue, self._lightness, self._saturation))

        new_scheme = Scheme(colors)
        return new_scheme

    def get_hue(self):
        return self._hue

    def get_lightness(self):
        return self._lightness

    def get_saturation(self):
        return self._saturation

    def get_rgb(self):
        """
        :return: tuple of r,g,b values in decimal [0,255]
        """
        r, g, b = colorsys.hls_to_rgb(self._hue, self._lightness, self._saturation)
        r = round(r * 255)
        g = round(g * 255)
        b = round(b * 255)
        return r, g, b

    def get_hex(self):
        """
        :return: string representing color in hex format (rgb)
        """
        r, g, b = self.get_rgb()
        # Convert to HEX, remove 0x, and if necessary add leading 0
        r = hex(r)[2:].zfill(2)
        g = hex(g)[2:].zfill(2)
        b = hex(b)[2:].zfill(2)
        return f"#{r}{g}{b}"

    def __str__(self):
        """
        :return: HLS values '|' separated as a string
        """
        return f"{round(self._hue * 360)}|{round(self._lightness * 100)}|{round(self._saturation * 100)}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


class Scheme:
    """
    A collection of Colors

    Schemes are mutable: colors can be added and removed
    """

    def __init__(self, initial_colors: list[Color]):
        """
        NON-FINAL IMPLEMENTATION
        Takes a list of Colors, the first is assumed to be the central color

        :param initial_colors: non-empty list of colors beginning with the base color
        """
        self._base_colors = initial_colors
        self._base_saturation = initial_colors[0].get_saturation()
        self._base_lightness = initial_colors[0].get_lightness()

        self._accent_colors = []

    def suggest_accent(self):
        """
        Obviously the implementation is not final
        This placeholder shows how generators will be implemented to produce relevant colors

        :yield: a new Color which might be a decent accent
        """
        # add check that it's not repeated

        comp = self._base_colors[0].get_complement()
        while 1:
            yield comp

    def add_accent(self, new_accent):
        # add check that it's not repeated
        self._accent_colors.append(new_accent)

    def get_rgb(self):
        """
        :return: list of tuples of r,g,b values in decimal [0,255]
        """
        values = []
        for single_color in self._base_colors:
            values.append(single_color.get_rgb())
        return values

    def get_hex(self):
        """
        :return: list of strings representing each color in hex format (rgb)
        """
        values = []
        for single_color in self._base_colors:
            values.append(single_color.get_hex())
        return values

    def __str__(self):
        """
        :return: HLS values ('|' separated) for each color ("\n" separated) as a string
        """
        values = ""
        for single_color in self._base_colors:
            values = f"{values}{single_color}\n"
        return values

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


def _test_bench():
    """
    Dedicating testing function to avoid shadowing variables
    """
    in_color = "#A6B1E1"

    base = Color.from_hex(in_color)
    comp = base.get_complement()
    scheme = base.gen_analog_scheme()

    # print(comp.get_hex())
    print(*scheme.get_hex())


def _color_checker():
    in_color = "#2B2D42"

    base = Color.from_hex(in_color)

    print(base)


if __name__ == "__main__":
    _test_bench()
    # _color_checker()
