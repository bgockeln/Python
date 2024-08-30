from tkinter import *

root = Tk()
root.title("Dikt saine Kalkulator")
root.geometry("350x200")
ergeb = ""
opvar = "+"
c = ""

#functions for calculation
def addi():
    print("Addition")
    global ergeb


def subt():
    print("Subtraktion")

def multi():
    print("Multiplikation")

def divi():
    print("Division")

#functions to change the operator symbol
def selAdd():
    operatorOben.config(text = "+")
    operatorUnten.config(text="+")

def selSub():
    operatorOben.config(text = "-")
    operatorUnten.config(text="-")

def selMul():
    operatorOben.config(text = "*")
    operatorUnten.config(text="*")

def selDiv():
    operatorOben.config(text = "/")
    operatorUnten.config(text="/")

#radiobutton
header = Label(root, text="Rechenarten")
header.grid(row=0, column=0)

rChoice = IntVar()
rChoice.set(1)
radiobutton1 = Radiobutton(master=root, anchor='w',
                           text="Addition", value=1, variable=rChoice, command= selAdd)
radiobutton1.grid(row=1, column=0)
radiobutton2 = Radiobutton(master=root, anchor='w',
                           text="Subtraktion", value=2, variable=rChoice, command = selSub)
radiobutton2.grid(row=1, column=1)
radiobutton3 = Radiobutton(master=root, anchor='w',
                           text="Multiplikation", value=3, variable=rChoice, command=selMul)
radiobutton3.grid(row=1, column=2)
radiobutton4 = Radiobutton(master=root, anchor="w",
                           text="Division", value=4, variable=rChoice, command=selDiv)
radiobutton4.grid(row=1, column=3)

if rChoice == 1:
    print("+")
elif rChoice == 2:
    print("-")
elif rChoice == 3:
    print("*")
elif rChoice == 4:
    print("/")

def calcin():
    a1 = entryA.get
    b1 = entryB.get
    global c
    c = a1 + b1


#tkinter stuff
enternum1 = Label(root, text="Erste Zahl")
enternum1.grid(row=2, column=0)
operatorOben = Label(root, text=opvar)
operatorOben.grid(row=2, column=1)
enternum2 = Label(root, text="Zweite Zahl")
enternum2.grid(row=2, column=2)

entryA = Entry(root, width=10)
entryA.grid(row=3, column=0)
operatorUnten = Label(root, text="+")
operatorUnten.grid(row=3, column=1)
entryB = Entry(root, width=10)
entryB.grid(row=3, column=2)

def test():
    ergebBox.config(text="kakapopo")

calcBtn = Button(root, text="Berechne", command = calcin)
calcBtn.grid(row = 4, column = 0)
ergebText = Label(root, text="Ergebniss")
ergebText.grid(row=4, column = 1)
ergebBox = Label(root, text=c)
ergebBox.grid(row = 4, column = 2)


mainloop()