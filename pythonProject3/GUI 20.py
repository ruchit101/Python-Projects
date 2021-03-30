from tkinter import *

root=Tk()

root.geometry("645x444")
root.title("Haha")
root.wm_iconbitmap("1.ico")
root.configure(background="grey")

width=root.winfo_screenmmwidth()
height=root.winfo_screenmmheight()

print(f"{width}x{height}")
Button(root,text="Destroy",command=root.destroy).pack()
root.mainloop()