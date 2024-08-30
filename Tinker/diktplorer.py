#import main module and filedialog module
from tkinter import *
from tkinter import filedialog

#browse function
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "C:/Users/bengo/Documents/BENBEN",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                        ("all files",
                                                         "*.*")))
    
    label_file_explorer.configure(text="File Opened: " + filename)

#create root window
window = Tk()

#window title
window.title("Der Diktplorer")

#window size
window.geometry("500x500")

#set background color
window.config(background = "white")

#create file explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")

button_explore = Button(window,
                         text = "Browse Files",
                         command = browseFiles)

button_exit = Button(window,
                     text = "Exit",
                     command = exit)

#using grid for positioning
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1, row = 3)

#mainloop
window.mainloop()
