from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

f3=Frame(root,borderwidth=8,bg="grey",relief=SUNKEN)
f3.pack(side=BOTTOM,fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack( pady=142)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red")
l.pack(pady=22)

m= Label(f3,text="3rd Frame",font="Helvetica 13 bold",fg="black")
m.pack(pady=22)

root.mainloop()