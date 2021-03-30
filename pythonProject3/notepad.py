from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfile
import os


def newfile():
    global file
    root.title("Untitled-Notepad")
    file = None
    textarea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "-Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file == None:
        file = asksaveasfile(initialfile="Untitled.txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            # Save as New File
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + "-Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    textarea.event_generate("<<Cut>>")


def copy():
    textarea.event_generate("<<Copy>>")


def paste():
    textarea.event_generate("<<Paste>>")


def about():
    tmsg.showinfo("About", "This notepad is created by Ruchit Bagdey. All copyrights reserved.")


if __name__ == '__main__':
    root = Tk()
    root.geometry("644x454")
    root.title("Untitled-Notepad")
    root.wm_iconbitmap(".icon\\notepad.ico")

    # Text Area
    textarea = Text(root, font="calibri 13")
    file = None
    textarea.pack(expand=True, fill=BOTH)

    # FILE menu begins
    Main = Menu(root)  # Horizontal menu
    filemenu = Menu(Main, tearoff=0)
    # add commands in the menu

    filemenu.add_command(label="New", command=newfile)
    filemenu.add_command(label="Open", command=openfile)
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=quitApp)
    Main.add_cascade(label="File", menu=filemenu)

    # Filemenu Ends

    # Edit Menu begins
    editmenu = Menu(Main, tearoff=0)
    # add cut ,copy paste commands in the menu

    editmenu.add_command(label="Cut", command=cut)
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    Main.add_cascade(label="Edit", menu=editmenu)

    # Edit Menu ends

    # Help Menu begins
    helpmenu = Menu(Main, tearoff=0)
    # add cut ,copy paste commands in the menu

    helpmenu.add_command(label="About Notepad", command=about)

    Main.add_cascade(label="Help", menu=helpmenu)

    # Help Menu ends

    # Scroll Bar in yaxis
    scrollbar = Scrollbar(textarea)  # Create  Scroll Bar
    scrollbar.pack(side=RIGHT, fill=Y)
    textarea.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=textarea.yview)

    root.config(menu=Main)

    root.mainloop()
