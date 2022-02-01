from tkinter import *
from tkinter import ttk
from tkinter.font import Font


def add_cascade(parent, label):
    newmenu = Menu(parent, background="white", activeborderwidth=0)
    parent.add_cascade(menu=newmenu, label=label, font=menubarfont)
    return newmenu


def add_command(parent, label):
    return parent.add_command(label=label,
                              font=menubarfont,
                              background="white")

root = Tk()
root.geometry("1200x600+0+0")
root.title("Editeur de texte")
root.option_add('*tearOff', FALSE)
#root.tk.call("source", "sun-valley.tcl")
#root.tk.call("set_theme", "light")

# variables
menubarfont = Font(family="Liberation Mono", size="10")
namefile = StringVar()
style = ttk.Style()
style.configure("TLabel", font=menubarfont)

# declaration de style
class Menubar:
    def __init__(self, parent):
        self.parent = parent
        self.menubar = Menu(self.parent,
                            relief="groove",
                            background="white",
                            activeborderwidth=0)
        self.parent.configure(menu=self.menubar)

    def additem(self, type, label):
        """
        :rtype: object
        """
        if type == "cascade":
            return add_cascade(self.menubar, label=label)

        elif type == "command":
            return add_command(self.menubar, label=label)

menubar = Menubar(root)
filemenu = menubar.additem("cascade","Fichier")
editmenu = menubar.additem("cascade", "Edition")
formatmenu = menubar.additem("cascade", "Format")
helpmenu = menubar.additem("cascade", "Aide")

add_command(filemenu, "Nouveau")
filemenu.entryconfigure("Nouveau", accelerator="Ctrl+N")

add_command(filemenu, "Ouvrir")
filemenu.entryconfigure("Ouvrir", accelerator="Ctrl+O")

add_command(filemenu, "Enregistrer")
filemenu.entryconfigure("Enregistrer", accelerator="Ctrl+S")

add_command(filemenu, "Enregistrer sous")
filemenu.entryconfigure("Enregistrer sous", accelerator="Ctrl+Shift+S")

add_command(filemenu, "Fermer")
filemenu.entryconfigure("Fermer", accelerator="Ctrl+X")

add_command(filemenu, "Quitter")

add_command(helpmenu, "License")
add_command(helpmenu, "A propos")

frame = ttk.Frame(root)
notebook = ttk.Notebook(frame)
onglet = ttk.Frame(notebook, height="200", width="200")
notebook.add(onglet, text="hello")
frame.grid(sticky="nwes")
notebook.grid(column=0, row=0)


root.mainloop()