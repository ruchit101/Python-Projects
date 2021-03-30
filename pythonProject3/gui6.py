from tkinter import *

root = Tk()
root.geometry("655x333")


def hello():
    print("Hello Buttons!!!")


def tellmename():
    print("Okay! My name is Bourbon_")


def fuckoff():
    print("okay then fuck off from here right now")


frame=Frame(root,borderwidth=6,relief=SUNKEN)
frame.pack(side=TOP)

b1 = Button(frame, fg='black', text='Print Now', command=hello)
b1.pack(anchor="nw", side=LEFT)

b2 = Button(frame, fg='black', text='Tell Me',command=tellmename)
b2.pack(anchor="nw", side=LEFT,padx=100)

b3 = Button(frame, fg='black', text='Fuck Off',command=fuckoff)
b3.pack(anchor="nw", side=LEFT)

root.mainloop()
