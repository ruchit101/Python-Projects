from tkinter import *
from PIL import Image,ImageTk

root = Tk()
root.title("My Gui with Bourbon_")
root.geometry("455x300")
#photo = PhotoImage(file="download.png")
#pic = Label(image=photo)

openimage = Image.open("PHOTO.jpg")
picture= ImageTk.PhotoImage(openimage)
pic=Label(image=picture)
pic.pack()
root.mainloop()
