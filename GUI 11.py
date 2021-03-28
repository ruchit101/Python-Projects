from tkinter import *
root=Tk()

def ruchit(event):
    #print(f"Ruchit will be sucessful!!!!!!{event.x},{event.x}")
    pop = Tk()
    pop.geometry("400x50")
    pop.title("popUp")
    Label(pop,text="Ruchit,You are wonderful gr8 Logic!!!!!!",font="32").pack()
    pop.mainloop()

root.geometry("645x447")
root.title("Events")

widget=Button(root,text="Button")
widget.pack()

widget.bind('<Button-1>',ruchit)
widget.bind('<Double-1>',quit)
root.mainloop()