# Python program to create color chooser dialog box
 
# importing tkinter module
from tkinter import *
 
# importing the choosecolor package
from tkinter import colorchooser

def choose_color():
 
    # variable to store hexadecimal code of color
    color_code = colorchooser.askcolor(title ="Choose color")
    print(color_code)

root = Tk()
root.title("Color Suite Tool")
root.geometry("800x600")
root.config(bg="lightgrey")


##color chooser row 0------------------------------------------
# Create Label
label = Label( root , text = " Choose a color" )
label.grid(row= 0, column=0, padx=10, pady=10, sticky=W)

button = Button(root, text = "Color Select",
                   command = choose_color)
button.grid(row=0, column=1, padx=10, pady=10, sticky=W)


##dropdown menus row 1------------------------------------------
# Add a grid for each dropdownmenu
themeFrame = Frame(root)
themeFrame.grid(column=0,row=1, sticky=(N,W,E,S) )
themeFrame.columnconfigure(0, weight = 1)
themeFrame.rowconfigure(0, weight = 1)
themeFrame.grid(pady = 20, padx = 20)

schemeFrame = Frame(root)
schemeFrame.grid(column=1,row=1, sticky=(N,W,E,S) )
schemeFrame.columnconfigure(0, weight = 1)
schemeFrame.rowconfigure(0, weight = 1)
schemeFrame.grid(pady = 20, padx = 20)

# Create a Tkinter variables
themePopupVar = StringVar(root)
schemePopupVar = StringVar(root)

# set theme and suite options
themes = { 'Pastel','Sad','Jewel','Pop','Sad','Contrast','Noir'}
themePopupVar.set('Pastel') # set the default option

schemes = {'Complimentary','Tridadic','Tetratic','Analagous','MonoChromatic'}
schemePopupVar.set('Complimentary') # set the default option

popupMenu = OptionMenu(themeFrame, themePopupVar, *themes)
Label(themeFrame, text="Choose a theme").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

popupMenu = OptionMenu(schemeFrame, schemePopupVar, *schemes)
Label(schemeFrame, text="Choose a scheme").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_theme(*args):
    print( themePopupVar.get() )

# on change dropdown value
def change_scheme(*args):
    print( schemePopupVar.get() )

# link function to change dropdown
themePopupVar.trace('w', change_theme)
schemePopupVar.trace('w', change_scheme)

root.mainloop()
