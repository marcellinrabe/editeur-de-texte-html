from tkinter import *
from tkinter import ttk


class Item:
    def __init__(self, parent, title):
        self.style = ttk.Style()
        self.style.configure('TMenubutton', font="Arial 10")
        self.menubutton = ttk.Menubutton(parent, text=title)
        self.menu = Menu(self.menubutton, relief="flat")
        self.menubutton.configure(menu=self.menu)


    def add_command(self, label="", command="", accelerator=""):
        self.menu.add_command(label=label, command=command, font="Arial 10", activeforeground="black",
                              activebackground="#f0faf8", accelerator=accelerator)


