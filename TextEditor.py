from tkinter import *
import tkinter.filedialog

root = Tk()
root.title("Naufil's Text Editor")

text = Text(root)
text.grid()

filename = None

def newFile():

    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveAs():

    global text
    t = text.get(0.0, END)

    location = tkinter.filedialog.asksaveasfilename(defaultextension=".txt")

    file = open(location, mode="w+")
    file.write(t)
    file.close()

def openFile():

    file = tkinter.filedialog.askopenfile(mode="r")
    t = file.read()

    text.delete(0.0, END)
    text.insert(0.0, t)

newFileButton = Button(root, text="New", command=newFile)
newFileButton.grid()

saveAsButton = Button(root, text="Save As", command=saveAs)
saveAsButton.grid()

openButton = Button(root, text="Open", command=openFile)
openButton.grid()

root.mainloop() 