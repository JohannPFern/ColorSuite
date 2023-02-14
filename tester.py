from color import Color, Scheme


def _test_bench():
    """
    Dedicating testing function to avoid shadowing variables
    """
    in_hue = 250/360
    base = Color.from_hue(in_hue)

    lighter = base.new_linear_modded(lightness_shift_factor=.2)
    darker = base.new_linear_modded(lightness_shift_factor=-.2)

    print(lighter.get_rgb())


def _color_checker():
    in_color = "#A42CD6"

    base = Color.from_hex(in_color)
    scheme = base.gen_analog_scheme()

    # print(comp.get_hex())
    print(scheme.get_hex())


if __name__ == "__main__":
    _test_bench()
    _color_checker()
