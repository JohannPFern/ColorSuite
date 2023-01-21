import colorsys
import random


class Color:
    """
    Saves HLS values of a color, and can generate other Color objects & representations
    HLS values generated and saved as floats in [0,1]
    H natively [0,360], LS natively [0,100]

    Colors might be immutable, "changes" generate new Colors which are returned?
    """

    def __init__(self, h, i, s):
        """
        :param h,i,s: float in [0,1]
        """
        self.hue = h
        self.lightness = i
        self.saturation = s

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

    def gen_reg_scheme(self, n):
        """
        Produce a scheme of n colors, including the base, which are evenly distributed around the hue wheel
        The points form a regular shape (or line) hence the name

        Saturation and Luminosity are IRRELEVANT to this process

        :param n: number of colors in scheme
        :return: list of colors
        """
        colors = [self]
        new_hue = self.hue
        hue_shift = 1 / n
        for i in range(n - 1):
            new_hue += hue_shift
            if new_hue > 1:
                new_hue -= 1
            colors.append(Color(new_hue, self.lightness, self.saturation))
        new_scheme = Scheme(colors)
        return new_scheme

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        new_hue = self.hue + 0.5 if self.hue < 0.5 else self.hue - 0.5
        return Color(new_hue, self.lightness, self.saturation)

    def gen_analog_scheme(self, degree=30):
        """
        Get colors flanking self, at a specified number of degrees of hue change, with same S & L
        ... default semi-arbitrarily chosen, it looks ok but maybe should be modified?

        :param degree: angular distance between base and analogs
        :return: a list of 2 colors
        """
        colors = [self]
        shift = degree / 360
        hue_up = self.hue + shift
        if hue_up > 1:
            hue_up -= 1
        colors.append(Color(hue_up, self.lightness, self.saturation))
        hue_down = self.hue - shift
        if hue_down < 0:
            hue_up += 1
        colors.append(Color(hue_down, self.lightness, self.saturation))
        new_scheme = Scheme(colors)
        return new_scheme

    def get_accent(self):
        """
        Obviously the implementation is not final
        This placeholder shows how generators will be implemented to produce colors in particular patterns

        :yield: a new Color which might be a decent accent
        """
        comp = self.get_complement()
        while 1:
            yield comp

    def get_rgb(self):
        """
        :return: tuple of r,g,b values in decimal [0,255]
        """
        r, g, b = colorsys.hls_to_rgb(self.hue, self.lightness, self.saturation)
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
        return (
            f"{round(self.hue * 360)}|{round(self.lightness * 100)}|{round(self.saturation * 100)}"
        )

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


class Scheme:
    """
    A collection of Colors
    """

    def __init__(self, initial_colors: list[Color]):
        """
        NON-FINAL IMPLEMENTATION
        Takes a list of Colors, the first is assumed to be the central color

        :param initial_colors: non-empty list of colors beginning with the primary color
        """
        self.colors = initial_colors
        self._base_saturation = initial_colors[0].saturation
        self._base_lightness = initial_colors[0].lightness

    def get_accent(self):
        """
        Obviously the implementation is not final
        This placeholder shows how generators will be implemented to produce relevant colors

        :yield: a new Color which might be a decent accent
        """
        comp = self.colors[0].get_complement()
        while 1:
            yield comp

    def get_rgb(self):
        """
        :return: list of tuples of r,g,b values in decimal [0,255]
        """
        values = []
        for single_color in self.colors:
            values.append(single_color.get_rgb())
        return values

    def get_hex(self):
        """
        :return: list of strings representing each color in hex format (rgb)
        """
        values = []
        for single_color in self.colors:
            values.append(single_color.get_hex())
        return values

    def __str__(self):
        """
        :return: HLS values ('|' separated) for each color ("\n" separated) as a string
        """
        values = ""
        for single_color in self.colors:
            values = f"{values}{single_color}\n"
        return values

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


if __name__ == "__main__":
    # Test Block
    in_color = "#20A39E"

    base = Color.from_hex(in_color)
    scheme = base.gen_analog_scheme()

    print(scheme)
    print(scheme.get_rgb())
    print(scheme.get_hex())
