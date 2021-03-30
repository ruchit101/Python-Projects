from tkinter import *
root=Tk()
root.geometry("654x454")
root.title("List Box")

def add_item():
    global i
    lbx.insert(ACTIVE,f"{i}")
    i+=1
i=0
lbx=Listbox(root)
lbx.pack()
lbx.insert(END,"First item of the list box")

Button(root,text="Add",command=add_item).pack()
root.mainloop()