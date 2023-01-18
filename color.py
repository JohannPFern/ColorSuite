import colorsys


class Color:
    """
    Create by passing in r,g,b values in [0,255]
    rbg values preserved (rounded) in [0,255] This might change eventually if more math is done in [0,1] space?
    Rounding to prevent float .000001 and .99999 error propagation, and ensure consistency

    hls values generated and saved as floats in [0,1]
    """

    def __init__(self, r, g, b):
        """
        :param r,g,b: int in [0,255]
        """
        self.red = round(r)
        self.green = round(g)
        self.blue = round(b)
        self.hue, self.luminosity, self.saturation = colorsys.rgb_to_hls(r, g, b)

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

    # Pass n where n is the total number of colors in the scheme
    def get_reg_scheme(self, n):
        """
        Produce a scheme of n colors, including the base, which are evenly distributed around the hue wheel
        The points form a regular shape (or line) hence the name

        Saturation and Luminosity are IRRELEVANT to this process
        :param n: number of colors in scheme
        :return: list of colors
        """
        colors = []
        new_hue = self.hue
        for i in range(n - 1):
            new_hue += 1 / n
            if new_hue > 1:
                new_hue -= 1
            r, g, b = colorsys.hls_to_rgb(new_hue, self.luminosity, self.saturation)
            colors.append(Color(r, g, b))
        return colors

    def __str__(self):
        """Uncomment desired print option"""
        # Print HLS
        # return f"{self.hue}{self.luminosity}{self.saturation}"

        # Print HEX
        return f"{hex(self.red)[2:]}{hex(self.green)[2:]}{hex(self.blue)[2:]}"

        # Print RBG
        # return f"{r}|{g}|{b}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


# Test Block
in_color = "123456"
in_red, in_green, in_blue = Color.hex_to_rgb(in_color)

base = Color(in_red, in_green, in_blue)
scheme = base.get_reg_scheme(4)
print(*scheme, sep="\n")
