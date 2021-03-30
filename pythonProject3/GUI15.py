from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x544")
root.title("Radio Button")

def order():
    tmsg.showinfo("Your Order", f"You ordered {(var.get())} ")

var=IntVar()

Label(root,text="Kya chahiye???",padx=14,font="lucida 19").pack()

lis=["Dosa","Idly","Wada","Sambhar","Rava Dosa"]
for i in range(len(lis)):
    radio = Radiobutton(root, text=lis[i], padx=14, variable=var, value=i+1)
    radio.pack(anchor="w")

Button(text="Order Now",command=order).pack()

root.mainloop()