from tkinter import *
root =Tk()
root.geometry("665x545")
root.title("Sign Up!")
def getval():
    print("Login Successful!!")
    print(f'{uservalue.get()}  {passvalue.get()}')
Label(text="Username").grid(row=0)  # koi farak nahi padta
Label(root,text="Password").grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

Button(text="Submit",command= getval).grid(row=2)
root.mainloop() # event for the GUI