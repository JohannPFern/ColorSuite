def new_logistic_modded(self, lightness_shift_factor=0, saturation_shift_factor=0):
    """
    Return a new color with the same hue as self, but with lightness and saturation shifted
    The shifts are smaller as maximum and minimum values are approached

    SUPER SUPER BROKEN DO NOT USE!!!!!!!!!!!!!!!!!!!!

    :param lightness_shift_factor: [-1,1] 0 is no change -1 goes to min light, 1 to max
    :param saturation_shift_factor: [-1,1] 0 is no change -1 goes to completely unsaturated, 1 to max
    :return:
    """
    std_dev = 0.5
    mean = 0.5

    if lightness_shift_factor:
        new_lightness = (
                self._lightness + 1 / math.fabs(self._lightness - 0.5) * lightness_shift_factor
        )
    else:
        new_lightness = self._lightness

    if saturation_shift_factor:
        new_lightness = (
                self._lightness + math.fabs(self._lightness - 0.5) * lightness_shift_factor
        )
    else:
        new_saturation = self._saturation
    return Color(self._hue, new_lightness, new_saturation)