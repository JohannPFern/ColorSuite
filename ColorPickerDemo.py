from tkinter import *
from tkinter import colorchooser
from webcolors import rgb_to_name

import colorsys

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

#Create a window with name "Color Picker" and with resolution of 1920 x 1080
root = Tk()
root.title("Color Picker")
root.geometry("1920x1080")  # set starting size of window

#Deafult color code value to white
#color_code = ((255,255,255),'#ffffff')
#print(color_code)

#WHAT IF WE PASSED A PARAMETER TO CHOOSE_COLOR --> IF THE VALUE OF THE PARAEMETER IS 1 THEN WE DELETE THE 
#OLD FRAMES, AND IF IT IS 0 THEN WE ARE CREATING NEW FRAMES

#OR WHAT IF WE CALL DESTROY IN CHOOSE_COLOR AND PUT IT ON A TIMER (SAY 10-15 SECONDS??)

suggestedColorFrame1 = Frame(root)
ArrayOfAllFrames = []
ArrayOfAllFrames.append(suggestedColorFrame1)
#suggestedColorFrame1.pack()

#button = Button(root , text = "Clear Output" , command = choose_color(1)).pack()

def choose_color():

  # variable to store hexadecimal code of color
  global color_code
  color_code = colorchooser.askcolor(title ="Choose color")
  #print(color_code)

  global schema

  #LockedOrUnlocked = [
  #  "unlocked",
  #  "locked"
#]

  #LockingVariable = StringVar()
  #LockingVariable.set( "unlocked" )

  #drop = OptionMenu( root , LockingVariable , *LockedOrUnlocked )

  #print(schema.get())
  #print(type(schema.get()))

  #test = schema.get();
  #print(test)

  chosenColorHLS = hex2hls(color_code[1])
  #print(chosenColorHLS)
  b = schemaProvider((chosenColorHLS), schema.get(),theme.get())

  global suggestedColorFrame1
  #suggestedColorFrame2 = Frame(root)
  #ArrayOfAllFrames.append(suggestedColorFrame2)

  userChosenLabel = Label(suggestedColorFrame1,text="User Chosen Color").pack()
  userColorCanvas = Canvas(suggestedColorFrame1,bg=hls2hex(b[0]), width=1000, height=100)
  userColorFrame = Frame(suggestedColorFrame1, bg=color_code[1],width=1000, height=100).pack()
  userChosenLabel2 = Label(suggestedColorFrame1,text=str(color_code[1])).pack()    
  
    #If suggesting 1 color
  if(schema.get() == "complimentary"):
    suggestedColorLabel1 = Label(suggestedColorFrame1,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame1,bg=hls2hex(b[0]), width=1000, height=100).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame1,text=str(hls2hex(b[0]))).pack()
    suggestedColorFrame1.pack()

        #return the frame here so we can clear it in the future

    #If suggesting 2 colors
  if(schema.get() == "triadic" or schema.get() == "analog" or schema.get() == "split_complimentary"):
    #global suggestedColorFrame1
    suggestedColorLabel1 = Label(suggestedColorFrame1,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame1,bg=hls2hex(b[0]), width=1000, height=100).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame1,text=str(hls2hex(b[0]))).pack()
    
    suggestedColorLabel3 = Label(suggestedColorFrame1,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame1,bg=hls2hex(b[1]), width=1000, height=100).pack()
    suggestedColorLabel4 = Label(suggestedColorFrame1,text=str(hls2hex(b[1]))).pack()
    suggestedColorFrame1.pack()

    #suggestedColorLabel3 = Label(root,text="Suggested Color #2:").pack()
    #suggestedColorFrame2 = Frame(root, bg=hls2hex(b[1]),width=1000, height=100).pack()
    #suggestedColorLabel4 = Label(root,text=str(hls2hex(b[1]))).pack()

        #return both frames here so we can clear it in the future

    #If suggesting 3 colors
  if(schema.get() == "tetratic"):
    suggestedColorLabel1 = Label(suggestedColorFrame1,text="Suggested Color #1:").pack()
    suggestedColorCanvas1 = Canvas(suggestedColorFrame1,bg=hls2hex(b[0]), width=1000, height=100).pack()
    suggestedColorLabel2 = Label(suggestedColorFrame1,text=str(hls2hex(b[0]))).pack()
    
    suggestedColorLabel3 = Label(suggestedColorFrame1,text="Suggested Color #2:").pack()
    suggestedColorCanvas2 = Canvas(suggestedColorFrame1,bg=hls2hex(b[1]), width=1000, height=100).pack()
    suggestedColorLabel4 = Label(suggestedColorFrame1,text=str(hls2hex(b[1]))).pack()

    suggestedColorLabel5 = Label(suggestedColorFrame1,text="Suggested Color #3:").pack()
    suggestedColorCanvas3 = Canvas(suggestedColorFrame1,bg=hls2hex(b[2]), width=1000, height=100).pack()
    suggestedColorLabel6 = Label(suggestedColorFrame1,text=str(hls2hex(b[2]))).pack()
    suggestedColorFrame1.pack()

        #return all three frames here so we can clear it in the future
    
def clearFrame():
    # destroy all widgets from frame
    for x in ArrayOfAllFrames:
      for widget in x.winfo_children():
        widget.destroy()
    
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

# initial menu text
theme.set( "none" )

themeFrame = Frame(root).pack()

# Change themeFrame back to root to get it to work.
drop = OptionMenu( root , theme , *options )
#Label(themeFrame, text="Choose a theme").pack
drop.pack()

options2 = [
    "complimentary",
    "triadic",
    "analog",
    "split_complimentary",
    "tetratic"
]

schema = StringVar()

# initial menu text
schema.set( "complimentary" )

# Create Dropdown menu
drop = OptionMenu( root , schema , *options2 )
drop.pack()

button = Button(root , text = "Reset all Frames" , command = clearFrame).pack()

LockedOrUnlocked = [
    "unlocked",
    "locked"
]

LockingVariable = StringVar()

# initial menu text
LockingVariable.set( "unlocked" )

# Create Dropdown menu
drop = OptionMenu( root , LockingVariable , *LockedOrUnlocked )





root.mainloop()