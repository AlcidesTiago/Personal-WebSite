"""

In this I have added all the functionality that is required in the notepad.

Main Code After Merging All 2.Importing, 3.Menu_Code and Functionalities_Code

"""

import os
import tkinter.messagebox as tmsg
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk


def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt",
                           filetypes=[("All Files", "*.*"),
                                      ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


# file menu Save As option
def saveAsFile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"),
                                            ("Text Documents", "*.txt")])
        if file == "":
            file = None

        else:
            # Save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # Save the file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


# Print File Function
class ShellExecute:
    pass


def print_file():
    # Ask for file (Which you want to print)
    file_to_print = filedialog.askopenfilename(
        initialdir="/", title="Select file",
        filetypes=(("Text files", "*.txt"), ("all files", "*.*")))

    if file_to_print:
        # Print Hard Copy of File
        ShellExecute()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad",
             "_____This Notepad is Made by Alcides Fernando Tiago____ "
             "\n Contact Me- alcidesft6@gmail.com \n ____if you have any problem___")


def aboutme():
    image = Image.open("EngDev.ico")
    photo = ImageTk.PhotoImage(image)
    image.resize((2, 2), Image.ANTIALIAS)
    varun_label = Label(image=photo)
    varun_label.pack()
    showinfo("Notepad",
             "Hi\nMy name is Alcides Fernando Tiago. I am a Software Engineer."
             "\nI am from Angola. This is my First GUI Software\nI made this by using Python.\nThank You!")


def rate():
    print("Rate us")
    value = tmsg.askquestion("Was your experience Good?", "You used this Notepad Software.. Was your experience Good?")
    if value == "Yes":
        msg = "Great. Rate us on appstore please"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)


if __name__ == '__main__':
    # Basic tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("Notepad.ico")
    root.geometry("644x588")

    # Add TextArea
    TextArea = Text(root, font="lucida 13")
    file = None
    TextArea.pack(expand=True, fill=BOTH)

    # Lets create a menu bar
    MenuBar = Menu(root)

    # File Menu Starts
    FileMenu = Menu(MenuBar, tearoff=0)
    # To open new file
    FileMenu.add_command(label="New                            Ctrl+N", command=newFile)
    FileMenu.add_command(label="New Window            Ctrl+Shift+N", command=newFile)

    # To Open already existing file
    FileMenu.add_command(label="Open...                       Ctrl+O", command=openFile)

    # To save the current file

    FileMenu.add_command(label="Save                            Ctrl+O", command=saveFile)
    FileMenu.add_command(label="Save As...                    Ctrl+Shift+S", command=saveAsFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Page Setup...                 ", command=saveFile)
    FileMenu.add_command(label="Print...                          Ctrl+P", command=print_file)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # File Menu ends

    # Edit Menu Starts
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)

    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    # Edit Menu Ends
    # Format Menu Starts
    FormatMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut, copy and paste
    FormatMenu.add_command(label="Word Wrap")
    FormatMenu.add_command(label="Font")
    FormatMenu.add_command(label="More")
    MenuBar.add_cascade(label="Format", menu=EditMenu)

    # Format Menu Ends
    # Help Menu Starts
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # Help Menu Ends
    AboutMenu = Menu(MenuBar, tearoff=0)
    AboutMenu.add_command(label="About Me", command=aboutme)
    AboutMenu.add_command(label="Rate us", command=rate)
    MenuBar.add_cascade(label="About Me", menu=AboutMenu)

    root.config(menu=MenuBar)

    # Adding Scrollbar
    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    label = Label(text="Made By Alcides Tiago", bg="gray", fg="white", padx=3, pady=4, font="commissars 9 bold",
                  borderwidth=0,
                  relief=SUNKEN)
    label.pack(side=BOTTOM, fill=X, padx=4, pady=4)
    root.mainloop()
