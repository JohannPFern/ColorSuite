import color
import themes
Color = color.Color
Scheme = color.Scheme



def _test_bench():
    """
    Dedicating testing function to avoid shadowing variables
    """
    in_hue = 250/360
    base = Color.from_hue(in_hue)

    palette = Scheme([base])

    suggestion = palette.suggest_color()
    print(suggestion.get_hex())

    palette.add_color(suggestion)

    print(palette.get_hex())



def _color_checker():
    in_color = "#A42CD6"

    base = Color.from_hex(in_color)
    scheme = base.gen_analog_scheme()

    # print(comp.get_hex())
    print(scheme)


if __name__ == "__main__":
    _test_bench()
    #_color_checker()
