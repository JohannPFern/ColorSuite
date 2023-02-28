import color
import itertools
import random as rand
import abc


class Theme(metaclass=abc.ABCMeta):
    """
    Defines Common Rules for Themes so that they can be used polymorphically
    """

    @abc.abstractmethod
    def generate_color(self, scheme):
        """
        Suggests an appropriate color for the in colors a scheme, with respect to this theme
        :param scheme: The scheme to get colors (and base saturation and lightness) from
        :return: A Color
        """
        pass

    @abc.abstractmethod
    def check_compliance(self, colors):
        """
        Find how well the given colors fit this theme
        :param colors: list of colors to be examined
        :return: [0,1] higher number, more satisfactory match
        """
        pass

    @abc.abstractmethod
    def on_add(self):
        """
        Remove all conflicting schemes and change Scheme parameters to fit
        :return: none
        """
        pass


class Base(Theme):
    def generate_color(self, scheme):
        core = rand.choice(scheme.get_colors())
        return rand.choice(core.gen_analog_colors())

    def check_compliance(self, colors):
        return 1

    def on_add(self):
        pass


class HighContrast(Theme):
    def generate_color(self, scheme: color.Scheme):
        return rand.choice(scheme.get_colors()).get_complement()

    def check_compliance(self, colors: list[color.Color]):
        min_contrast = 100
        for pair in itertools.combinations(colors):
            hue_diff, light_diff, sat_diff = pair[0].calc_difference(pair)
            contrast = hue_diff * 60 + light_diff * 20 + sat_diff * 20
            min_contrast = contrast if contrast < min_contrast else min_contrast
        return min_contrast

    def on_add(self, scheme: color.Scheme):
        pass


class Pastel(Theme):
    def generate_color(self, scheme):
        core = rand.choice(scheme.get_colors())
        hue = rand.choice(core.gen_analog_colors()).get_hue()
        return scheme.color_from_hue(hue)

    def check_compliance(self, colors):
        return 1

    def on_add(self, scheme: color.Scheme):
        scheme.set_bases(0.9, 0.9)


class Pop(Theme):
    def generate_color(self, scheme):
        core = rand.choice(scheme.get_colors())
        hue = rand.choice(core.gen_analog_colors()).get_hue()
        return scheme.color_from_hue(hue)

    def check_compliance(self, colors):
        return 1

    def on_add(self, scheme: color.Scheme):
        scheme.set_bases(0.5, 0.9)


class Noir(Theme):
    def generate_color(self, scheme):
        core = rand.choice(scheme.get_colors())
        hue = rand.choice(core.gen_analog_colors()).get_hue()
        return scheme.color_from_hue(hue)

    def check_compliance(self, colors):
        return 1

    def on_add(self, scheme: color.Scheme):
        scheme.set_bases(0.4, 0.1)


class Cyberpunk(Theme):
    def generate_color(self, scheme):
        core = rand.choice(scheme.get_colors())
        hue = rand.choice(core.gen_analog_colors()).get_hue()
        return scheme.color_from_hue(hue)

    def check_compliance(self, colors):
        return 1

    def on_add(self, scheme: color.Scheme):
        scheme.set_bases(0.2, 0.9)
