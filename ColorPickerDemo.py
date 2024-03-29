from tkinter import *
from tkinter import colorchooser, ttk
from webcolors import rgb_to_name

import tkinter as tk

import colorsys
# def quickInstructions_popup():
#   top= Toplevel(root)
#   top.geometry("750x250")
#   top.title("Quick Guide")
#   quickGuideTextContent1 = "Quick Guide\n"
#   text1= Label(top, text= quickGuideTextContent1 , font=('comic12'),justify=LEFT) #, bg="green", fg="black")
#   text1.pack(anchor=tk.W, side=TOP)

def theme_popup():
  top = Toplevel(root)
  top.geometry("750x350")
  top.title("Theme Help!")
  themeHelpTextContent1 = "Theme Help!\n"
  text1= Label(top, text= themeHelpTextContent1, font=('comic 12 bold'),justify=LEFT) #, bg="green", fg="black")
  text1.pack(anchor=tk.W, side=TOP)

  themeHelpTextContent2 = "There are a list of given keywords that are \
descriptive to the theme that the tool can generate for the user.\n It is not necessary to \
choose a theme. However, choosing a theme adds a constraint to the color generative \nprocess \
and will affect the bounds of colors that will be generated. Here is a short description of \
each of the \nthemes that are offered by the Color Suite Tool.\n\
"
  text2= Label(top, text= themeHelpTextContent2, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text2.pack(anchor=tk.W, side=TOP)

  themeHelpTextContent3 = "- Pastel theme implements colors that have just enough white mixed into it to look \
pale and soft while \nmaintaining its color. This theme outputs colors of low saturation and brightness.\n\
- Pop theme implements colors that are meant to catch the eye by being bright and very vivid/vibrant.\n \
This is done so by focusing on colors that are higher in saturation and brightness.\n\
- Noir theme implements colors that are more muted and darker. Inspired by the chiaroscuro \
lighting\n of renaissance art and German Expressionism, these colors express emotions of moodiness and brooding.\n\
The tool achieves this palette by lowering both saturation and lightness.\n\
- Cyberpunk theme implements colors that are rich in saturation but low in brightness.\
"
  text3= Label(top, text= themeHelpTextContent3, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text3.pack(anchor=tk.W, side=TOP)

def schema_popup():
  top= Toplevel(root)
  top.geometry("750x300")
  top.title("Schema Help!")
  schemaHelpTextContent1 = "Schema Help!\n"
  text1= Label(top, text= schemaHelpTextContent1, font=('comic 12 bold'),justify=LEFT) #, bg="green", fg="black")
  text1.pack(anchor=tk.W, side=TOP)

  schemaHelpTextContent2 = "\
Color schemes exist to provide to identify harmonious relationships between colors.The Color Suite Tool \n\
implements geometric calculation with respect to the color wheel to identify the desired colors based on the\n\
selected schema. There exist 5 different schemas that the user can choose from, of which their brief \n\
descriptions are listed below.\n"
  text2= Label(top, text= schemaHelpTextContent2, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text2.pack(anchor=tk.W, side=TOP)

  schemaHelpTextContent3 = "- Complimentary - Two colors, located 180 degrees opposite of each other on a color wheel.\n\
- Triadic - Three colors, located equidistant from each other on the color wheel.\n\
- Analogous - Three colors, located sequentially on a color wheel. \n\
- Split-Complementary -  three colors, with one on one side of a color wheel and two located \n\
flanking the compliment, as if analogous.\n\
- Tetradic - Four colors, located equidistant from each other on the color wheel.\n\
"
  text3= Label(top, text= schemaHelpTextContent3, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text3.pack(anchor=tk.W, side=TOP)

def tns_popup():
  top= Toplevel(root)
  top.geometry("750x300")
  top.title("Tints & Shades Help!")
  tnsHelpTextContent1 = "Tints & Shades Help!\n"
  text1= Label(top, text= tnsHelpTextContent1, font=('comic 12 bold'),justify=LEFT) #, bg="green", fg="black")
  text1.pack(anchor=tk.W, side=TOP)

  tnsHelpTextContent2 = "\
Tints refer to lighter versions of a color while shades refer to darker versions. From the color that the user \n\
originally provides, they can receive different tints and shades as to explore similar colors. Tints are shifted to \n\
become warmer in hue, approaching colors like red, orange, and yellow; while shades are shifted to become \n\
colder in hue, approaching purple, blue, and green.\n"
  text2= Label(top, text= tnsHelpTextContent2, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text2.pack(anchor=tk.W, side=TOP)

  tnsHelpTextContent3 = "\
How to use Tints Shades.\n\
After the user has generated colors, they should lock the colors for which they would like to generate tints \n\
and shades for. For each color that they lock, they can expect different \"tints and shades\" for each color \n\
that is locked. If you are unable to see all of the tints and shade outputs, please try removing the colors \n\
that are not locked and locking one color at a time."
  text3= Label(top, text= tnsHelpTextContent3, font=('comic 12'),justify=LEFT) #, bg="green", fg="black")
  text3.pack(anchor=tk.W, side=TOP)
  
def hls2hex(initHLS):
    rgb = colorsys.hls_to_rgb(initHLS[0],initHLS[1],initHLS[2])
    rgb = [round(y*255) for y in rgb]
    r = str(hex(rgb[0])[2:].zfill(2))
    g = str(hex(rgb[1])[2:].zfill(2))
    b = str(hex(rgb[2])[2:].zfill(2))
    return '#' + r+g+b

def hex2hls(hex_value):
    h = hex_value.strip("#")
    rgb = tuple(int(h[i:i+2], 16) for i in (0, 2, 4))
    hls = colorsys.rgb_to_hls(rgb[0]/255, rgb[1]/255, rgb[2]/255)
    return hls

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

#Create a window with name "Color Picker" and with resolution of 1920 x 1080
root = Tk()
root.title("Color Picker")
root.geometry("1920x1080")  # set starting size of window

ArrayOfAllFrames = []
ArrayOfAllLockingVariables = []
ArrayOfAllCanvas = []
ArrayOfAllColors = []

def choose_color():

  # variable to store hexadecimal code of color
  global color_code
  color_code = colorchooser.askcolor(title ="Choose color")
  #print(color_code)

  global schema
 
  chosenColorHLS = hex2hls(color_code[1])
  b = schemaProvider((chosenColorHLS), schema.get(),theme.get())

  LockingVariableColorChoice = StringVar()
  LockingVariableColorChoice.set( "unlocked" )

  LockingVariableSuggestion1 = StringVar()
  LockingVariableSuggestion1.set( "unlocked" )

  LockingVariableSuggestion2 = StringVar()
  LockingVariableSuggestion2.set( "unlocked" )

  LockingVariableSuggestion3 = StringVar()
  LockingVariableSuggestion3.set( "unlocked" )

  UserColorChoiceFrame = Frame()
  userChosenLabel = Label(UserColorChoiceFrame,text="User Chosen Color").pack()
  userColorCanvas = Canvas(UserColorChoiceFrame)
  userColorCanvas.config(bg=color_code[1], width=1000, height=20)
  userColorCanvas.pack()
  userChosenLabel2 = Label(UserColorChoiceFrame,text=str(color_code[1])).pack()
  check = Checkbutton(UserColorChoiceFrame, text='Lock Color', variable=LockingVariableColorChoice, onvalue='locked', offvalue='unlocked').pack()
  UserColorChoiceFrame.pack()
  ArrayOfAllFrames.append(UserColorChoiceFrame)
  ArrayOfAllLockingVariables.append(LockingVariableColorChoice)
  ArrayOfAllCanvas.append(userColorCanvas)
  ArrayOfAllColors.append(color_code[1])

    #If suggesting 1 color
  if(schema.get() == "complimentary"):
    suggestedColorFrame1 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame1,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame1)
    suggestedColorCanvas1.config(bg=hls2hex(b[0]), width=1000, height=20)
    suggestedColorCanvas1.pack()
    suggestedColorLabel2 = Label(suggestedColorFrame1,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame1, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame1.pack()
    ArrayOfAllFrames.append(suggestedColorFrame1)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1)
    ArrayOfAllColors.append(hls2hex(b[0]))
    

    #If suggesting 2 colors
  if(schema.get() == "triadic" or schema.get() == "analog" or schema.get() == "split_complimentary"):
    suggestedColorFrame2 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame2,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame2)
    suggestedColorCanvas1.config(bg=hls2hex(b[0]), width=1000, height=20)
    suggestedColorCanvas1.pack()
    suggestedColorLabel2 = Label(suggestedColorFrame2,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame2, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame2.pack()
    ArrayOfAllFrames.append(suggestedColorFrame2)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1)
    ArrayOfAllColors.append(hls2hex(b[0]))

    
    suggestedColorFrame3 = Frame()
    suggestedColorLabel3 = Label(suggestedColorFrame3,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame3)
    suggestedColorCanvas2.config(bg=hls2hex(b[1]), width=1000, height=20)
    suggestedColorCanvas2.pack()
    suggestedColorLabel4 = Label(suggestedColorFrame3,text=str(hls2hex(b[1]))).pack()
    check = Checkbutton(suggestedColorFrame3, text='Lock Color', variable=LockingVariableSuggestion2, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame3.pack()
    ArrayOfAllFrames.append(suggestedColorFrame3) 
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion2)
    ArrayOfAllCanvas.append(suggestedColorCanvas2)
    ArrayOfAllColors.append(hls2hex(b[1]))

    #If suggesting 3 colors
  if(schema.get() == "tetratic"):
    suggestedColorFrame4 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame4,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame4)
    suggestedColorCanvas1.config(bg=hls2hex(b[0]), width=1000, height=20)
    suggestedColorCanvas1.pack()
    suggestedColorLabel2 = Label(suggestedColorFrame4,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame4, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame4.pack()
    ArrayOfAllFrames.append(suggestedColorFrame4)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1)
    ArrayOfAllColors.append(hls2hex(b[0]))
    
    suggestedColorFrame5 = Frame()
    suggestedColorLabel3 = Label(suggestedColorFrame5,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame5)
    suggestedColorCanvas2.config(bg=hls2hex(b[1]), width=1000, height=20)
    suggestedColorCanvas2.pack()
    suggestedColorLabel4 = Label(suggestedColorFrame5,text=str(hls2hex(b[1]))).pack()
    check = Checkbutton(suggestedColorFrame5, text='Lock Color', variable=LockingVariableSuggestion2, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame5.pack()
    ArrayOfAllFrames.append(suggestedColorFrame5)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion2)
    ArrayOfAllCanvas.append(suggestedColorCanvas2)
    ArrayOfAllColors.append(hls2hex(b[1]))

    suggestedColorFrame6 = Frame()
    suggestedColorLabel5 = Label(suggestedColorFrame6,text="Suggested Color #3:").pack()
    suggestedColorCanvas3 = Canvas(suggestedColorFrame6)
    suggestedColorCanvas3.config(bg=hls2hex(b[2]), width=1000, height=20)
    suggestedColorCanvas3.pack()
    suggestedColorLabel6 = Label(suggestedColorFrame6,text=str(hls2hex(b[2]))).pack()
    check = Checkbutton(suggestedColorFrame6, text='Lock Color', variable=LockingVariableSuggestion3, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame6.pack()
    ArrayOfAllFrames.append(suggestedColorFrame6)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion3)
    ArrayOfAllCanvas.append(suggestedColorCanvas3)
    ArrayOfAllColors.append(hls2hex(b[2]))

        #return all three frames here so we can clear it in the future
    
#Need To FOCUS ON THIS SECTION!!!!!!!!!!!!!!!!!!!!!!!
#Need to focus on change from dropdown menu to checkbuttons, then need to get the value of the 
#checkbutton from the array of all frames so we know which ones we want to clear when we click the "Reset All Frames Button"

#What if instead I had an array that held the locking variables, that way we check the array and then delete the corresponding
#Frame in the ArrayOfAllFrames.

ArrayOfSelectedColors = []

def showShadesAndTints():
  for index, x in enumerate(ArrayOfAllLockingVariables):
    if(x.get() == "locked"):
      ArrayOfSelectedColors.append(index)

  for index in ArrayOfSelectedColors:
    color = ArrayOfAllColors[index]
    HLSColor = hex2hls(color)
    b = tintShade(HLSColor, 2)

    for x in range(5):
      LockingVariableColorChoice = StringVar()
      LockingVariableColorChoice.set( "unlocked" )
      FrameOrTint = Frame()
      if(x == 0 or x == 1):
        FrameOrTintLabel = Label(FrameOrTint,text="Tint").pack()

      if (x == 2):
        FrameOrTintLabel = Label(FrameOrTint,text="Original Color").pack()

      if(x == 3 or x == 4):
        FrameOrTintLabel = Label(FrameOrTint,text="Shade").pack()

      #FrameOrTintLabel = Label(FrameOrTint,text="Tint or Shade").pack()
      FrameOrTintCanvas = Canvas(FrameOrTint)
      FrameOrTintCanvas.config(bg=hls2hex(b[x]), width=1000, height=20)
      FrameOrTintCanvas.pack()
      FrameOrTintLabel2 = Label(FrameOrTint,text=str(hls2hex(b[x]))).pack()
      check = Checkbutton(FrameOrTint, text='Lock Color', variable=LockingVariableColorChoice, onvalue='locked', offvalue='unlocked').pack()
      FrameOrTint.pack()
      ArrayOfAllFrames.append(FrameOrTint)
      ArrayOfAllLockingVariables.append(LockingVariableColorChoice)
      ArrayOfAllCanvas.append(FrameOrTintCanvas)
      ArrayOfAllColors.append(hls2hex(b[x]))
  
  ArrayOfSelectedColors.clear()

    


def updateColorsByTheme():
  pass
  #We can use this code to change existing canvas widgets to be different codes 
  #for index, x in enumerate(ArrayOfAllCanvas):
    #ArrayOfAllCanvas[index].configure(bg = "green")


ItemsToBeDeleted = []
def clearFrame():
    # destroy all widgets from frame

    #Need to add code that deletes the elements within ItemsToBeDeleted and the ArrayOfAllFrames
    #Whenever we clear and remove frames. Because otherwise the size of ItemsToBeDeleted and ArrayOfAllFrames will
    #continue to increase overtime. 

    for index, x in enumerate(ArrayOfAllLockingVariables):
      if(x.get() == "unlocked"):
         ItemsToBeDeleted.append(index)
         #print(ItemsToBeDeleted[index])

         
    for index in ItemsToBeDeleted:
       for widget in ArrayOfAllFrames[index].winfo_children():
          widget.destroy()
          ArrayOfAllFrames[index].pack_forget()
    
    for index in reversed(ItemsToBeDeleted):
       del ArrayOfAllFrames[index]
       del ArrayOfAllLockingVariables[index]
       del ArrayOfAllCanvas[index]
       del ArrayOfAllColors[index]

    ItemsToBeDeleted.clear()

# Create label
selectAColorlabel = Label(root, text="Pick a theme and schema first before you choose your color!").pack()
#label.grid(row=0)

#This code is experimental:

button = Button(root, text = "Select color", command = choose_color).pack()
#button.grid(row=1)

# Dropdown menu options
options = [
    "none",
    "pastel",
    "pop",
    "noir",
    "cyberpunk"
]

theme = StringVar()
theme.set( "none" )
themeFrame = Frame(root).pack()
drop = OptionMenu( root , theme , *options )
drop.pack()

#help informative window for schema
ttk.Button(root, text= "?: theme", command= theme_popup).pack()

options2 = [
    "complimentary",
    "triadic",
    "analog",
    "split_complimentary",
    "tetratic"
]

schema = StringVar()

schema.set( "complimentary" )

drop = OptionMenu( root , schema , *options2 )
drop.pack()

#help informative window for schema
ttk.Button(root, text= "?: schema", command= schema_popup).pack()

button = Button(root , text = "Generate Shades & Tints" , command = showShadesAndTints).pack()
#help informative window for tns
ttk.Button(root, text= "?: T&S", command= tns_popup).pack()


button = Button(root , text = "Remove Unlocked Colors" , command = clearFrame).pack()

root.mainloop()