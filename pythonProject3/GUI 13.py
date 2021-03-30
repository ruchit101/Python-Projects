from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x545")
root.title("Nothing")
def getval():
    print("jdbchav")

def Help():
    tmsg.showinfo("Help","I will help you!!!")

def rate():
    ans=tmsg.askquestion("Rate Us","Did You Like?????")
    if ans=="yes":
        msg="Rate on Google playStore"
    else:
        msg="Kaun be"
    tmsg.showinfo("Message",msg)

#mymenu = Menu(root)
#mymenu.add_command(label='file',command=getval)
#mymenu.add_command(label='Exit',command=quit)
#root.config(menu=mymenu)

Main=Menu(root)
file=Menu(Main,tearoff=0)
file.add_command(label="File",command=getval)
file.add_command(label="Save",command=getval)
file.add_separator()
file.add_command(label="Save As",command=getval)
file.add_command(label="Print",command=getval)
file.add_command(label="Options",command=getval)

edit=Menu(Main,tearoff=0)
edit.add_command(label="Edit",command=getval)
edit.add_command(label="Add",command=getval)
edit.add_separator()
edit.add_command(label="Save As",command=getval)
edit.add_command(label="Okay",command=getval)
edit.add_command(label="Options",command=getval)

m3=Menu(Main)
m3.add_command(label="Help",command=Help)
m3.add_command(label="Rate Us",command=rate)

# config and cascade
root.config(menu=Main)
Main.add_cascade(label="FILE",menu=file)
Main.add_cascade(label="EDIT",menu=edit)
Main.add_cascade(label="HELP",menu=m3)
root.mainloop()