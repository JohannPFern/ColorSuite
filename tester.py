import color
import themes
Color = color.Color
Scheme = color.Scheme



def _test_bench():
    """
    Dedicating testing function to avoid shadowing variables
    """
    in_hue = 250/360

    palette = Scheme.from_hue(in_hue)

    suggestion = palette.suggest_color()
    print(suggestion.get_hex())

    palette.add_color(suggestion)

    print(palette.get_hex())



def _color_checker():
    in_color = "#00FF00"

    base = Color.from_hex(in_color)
    #scheme = base.gen_analog_scheme()

    # print(comp.get_hex())
    print(base)


if __name__ == "__main__":
    #_test_bench()
    _color_checker()
