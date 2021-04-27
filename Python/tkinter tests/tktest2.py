import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.pack()

        self.t = tk.Label(self, text="HI")
        self.t.pack()

        menu = tk.Menu(self.master)
        self.master.config (menu = menu)

        file = tk.Menu(menu)
        file.add_command(label="Eins", command= lambda: self.printerlol("hi"))
        menu.add_cascade(label="File", menu=file)
        edit = tk.Menu(menu)
        edit.add_command(label="Undu")
        menu.add_cascade(label="Edit", menu= edit)

    def printerlol(self,insel="lolo"):
        insello = insel
        print(insello+"tot")
        


root = tk.Tk()
root.minsize(400,100)
app = Application(root)
app.mainloop()