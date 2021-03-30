from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()

root.geometry("1455x1300")
root.title("My first GUI")
# photo = PhotoImage(file="download.png")
# pic = Label(image=photo)
for root, dirs, files in os.walk("/New folder"):
    for file in files:
        if file.endswith(".png"):
            photo = PhotoImage(file=str(file))
            Label(image=photo).pack()

# pic.pack()
root.mainloop()
