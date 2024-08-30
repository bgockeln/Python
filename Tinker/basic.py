# Import tkinter Moduke
from tkinter import *

#create the window and name it root
root = Tk()

#window title and dimension
root.title("Evil Dick inna House")
root.geometry("350x200")

#adding a menu
menu = Menu(root)
item = Menu(menu)
menu.add_cascade(label='File', menu=item)
item.add_command(label='New')

root.config(menu=menu)

#adding a table to the root window
textl = Label(root, text = "Are you a transfreak?")
textl.grid()

text2 = Label(root, text="Eat a fat cock!")
text2.grid()

#fuction for clicking the button A
def clickon():
    textl.configure(text = "I just got perverted")

#entry fieldd
txtfield = Entry(root, width=10)
txtfield.grid()

def clickon2():
    res = "you wrote" + txtfield.get()
    text2.configure(text= res)

buttn2 = Button(root, text = "You wrote", 
                fg = "blue", command=clickon2)
buttn2.grid(column=2, row=0)

#button with red color text inside
buttn = Button(root, text = "Turn gay",
               fg = "red", command=clickon)
#button position
buttn.grid(column=1, row=0)

#main loop for the window
root.mainloop()