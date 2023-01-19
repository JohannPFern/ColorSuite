import colorsys
import random


class Color:
    """
    RGB & HLS values generated and saved as floats in [0,1]
    RBG natively int [0,255]
    H natively [0,360], LS natively [0,100]
    """

    def __init__(self, r, g, b):
        """
        :param r,g,b: int in [0,255]
        """
        self._red = r
        self._green = g
        self._blue = b
        self._hue, self._lightness, self._saturation = colorsys.rgb_to_hls(r, g, b)

    @staticmethod
    def hex_to_rgb(hex_code):
        """
        helper function to prep input to constructor

        :param hex_code: ex: "123456"
        :return: ex: 18, 52, 86
        """
        r = int(hex_code[:2], 16) / 255
        g = int(hex_code[2:4], 16) / 255
        b = int(hex_code[4:], 16) / 255
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
            r, g, b = colorsys.hls_to_rgb(new_hue, self._lightness, self._saturation)
            colors.append(Color(r, g, b))
        return colors

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        return self.get_reg_scheme(2)[0]

    def get_analog(self, degree=30):
        """
        Get colors flanking self, at a specified number of degrees of hue change, with same S & L

        :param degree: how far the flanking colors are from self... default semi-arbitrarily chosen
        :return: a list of 2 colors
        """
        colors = []
        shift = degree / 360
        hue_up = self._hue + shift
        if hue_up > 1:
            hue_up -= 1
        r, g, b = colorsys.hls_to_rgb(hue_up, self._lightness, self._saturation)
        colors.append(Color(r, g, b))
        hue_down = self._hue - shift
        if hue_down < 0:
            hue_up += 1
        r, g, b = colorsys.hls_to_rgb(hue_down, self._lightness, self._saturation)
        colors.append(Color(r, g, b))
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

    def __str__(self):
        """Uncomment desired print option"""
        # Print HLS
        # return f"{round(self._hue*360)}|{round(self._lightness*100)}|{round(self._saturation*100)}"

        # Print RBG
        # return f"{round(self._red*255)}|{round(self._green*255)}|{round(self._blue*255)}"

        # Print HEX
        # Convert to HEX, remove 0x, and if necessary add leading 0
        r = hex(round(self._red * 255))[2:].zfill(2)
        g = hex(round(self._green * 255))[2:].zfill(2)
        b = hex(round(self._blue * 255))[2:].zfill(2)
        return f"{r}{g}{b}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


if __name__ == "__main__":
    # Test Block
    in_color = "0a0a00"
    in_red, in_green, in_blue = Color.hex_to_rgb(in_color)

    base = Color(in_red, in_green, in_blue)
    scheme = base.get_analog(15)

    print(base)
    print(*scheme, sep="\n")
