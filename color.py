import colorsys
import random


class Color:
    """
    Create by passing in r,g,b values in [0,255]
    RGB values (int rounded) in [0,255] This might change eventually if more math is done in [0,1] space?
    Rounding to prevent float .000001 and .99999 error propagation, and ensure consistency

    HLS values generated and saved as floats in [0,1]
    """

    def __init__(self, r, g, b):
        """
        :param r,g,b: int in [0,255]
        """
        self._red = round(r)
        self._green = round(g)
        self._blue = round(b)
        self._hue, self._luminosity, self._saturation = colorsys.rgb_to_hls(r, g, b)

    @staticmethod
    def hex_to_rgb(hex_code):
        """
        helper function to prep input to constructor

        :param hex_code: ex: "123456"
        :return: ex: 18, 52, 86
        """
        r = int(hex_code[:2], 16)
        g = int(hex_code[2:4], 16)
        b = int(hex_code[4:], 16)
        return r, g, b

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
            r, g, b = colorsys.hls_to_rgb(new_hue, self._luminosity, self._saturation)
            colors.append(Color(r, g, b))
        return colors

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        return self.get_reg_scheme(2)[0]

    def get_accent(self):
        """
        Obviously the implementation is not final
        This placeholder shows how generators will be implemented to produce colors in particular patterns

        :yield: a new Color which might be a decent accent
        """
        comp = self.get_complement()
        while 1:
            yield comp

    def __str__(self):
        """Uncomment desired print option"""
        # Print HLS
        # return f"{self.hue}{self.luminosity}{self.saturation}"

        # Print HEX
        return f"{hex(self._red)[2:]}{hex(self._green)[2:]}{hex(self._blue)[2:]}"

        # Print RBG
        # return f"{r}|{g}|{b}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


if __name__ == "__main__":
    # Test Block
    in_color = "123456"
    in_red, in_green, in_blue = Color.hex_to_rgb(in_color)

    base = Color(in_red, in_green, in_blue)
    accents = base.get_accent()

    in_color2 = "654321"
    in_red2, in_green2, in_blue2 = Color.hex_to_rgb(in_color2)

    base2 = Color(in_red2, in_green2, in_blue2)
    accents2 = base2.get_accent()

    print(next(accents))
    print(next(accents2))
