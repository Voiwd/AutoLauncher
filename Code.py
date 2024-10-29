from tkinter import *

window = Tk()

window.title("")
window.geometry("600x400")

def create():
    return print("New Preset")

button = Button(window, text="+", command=create)
button.place(relx=0.5, rely=0.5)

window.mainloop()