import colorsys
import random as rand
import math


class Color:
    """
    Saves HLS values of a color, and can generate other Color objects & representations
    HLS values generated and saved as floats in [0,1]
    H natively [0,360], LS natively [0,100]
    """

    _BLUE_HUE = 235 / 360
    _STD_LIGHTNESS = 0.5
    _STD_SATURATION = 0.5

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

    @classmethod
    def from_hue(cls, hue):
        """
        Generate a color at std
        :param hue: hue in [0,1]
        :return: Color with hue at standard saturation and lightness
        """
        return Color(hue, cls._STD_LIGHTNESS, cls._STD_SATURATION)

    def new_linear_modded(self, lightness_shift_factor=0, saturation_shift_factor=0):
        """
        Return a new color with the same hue as self, but with lightness and saturation shifted

        :param lightness_shift_factor: [-1,1]
        :param saturation_shift_factor: [-1,1]
        :return: Color
        """
        new_lightness = self._lightness + lightness_shift_factor
        new_saturation = self._saturation + saturation_shift_factor
        if new_lightness > 1:
            new_lightness = 1
        elif new_lightness < 0:
            new_lightness = 0
        if new_saturation > 1:
            new_saturation = 1
        elif new_saturation < 0:
            new_saturation = 0
        return Color(self._hue, new_lightness, new_saturation)

    @staticmethod
    def hue_addition(hue, shift):
        new_hue = hue + shift
        if new_hue > 1:
            return new_hue - 1
        if new_hue < 0:
            return new_hue + 1
        return new_hue

    def gen_reg_colors(self, n):
        """
        Produce a scheme of n colors, including the base, which are evenly distributed around the hue wheel
        The points form a regular shape (or line) hence the name

        Saturation and Luminosity are IRRELEVANT to this process

        :param n: number of colors in scheme
        :return: list of colors
        """
        colors = []
        new_hue = self._hue
        hue_shift = 1 / n
        for i in range(n - 1):
            new_hue = Color.hue_addition(new_hue, hue_shift)
            colors.append(Color(new_hue, self._lightness, self._saturation))
        return colors

    def get_complement(self):
        """
        A degenerate case of regular scheme, where only 1 color is returned
        A separate method is called for ease of development as complements will (probably) be frequently used

        :return: the color with equal S & L, and opposite H
        """
        new_hue = self._hue + 0.5 if self._hue < 0.5 else self._hue - 0.5
        return Color(new_hue, self._lightness, self._saturation)

    def gen_analog_colors(self, degree=30):
        """
        Get colors flanking self, at a specified number of degrees of hue change, with same S & L
        ... default semi-arbitrarily chosen, it looks ok but maybe should be modified?

        :param degree: angular distance between base and analogs
        :return: a list of 2 colors
        """
        colors = []
        shift = degree / 360

        new_hue = Color.hue_addition(self._hue, shift)
        colors.append(Color(new_hue, self._lightness, self._saturation))

        new_hue = Color.hue_addition(self._hue, -shift)
        colors.append(Color(new_hue, self._lightness, self._saturation))

        return colors

    def calc_difference(self, other_color: "Color"):
        hue_diff = math.fabs(self._hue - other_color._hue)
        light_diff = math.fabs(self._lightness - other_color._lightness)
        sat_diff = math.fabs(self._saturation - other_color._lightness)
        return hue_diff, light_diff, sat_diff

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

    _BASE_THRESHOLD = 0.7
    _THRESHOLD_SHIFT = 0.01

    def __init__(self, initial_colors: list[Color]):
        from themes import Base

        """
        Takes a list of Colors, the first is assumed to be the central color

        :param initial_colors: non-empty list of colors beginning with the base color
        """
        self._locked_colors = initial_colors
        self._base_saturation = initial_colors[0].get_saturation()
        self._base_lightness = initial_colors[0].get_lightness()

        self._themes = [Base()]

    def set_bases(self, new_lightness, new_saturation):
        self._base_lightness = new_lightness
        self._base_saturation = new_saturation

    @classmethod
    def from_hue(cls, initial_hue):
        core = Color.from_hue(initial_hue)
        return cls([core])

    def color_from_hue(self, hue):
        return Color(hue, self._base_lightness, self._base_lightness)

    def add_color(self, new_accent: Color):
        if new_accent in self._locked_colors:
            return
        self._locked_colors.append(new_accent)

    def remove_color(self, accent: Color):
        self._locked_colors.remove(accent)

    def add_theme(self, new_theme: "Theme"):
        if new_theme in self._themes:
            return
        self._themes.append(new_theme)

    def remove_theme(self, theme: "Theme"):
        self._themes.remove(theme)

    def suggest_color(self):
        """
        Suggest a color based on the colors currently present, which complies to some degree with each theme
        """
        threshold = self._BASE_THRESHOLD
        while 1:
            threshold -= self._THRESHOLD_SHIFT
            active_theme = rand.choice(self._themes)
            suggestion = active_theme.generate_color(self)
            proposition = self._locked_colors.copy().append(suggestion)

            compliances = [theme.check_compliance(proposition) for theme in self._themes]
            if min(compliances) > threshold:
                return suggestion

    def get_colors(self):
        return self._locked_colors

    def get_rgb(self):
        """
        :return: list of tuples of r,g,b values in decimal [0,255]
        """
        values = []
        for single_color in self._locked_colors:
            values.append(single_color.get_rgb())
        return values

    def get_hex(self):
        """
        :return: list of strings representing each color in hex format (rgb)
        """
        values = []
        for single_color in self._locked_colors:
            values.append(single_color.get_hex())
        return values

    def __str__(self):
        """
        :return: HLS values ('|' separated) for each color ("\n" separated) as a string
        """
        strings = [str(single_color) for single_color in self._locked_colors]
        return "\n".join(strings)

    def __repr__(self):
        """So printing lists is easier"""
        return str(self)

    def __len__(self):
        return len(self._locked_colors)
