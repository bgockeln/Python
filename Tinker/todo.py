#imports
from tkinter import *
from tkinter import messagebox

#global list to store all the tasks
tasks_list = []

#global variable to count tasks
counter = 1

#function for checking for input errors
def inputError():
    #check if task field is empty or not
    if enterTaskField.get() == "":
        #show error msg
        messagebox.showerror("Input Error")
        return 0
    return 1

#function for clearing contents of task number text field
def clear_taskNumberField():
    #clear the task number text field
    taskNumberField.delete(0.0, END)

#function for clearing the contents of task entry field
def clear_taskField():
    #clear content of task field entry box
    enterTaskField.delete(0, END)

#function for insterting contents from task entry field to text area
def insertTask():
    global counter
    #check for error
    value = inputError()
    #if error occours then return
    if value == 0:
        return
    #add a new line character to the task string
    content = enterTaskField.get() + "\n"
    #store task in list
    tasks_list.append(content)
    #insert content of task entry field to text area and add task one by one
    TextArea.insert("end -1 chars", "[ " + str(counter) + " ] " + content)
    #increment counter
    counter += 1
    #calling function to delete content of task field
    clear_taskField()

#function for deleteing specified task
def delete():
    global counter
    #empty task error check
    if len(tasks_list) == 0:
        messagebox.showerror("No task")
        return
    
    #get task number
    number = taskNumberField.get(1.0, END)

    #get the number of the task to delete
    if number == "\n":
        messagebox.showerror("input error")
        return
    else:
        task_no = int(number)

    #calling function to delete content of task number field
    clear_taskNumberField()
    #delete specified task from list
    tasks_list.pop(task_no - 1)
    #decrement
    counter -= 1
    #whole content of text area widget is deleted
    TextArea.delete(1.0, END)
    #rewriting the task after deleting one task at a time
    for i in range(len(tasks_list)):
        TextArea.insert("end -1 chars", " [ " + str(i + 1) + " ] " + tasks_list[i])

#driver code?
if __name__ == "__main__":
    #create window
    window = Tk()

    #background color
    window.configure(background = "light grey")

    #window title
    window.title("Dikt seine ToDo App")

    #windowsize
    window.geometry("250x300")

    #Task label
    enterTask = Label(window, text = "Enter Your Task", bg ="light green")

    #entrybox for tasks
    enterTaskField = Entry(window)

    #create submit button and place it in the window that calls the insert task function when pressed
    Submit = Button(window, text = "Submit", fg = "black", bg = "grey", command=insertTask)

    #create a text area with specified font
    TextArea = Text(window, height=5, width = 25, font = "lucida 13")

    #create label 
    taskNumber = Label(window, text="Delete Task Number", bg = "blue")

    taskNumberField = Text(window, height = 1, width = 2, font = "lucida 13")

    #create delete button and place it in the window that calls the function delete when pressed
    delete = Button(window, text = "Delete", fg="Black", bg = "red", command = delete)

    #create exit button and place it into the window
    Exit = Button(window, text = "Exit", fg = "black", bg = "red", command = exit)

    #placing widgets with grid method
    enterTask.grid(row = 0, column = 2)
    
    #ipadx attribute to set the entry box horizontal
    enterTaskField.grid(row = 1, column = 2, ipadx = 50)

    Submit.grid(row = 2, column = 2)

    #padx attribute to provide x-axis margin
    TextArea.grid(row = 3, column = 2, padx = 10, sticky = W)

    taskNumber.grid(row = 4, column = 2, pady = 5)

    taskNumberField.grid(row = 5, column = 2)

    delete.grid(row = 6, column = 2, pady = 5)

    Exit.grid(row = 7, column = 2)

    #mainloop
    window.mainloop()
