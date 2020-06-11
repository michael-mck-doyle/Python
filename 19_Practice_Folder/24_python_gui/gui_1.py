import tkinter as tk
from tkinter import ttk # ttk has advanced widgets, it is an extension of ykinter
win = tk.Tk()
win.title("Python GUI")
#this line adds a label to the gui
aLabel = ttk.Label(win, text="A label")
aLabel.grid(column=0, row=0)
# setting this to  (0, 0) means that the window can't be resized
#win.resizable(0,0)

# modified button click function
def ClickMe():
    action.configure(text='Hello ' + name.get())


# changing our label
ttk.Label(win, text="Enter a name:").grid(column=0, row=0)

win.mainloop()
