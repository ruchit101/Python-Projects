from tkinter import *

root=Tk()
#root.geometry("644x545")
root.title("Gui Resize")

def change():
    root.geometry(f"{widthvalue.get()}x{heightvalue.get()}")


Label(root,text="Width :").grid(row=0,column=0)
Label(root,text="Height :").grid(row=1,column=0)

widthvalue=StringVar()
heightvalue=StringVar()

Entry(root,textvariable=widthvalue).grid(row=0,column=1)
Entry(root,textvariable=heightvalue).grid(row=1,column=1)

#Button
but=Button(root,text="Change",command=change)
but.grid(row=4,column=1)
root.mainloop()