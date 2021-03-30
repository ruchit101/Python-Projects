from tkinter import *
import tkinter.messagebox as tmsg
root=Tk()
root.geometry("644x544")
root.title("Slider")

def getval():
    with open("records1.txt",'a') as f:
        f.write(f"{my_slider.get()}\n")
    tmsg.showinfo("Rate Us",f"Thank You for rating us!!")
#title
Label(root,text="How was your customer experience ??").pack()
my_slider=Scale(root,from_=0,to=10,orient=HORIZONTAL,tickinterval=1)
my_slider.pack()

Button(root,text="Submit",command=getval).pack()
root.mainloop()