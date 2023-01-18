import colorsys


class Color:
    """
    Create by passing in r,g,b values in [0,255]
    All values converted to and saved in [0,1]
    """

    def __init__(self, r, g, b):
        self.red = r / 255
        self.green = g / 255
        self.blue = b / 255
        self.hue, self.luminosity, self.saturation = colorsys.rgb_to_hls(r, g, b)

    @staticmethod
    def hex_to_rgb(hex_code):
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

        # Prep rbg methods
        r = int(self.red * 255)
        g = int(self.green * 255)
        b = int(self.blue * 255)

        # Print HEX
        return f"{hex(r)[2:]}{hex(g)[2:]}{hex(b)[2:]}"

        # Print RBG
        # return f"{r}|{g}|{b}"

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)


# Test Block
in_color = "123456"
in_red, in_green, in_blue = Color.hex_to_rgb(in_color)

base = Color(in_red, in_green, in_blue)
scheme = base.get_reg_scheme(3)

print(*scheme, sep="\n")
