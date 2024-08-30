# Import tkinter Moduke
from tkinter import *

#create the window and name it root
root = Tk()

#window title and dimension
root.title("Evil Dick inna House")
root.geometry("350x200")

#adding a table to the root window
textl = Label(root, text = "Are you a transfreak?")
textl.grid()

#fuction for clicking the button A
def clickon():
    textl.configure(text = "I just got perverted")

#entry field
txtfield = Entry(root, width=10)
txtfield.grid()

buttn2 = Button(root, text = "You wrote", 
                )

#button with red color text inside
buttn = Button(root, text = "Turn gay",
               fg = "red", command=clickon)
#button position
buttn.grid(column=1, row=0)

#main loop for the window
root.mainloop()