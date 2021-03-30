from tkinter import *

root=Tk()
root.geometry("445x254")
root.title("My Form")

def getval():
    print(f'{namevalue.get(),phonevalue.get(),food.get()}')
    with open("records.txt",'a') as f:
        f.write(f'{namevalue.get(),phonevalue.get(),food.get()}\n')
    print("Its submitted!!!!")


Label(root,text="Welcome to Ruchit Travels",font="bold").grid(row=0,column=1,pady=14)

Name=Label(root,text="Name")
phone =Label(root,text="Phone")
Name.grid(row=1,column=0)
phone.grid(row=2,column=0)

namevalue=StringVar()
phonevalue=StringVar()
food=IntVar()

nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
nameentry.grid(row=1,column=1)
phoneentry.grid(row=2,column=1)

foodservice=Checkbutton(root,text=" Wanna yummy food???",variable=food)
foodservice.grid(row=4,column=1)

#button
Button(root,text="Submit",command=getval).grid(row=5,column=1)

root.mainloop()