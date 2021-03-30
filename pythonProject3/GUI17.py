from tkinter import *
root = Tk()
root.geometry("455x233")
root.title("Scrollbar tutorial")
# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2 scrollbar.config(command=widget.yview)
scrollbar = Scrollbar(root)                     # Create  Scroll Bar
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand = scrollbar.set)         # set yscroll command to scrollbar.set
for i in range(344):
     listbox.insert(END, f"Item {i}")

listbox.pack(fill="both",padx=22)
#text = Text(root, yscrollcommand = scrollbar.set)
#text.pack(fill=BOTH)
scrollbar.config(command=listbox.yview)                    # Set tee config                      
#scrollbar.config(command=text.yview)

root.mainloop()
