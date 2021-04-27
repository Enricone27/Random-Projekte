import AllesAnzeigen
import NeueNote
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.pack()
        self.main()
    
    def main (self):
        self.t = Label(self, text="HI")
        self.t.pack()

        menu = Menu(self.master)
        self.master.config (menu = menu)

        file = Menu(menu)
        file.add_command(label="Anzeigen", command= lambda: AllesAnzeigen.funk())
        file.add_command(label="Neu", command= lambda: NeueNote.funk())
        menu.add_cascade(label="Dein Befehl", menu=file)
        
root = Tk()
root.minsize(400,100)
app = Application(master=root)
app.mainloop()
