import colorsys
import random


class Color:
    """
    Saves HLS values of a color, and can generate other Color objects & representations
    HLS values generated and saved as floats in [0,1]
    H natively [0,360], LS natively [0,100]
    """

    def __init__(self, h, i, s):
        """
        :param r,g,b: int in [0,255]
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

        h, i, s = Color.hex_to_hls(hex_code)
        return cls(h, i, s)

    @staticmethod
    def hex_to_hls(hex_code):
        """
        helper function to prep input to constructor
        This could be moved into from_hex? Leaving it encapsulated for now incase there's another use case?

        :param hex_code: color hex, with or without leading # ex: "123456" or "#123456"
        :return: ex: 210, 20, 65
        """
        hex_code = hex_code.lstrip("#")
        r = int(hex_code[:2], 16) / 255
        g = int(hex_code[2:4], 16) / 255
        b = int(hex_code[4:], 16) / 255
        h, i, s = colorsys.rgb_to_hls(r, g, b)
        return h, i, s

    def get_reg_scheme(self, n):
        """
        Produce a scheme of n colors, including the base, which are evenly distributed around the hue wheel
        The points form a regular shape (or line) hence the name

        Saturation and Luminosity are IRRELEVANT to this process

        :param n: number of colors in scheme
        :return: list of colors
        """
        colors = []
        new_hue = self._hue
        for i in range(n - 1):
            new_hue += 1 / n
            if new_hue > 1:
                new_hue -= 1
            colors.append(Color(new_hue, self._lightness, self._saturation))
        return colors

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        return self.get_reg_scheme(2)[0]

    def get_analog_scheme(self, degree=30):
        """
        Get colors flanking self, at a specified number of degrees of hue change, with same S & L
        ... default semi-arbitrarily chosen, it looks ok but maybe should be modified?

        :param degree: angular distance between base and analogs
        :return: a list of 2 colors
        """
        colors = []
        shift = degree / 360
        hue_up = self._hue + shift
        if hue_up > 1:
            hue_up -= 1
        colors.append(Color(hue_up, self._lightness, self._saturation))
        hue_down = self._hue - shift
        if hue_down < 0:
            hue_up += 1
        colors.append(Color(hue_down, self._lightness, self._saturation))
        return colors

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
        return f"{round(self._hue*360)}|{round(self._lightness*100)}|{round(self._saturation*100)}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


if __name__ == "__main__":
    # Test Block
    in_color = "#123456"

    base = Color.from_hex(in_color)
    scheme = base.get_analog_scheme(15)

    print(*base.get_rgb(), sep="")
    for color in scheme:
        print(color.get_hex())
