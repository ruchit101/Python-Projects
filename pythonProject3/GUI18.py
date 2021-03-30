from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Status Bar tutorial")

def update():
    statusvar.set("Busy....")
    sbar.update()
    import time
    time.sleep(2)
    statusvar.set("Ready hai !!!")


statusvar = StringVar()
statusvar.set("Ready")

sbar=Label(root,textvariable=statusvar,relief =SUNKEN,anchor="w")
sbar.pack(fill=X,side=BOTTOM)

Button(root,text="Upload",command=update).pack()




root.mainloop()