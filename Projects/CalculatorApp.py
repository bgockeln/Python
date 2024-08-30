#What does END do, check eval .delete .insert
from tkinter import *
from tkinter.constants import SUNKEN
import tkinter.messagebox

#Create the Window
root = Tk()
root.title("Dikt saine Kalkulator")
mFrame = Frame(root, bg="skyblue", padx=10)
mFrame.pack()

#Functions
def myclick(number):
    calDis.insert(END, number)

def equal():
    try:
        y = str(eval(calDis.get()))
        calDis.delete(0, END)
        calDis.insert(0, y)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    calDis.delete(0, END)

#Display
calDis = Entry(mFrame, relief=SUNKEN, borderwidth=3, width=30)
calDis.grid(row = 0, column = 0, columnspan=3, ipady=2, pady=2)

#Button 1 - 3
but1 = Button(mFrame, text="1", padx= 15, pady = 5, width= 3,command = lambda:myclick(1))
but2 = Button(mFrame, text="2", padx= 15, pady = 5, width= 3, command = lambda:myclick(2))
but3 = Button(mFrame, text="3", padx= 15, pady = 5, width= 3, command = lambda:myclick(3))
but1.grid(row = 1, column = 0, pady=2)
but2.grid(row = 1, column = 1, pady=2)
but3.grid(row = 1, column = 2, pady=2)

#Button 4 - 6
but4 = Button(mFrame, text="4", padx= 15, pady = 5, width= 3, command = lambda:myclick(4))
but5 = Button(mFrame, text="5", padx= 15, pady = 5, width= 3, command = lambda:myclick(5))
but6 = Button(mFrame, text="6", padx= 15, pady = 5, width= 3, command = lambda:myclick(6))
but4.grid(row = 2, column =0, pady=2)
but5.grid(row = 2, column =1, pady=2)
but6.grid(row = 2, column =2, pady=2)

#Button 7 - 9
but7 = Button(mFrame, text="7", padx= 15, pady = 5, width= 3, command = lambda:myclick(7))
but8 = Button(mFrame, text="8", padx= 15, pady = 5, width= 3, command = lambda:myclick(8))
but9 = Button(mFrame, text="9", padx= 15, pady = 5, width= 3, command = lambda:myclick(9))
but7.grid(row = 3, column = 0, pady=2)
but8.grid(row = 3, column = 1, pady=2)
but9.grid(row = 3, column = 2, pady=2)

#Button 0 
but0 = Button(mFrame, text="0", padx= 15, pady = 5, width= 3, command = lambda:myclick(0))
but0.grid(row = 4, column = 1, pady=2)

#Button + - *
butAdd = Button(mFrame, text="+", padx= 15, pady = 5, width= 3, command = lambda:myclick("+"))
butAdd.grid(row = 5, column = 0, pady=2)
butSub = Button(mFrame, text="-", padx= 15, pady = 5, width= 3, command = lambda:myclick("-"))
butSub.grid(row = 5, column = 1, pady=2)
butMul = Button(mFrame, text="*", padx= 15, pady = 5, width= 3, command = lambda:myclick("*"))
butMul.grid(row = 5, column = 2, pady=2)

#Button / clear
butDiv = Button(mFrame, text="/", padx= 15, pady = 5, width= 3, command = lambda:myclick("/"))
butClear = Button(mFrame, text="Clear", padx= 15, pady = 5, width= 12, command = clear)
butDiv.grid(row = 6, column = 0, pady=2)
butClear.grid(row = 6, column = 1, columnspan = 2, pady=2)

#Button =
butEquals = Button(mFrame, text="=", padx= 15, pady = 5, width= 9, command = equal)
butEquals.grid(row = 7, column = 0, columnspan=3, pady=2)


root.mainloop()
