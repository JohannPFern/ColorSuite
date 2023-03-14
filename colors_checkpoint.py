# -*- coding: utf-8 -*-
"""Colors-checkpoint.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10m2uWpIhvYB0y9jthvXOkLA505jZSzk_
"""

import colorsys

"""User runs tintShade once they have a locked pallet that they are happy with. All hexcodes will be passed to backend. Backend returns list of tints and shades of fixed length N. """

def tintShade(initHLS, numColors):
  shift = 0.1
  pallet = [initHLS]
  for x in range(numColors):
    #tint: shift to warm, decrease sat, increase light
    if initHLS[0] >= (25/360) and initHLS[0] <= (205/360):
      newH_t = initHLS[0] * (1 + -(shift*(x+1)*0.9))%1
    else:
      newH_t = initHLS[0] * (1 + (shift*(x+1)*1.1))%1
    newL_t = initHLS[1] * (1.1+ shift*(x))
    newS_t = initHLS[2] * 0.9

    pallet = [(newH_t, newL_t, newS_t)] + pallet

    #shade: shift to cool, decrease sat, decrease light
    if initHLS[0] >= (25/360) and initHLS[0] <= (205/360):
      newH_s = initHLS[0] * (1 + (shift*(x+1)*0.9))%1
    else:
      newH_s = initHLS[0] * (1 + -(shift*(x+1)*1.1))%1
    newL_s = initHLS[1] * (0.9 - shift*(x))
    newS_s = initHLS[2] * 0.9

    pallet = pallet + [(newH_s, newL_s, newS_s)]
  return pallet

def HLStoHex(initHLS):
    rgb = colorsys.hls_to_rgb(initHLS[0],initHLS[1],initHLS[2])
    rgb = [round(y*255) for y in rgb]
    r = str(hex(rgb[0])[2:].zfill(2))
    g = str(hex(rgb[1])[2:].zfill(2))
    b = str(hex(rgb[2])[2:].zfill(2))
    return r+g+b

def schemaProvider(initHLS, schema):
    if(schema=='complimentary'):
        newHue = (initHLS[0]+0.5)%1
        newHLS = (newHue, initHLS[1],initHLS[2])
        return [newHLS]
    elif(schema=='triadic'):
        newHue1 = (initHLS[0]+0.3333)%1
        newHue2 = (initHLS[0]+0.6666)%1
        newHLS1 = (newHue1, initHLS[1],initHLS[2])
        newHLS2 = (newHue2, initHLS[1],initHLS[2])
        return [newHLS1, newHLS2]
    elif(schema=='split_complimentary'):
        newHue1 = (initHLS[0]+0.4167)%1
        newHue2 = (initHLS[0]+0.5833)%1
        newHLS1 = (newHue1, initHLS[1],initHLS[2])
        newHLS2 = (newHue2, initHLS[1],initHLS[2])
        return [newHLS1, newHLS2]

HLStoHex((0.2, 0.3, 0.5))

a = schemaProvider((0.2, 0.3, 0.5), 'complimentary')
HLStoHex(a[0])

b = schemaProvider((0.2, 0.3, 0.5), 'triadic')
print(HLStoHex(b[0]), HLStoHex(b[1]))

c = schemaProvider((0.2, 0.3, 0.5), 'split_complimentary')
print(HLStoHex(c[0]), HLStoHex(c[1]))

tintShade((0.2, 0.3, 0.5), 3)

for x in tintShade((0.2, 0.3, 0.5), 3):
  print(HLStoHex(x))