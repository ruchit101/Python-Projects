from tkinter import *

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("644x454")

    def Title(self,strng):
        self.title(strng)

    def status(self):
        self.var=StringVar()
        self.var.set("Ready")
        self.bar=Label(self,textvar=self.var,relief=SUNKEN,anchor="w")
        self.bar.pack(side=BOTTOM,fill=X)


    def click(self):
        print("Pressed!!")

    def btn(self,var):
        self.butt=Button(self,text=var,command=self.click).pack()
if __name__=='__main__':
    window=GUI()
    window.Title("Class wala GUI")
    window.status()
    window.btn("Click me")
    window.mainloop()
