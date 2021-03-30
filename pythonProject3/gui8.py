from tkinter import *

root=Tk()
root.geometry("445x254")
root.title("My Form")

def getval():
    print("Its submitted!!!!")

Label(root,text="Welcome to Ruchit Travels",font="bold").grid(row=0,column=1,pady=14)

Username=Label(root,text="Username")
Password=Label(root,text="Password")
Username.grid(row=1,column=0)
Password.grid(row=2,column=0)

uservalue=StringVar()
passvalue=StringVar()
food=IntVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=1,column=1)
passentry.grid(row=2,column=1)

foodservice=Checkbutton(root,text=" Waanan yummy food???",variable=food)
foodservice.grid(row=4,column=1)

#button
Button(root,text="Submit",command=getval).grid(row=5,column=1)

root.mainloop()