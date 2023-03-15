from tkinter import *
from tkinter import colorchooser, ttk
from webcolors import rgb_to_name

import tkinter as tk

import colorsys
def theme_popup():
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Theme Help!")
   Label(top, text= "Theme Help!", font=('Mistral 18 bold')).place(x=150,y=80)

def schema_popup():
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Schema Help!")
   Label(top, text= "Schema Help!", font=('Mistral 18 bold')).place(x=150,y=80)

def tns_popup():
   top= Toplevel(root)
   top.geometry("750x250")
   top.title("Tints & Shades Help!")
   Label(top, text= "Tints & Shades Help!", font=('Mistral 18 bold')).place(x=150,y=80)

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
  userColorCanvas = Canvas(UserColorChoiceFrame,bg=color_code[1], width=1000, height=20).pack()
  userChosenLabel2 = Label(UserColorChoiceFrame,text=str(color_code[1])).pack()
  check = Checkbutton(UserColorChoiceFrame, text='Lock Color', variable=LockingVariableColorChoice, onvalue='locked', offvalue='unlocked').pack()
  UserColorChoiceFrame.pack()
  ArrayOfAllFrames.append(UserColorChoiceFrame)
  ArrayOfAllLockingVariables.append(LockingVariableColorChoice)
  ArrayOfAllCanvas.append(userColorCanvas)

    #If suggesting 1 color
  if(schema.get() == "complimentary"):
    suggestedColorFrame1 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame1,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame1,bg=hls2hex(b[0]), width=1000, height=20).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame1,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame1, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame1.pack()
    ArrayOfAllFrames.append(suggestedColorFrame1)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1)
    

    #If suggesting 2 colors
  if(schema.get() == "triadic" or schema.get() == "analog" or schema.get() == "split_complimentary"):
    suggestedColorFrame2 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame2,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame2,bg=hls2hex(b[0]), width=1000, height=20).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame2,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame2, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame2.pack()
    ArrayOfAllFrames.append(suggestedColorFrame2)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1) 

    
    suggestedColorFrame3 = Frame()
    suggestedColorLabel3 = Label(suggestedColorFrame3,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame3,bg=hls2hex(b[1]), width=1000, height=20).pack()
    suggestedColorLabel4 = Label(suggestedColorFrame3,text=str(hls2hex(b[1]))).pack()
    check = Checkbutton(suggestedColorFrame3, text='Lock Color', variable=LockingVariableSuggestion2, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame3.pack()
    ArrayOfAllFrames.append(suggestedColorFrame3) 
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion2)
    ArrayOfAllCanvas.append(suggestedColorCanvas2) 

    #If suggesting 3 colors
  if(schema.get() == "tetratic"):
    suggestedColorFrame4 = Frame()
    suggestedColorLabel1 = Label(suggestedColorFrame4,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame4,bg=hls2hex(b[0]), width=1000, height=20).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame4,text=str(hls2hex(b[0]))).pack()
    check = Checkbutton(suggestedColorFrame4, text='Lock Color', variable=LockingVariableSuggestion1, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame4.pack()
    ArrayOfAllFrames.append(suggestedColorFrame4)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion1)
    ArrayOfAllCanvas.append(suggestedColorCanvas1)
    
    suggestedColorFrame5 = Frame()
    suggestedColorLabel3 = Label(suggestedColorFrame5,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame5,bg=hls2hex(b[1]), width=1000, height=20).pack()
    suggestedColorLabel4 = Label(suggestedColorFrame5,text=str(hls2hex(b[1]))).pack()
    check = Checkbutton(suggestedColorFrame5, text='Lock Color', variable=LockingVariableSuggestion2, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame5.pack()
    ArrayOfAllFrames.append(suggestedColorFrame5)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion2)
    ArrayOfAllCanvas.append(suggestedColorCanvas2)

    suggestedColorFrame6 = Frame()
    suggestedColorLabel5 = Label(suggestedColorFrame6,text="Suggested Color #3:").pack()
    suggestedColorCanvas3 = Canvas(suggestedColorFrame6,bg=hls2hex(b[2]), width=1000, height=20).pack()
    suggestedColorLabel6 = Label(suggestedColorFrame6,text=str(hls2hex(b[2]))).pack()
    check = Checkbutton(suggestedColorFrame6, text='Lock Color', variable=LockingVariableSuggestion3, onvalue='locked', offvalue='unlocked').pack()
    suggestedColorFrame6.pack()
    ArrayOfAllFrames.append(suggestedColorFrame6)
    ArrayOfAllLockingVariables.append(LockingVariableSuggestion3)
    ArrayOfAllCanvas.append(suggestedColorCanvas3)

        #return all three frames here so we can clear it in the future
    
#Need To FOCUS ON THIS SECTION!!!!!!!!!!!!!!!!!!!!!!!
#Need to focus on change from dropdown menu to checkbuttons, then need to get the value of the 
#checkbutton from the array of all frames so we know which ones we want to clear when we click the "Reset All Frames Button"

#What if instead I had an array that held the locking variables, that way we check the array and then delete the corresponding
#Frame in the ArrayOfAllFrames.


def showShadesAndTints():
   pass
  #for x in ArrayOfAllCanvas:
    #x.config(bg = "green")
    #LockingVariableSuggestion3 = StringVar()
    #LockingVariableSuggestion3.set( "unlocked" )
    #suggestedColorLabel5 = Label(suggestedColorFrame6,text="Suggested Color #3:").pack()
    #suggestedColorCanvas3 = Canvas(suggestedColorFrame6,bg="white", width=1000, height=20).pack()
    #suggestedColorLabel6 = Label(suggestedColorFrame6,text="white").pack()
    #check = Checkbutton(suggestedColorFrame6, text='Lock Color', variable=LockingVariableSuggestion3, onvalue='locked', offvalue='unlocked').pack()
    #suggestedColorFrame6.pack()


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

    #for x in ArrayOfAllFrames:
      #for widget in x.winfo_children():
        #for i, subwidget in enumerate(widget.winfo_children()):
        #if isinstance(widget, tk.OptionMenu):
          #print("We got here")
          #print(widget.getvar("LockingVariableSuggestion3"))
          #print(widget.getvar())
          #if(widget.state() == "Unlocked"):
            #print(True)
        #widget.destroy()
      #x.pack_forget()

    #for i in range(len(ArrayOfAllFrames)):
      #del ArrayOfAllFrames[i]
    #print(len(ArrayOfAllFrames))
    
    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    #suggestedColorFrame1.pack_forget()


#def updateThemeOrSchema():
#  #suggestedColorLabel1.pack_forget()
#  suggestedColorFrame1.pack_forget()
#  #suggestedColorLabel2.pack_forget() 
#  print(theme.get())

# Create label
selectAColorlabel = Label(root, text="Pick a color by clicking on the button below:").pack()
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
ttk.Button(root, text= "?: T&S", command= schema_popup).pack()


button = Button(root , text = "Remove Unlocked Colors" , command = clearFrame).pack()

root.mainloop()