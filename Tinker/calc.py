# Import tkinter Moduke
from tkinter import *

#create the window and name it root
root = Tk()

def clickon():
    a = int(txtfield1.get())
    b = int(txtfield2.get())
    c = a + b
    #res = c
    text4.configure(text=c)

#window title and dimension
root.title("Evil Dick inna House")
root.geometry("350x200")

#adding a table to the root window
textl = Label(root, text = "Dikt saine Kalk")
textl.grid(column=0, row=0)

text2 = Label(root, text="Enter a Number")
text2.grid(column=0, row=1)

text3 = Label(root, text="Enter another number")
text3.grid(column=1, row=1)

text4 = Label(root, text="Ergebniss")
text4.grid(column=2, row=2)

#entry field
txtfield1 = Entry(root, width=5)
txtfield1.grid(column=0, row=2)

txtfield2 = Entry(root, width=5)
txtfield2.grid(column=1, row=2)

buttn = Button(root, text = "calc", 
                fg = "blue", command=clickon)
buttn.grid(column=0, row=3)





#button with red color text inside
#buttn = Button(root, text = "Turn gay",
#               fg = "red", command=clickon)
#button position
#buttn.grid(column=1, row=0)

#main loop for the window
root.mainloop()