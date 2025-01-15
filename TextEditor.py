from tkinter import *
import tkinter.filedialog
import tkinter.simpledialog

root = Tk()
root.title("Naufil's Text Editor")

text = Text(root)
text.grid()

def saveAs():

    global text
    t = text.get(0.0, END)

    location = tkinter.filedialog.asksaveasfilename(defaultextension=".txt")

    file = open(location, mode="w+")
    file.write(t)
    file.close()

saveAsButton = Button(root, text="Save As", command=saveAs)
saveAsButton.grid()

root.mainloop() 