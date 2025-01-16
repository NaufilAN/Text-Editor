from tkinter import *
import tkinter.filedialog

root = Tk()
root.title("Naufil's Text Editor")

filename = None

def newFile():

    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveAs():

    global text
    t = text.get(0.0, END)

    location = tkinter.filedialog.asksaveasfilename(defaultextension=".txt")

    if not location: return # no file given, return
    
    file = open(location, mode="w+")
    file.write(t)
    file.close()

def openFile():
    file = tkinter.filedialog.askopenfile(mode="r")

    if not file: return # no file given, return

    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

buttonFrame = Frame(root) # frame for all key buttons
buttonFrame.grid(row=0, column=0, sticky=W) # stay on top of page

newFileButton = Button(buttonFrame, text="New", command=newFile)
newFileButton.grid(row=0, column=0)

saveAsButton = Button(buttonFrame, text="Save As", command=saveAs)
saveAsButton.grid(row=0, column=1)

openButton = Button(buttonFrame, text="Open", command=openFile)
openButton.grid(row=0, column=2)

text = Text(root) # create a textfield
Grid.columnconfigure(root, 0, weight=1) #configure columns to allow resize
Grid.rowconfigure(root, 1, weight=1) #configure rows to allow resize
text.grid(sticky='NSEW') # stick to north east

root.mainloop() 