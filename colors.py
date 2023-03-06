# -*- coding: utf-8 -*-
"""Colors.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k0f9D0PjtlKC826pFlrQeeyVi9WVdyzh
"""

import colorsys

def hls2hex(initHLS):
    rgb = colorsys.hls_to_rgb(initHLS[0],initHLS[1],initHLS[2])
    rgb = [round(y*255) for y in rgb]
    r = str(hex(rgb[0])[2:].zfill(2))
    g = str(hex(rgb[1])[2:].zfill(2))
    b = str(hex(rgb[2])[2:].zfill(2))
    return r+g+b

def hex2hls(hex_value):
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    hls = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return hls

#helper function used in Schema provider
#takes in HLS and theme, shifts L and S values to match theme
#
#Themes accepted: pastel, pop, noir, cyberpunk
def themeShifter(initHLS, theme):
    if(theme == 'pastel'):
      #desat, light
      newLight = 0.9
      newSat = 0.9
      return (initHLS[0], newLight, newSat)
    elif(theme == 'pop'):
      #sat, light
      newLight = 0.5
      newSat = 0.9
      return (initHLS[0], newLight, newSat)
    elif(theme == 'noir'):
      #desat, dark
      newLight = 0.4
      newSat = 0.1
      return (initHLS[0], newLight, newSat)
    elif(theme=='cyberpunk'):
      #sat, dark
      newLight = 0.2
      newSat = 0.9
      return (initHLS[0], newLight, newSat)

#Main color schema provider
#Takes in inital HLS selection, shema type, theme type. Output list suggested colors for schema.
#Schema accepted: complimentary, triadic, analog, split_complimentary, tetratic 
#
#Themes accepted: none (uses selected sat and lightness), pastel, pop, noir, cyberpunk
def schemaProvider(initHLS, schema, theme):
    if(schema=='complimentary'):
        newHue = (initHLS[0]+0.5)%1
        if(theme=='none'):
          newHLS = (newHue, initHLS[1],initHLS[2])
          return [newHLS]
        else:
          newHLS = themeShifter((newHue, initHLS[1],initHLS[2]), theme)
          return [newHLS]
    elif(schema=='triadic'):
        newHue1 = (initHLS[0]+0.3333)%1
        newHue2 = (initHLS[0]+0.6666)%1
        if(theme=='none'):
          newHLS1 = (newHue1, initHLS[1],initHLS[2])
          newHLS2 = (newHue2, initHLS[1],initHLS[2])
          return [newHLS1, newHLS2]
        else:
          newHLS1 = themeShifter((newHue1, initHLS[1],initHLS[2]), theme)
          newHLS2 = themeShifter((newHue2, initHLS[1],initHLS[2]), theme)
          return [newHLS1, newHLS2]
    elif(schema=='analog'):
        newHue1 = (initHLS[0]+0.125)%1
        newHue2 = (initHLS[0]-0.125)%1
        if(theme=='none'):
          newHLS1 = (newHue1, initHLS[1],initHLS[2])
          newHLS2 = (newHue2, initHLS[1],initHLS[2])
          return [newHLS1, newHLS2]
        else:
          newHLS1 = themeShifter((newHue1, initHLS[1],initHLS[2]), theme)
          newHLS2 = themeShifter((newHue2, initHLS[1],initHLS[2]), theme)
          return [newHLS1, newHLS2]
    elif(schema=='split_complimentary'):
        newHue1 = (initHLS[0]+0.4167)%1
        newHue2 = (initHLS[0]+0.5833)%1
        if(theme=='none'):
          newHLS1 = (newHue1, initHLS[1],initHLS[2])
          newHLS2 = (newHue2, initHLS[1],initHLS[2])
          return [newHLS1, newHLS2]
        else:
          newHLS1 = themeShifter((newHue1, initHLS[1],initHLS[2]), theme)
          newHLS2 = themeShifter((newHue2, initHLS[1],initHLS[2]), theme)
          return [newHLS1, newHLS2]
    elif(schema=='tetratic'):
        newHue1 = (initHLS[0]+0.25)%1
        newHue2 = (initHLS[0]+0.5)%1
        newHue3 = (initHLS[0]+0.75)%1
        if(theme=='none'):
          newHLS1 = (newHue1, initHLS[1],initHLS[2])
          newHLS2 = (newHue2, initHLS[1],initHLS[2])
          newHLS3 = (newHue3, initHLS[1],initHLS[2])
          return [newHLS1, newHLS2, newHLS3]
        else:
          newHLS1 = themeShifter((newHue1, initHLS[1],initHLS[2]), theme)
          newHLS2 = themeShifter((newHue2, initHLS[1],initHLS[2]), theme)
          newHLS3 = themeShifter((newHue3, initHLS[1],initHLS[2]), theme)
          return [newHLS1, newHLS2, newHLS3]

b = schemaProvider((0.2, 0.3, 0.5), 'triadic','pastel')
print(hls2hex(b[0]), hls2hex(b[1]))

c = schemaProvider((0.2, 0.3, 0.5), 'split_complimentary','cyberpunk')
print(hls2hex(c[0]), hls2hex(c[1]))