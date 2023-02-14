import abc
from color import Color, Scheme


class Theme(metaclass=abc.ABC):
    """
    Defines Common Rules for Themes so that they can be used polymorphically
    """

    @abc.abstractmethod
    def suggest_color(self, scheme):
        """
        Suggests an appropriate color for the in colors a scheme, with respect to this theme
        :param scheme: The scheme to get colors (and base saturation and lightness) from
        :return: A Color
        """
        pass

    @abc.abstractmethod
    def check_compliance(self, colors: list[Color]):
        """
        Find how well the given colors fit this theme
        :param colors: list of colors to be examined
        :return: [0,1] higher number, more satisfactory match
        """
        pass
