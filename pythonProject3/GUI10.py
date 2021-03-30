from tkinter import *

root =Tk()
canvas_width=800
canvas_height=600
root.geometry(f"{canvas_width}x{canvas_height}")
can_wid=Canvas(root,width=canvas_width,height=canvas_height)
can_wid.pack()

can_wid.create_line(0,0,800,600)
can_wid.create_rectangle(0,0,50,100,fill="blue")
can_wid.create_oval(20,20,500,500,fill="red")
can_wid.create_text(200,200,text="Python Gui")
root.mainloop()