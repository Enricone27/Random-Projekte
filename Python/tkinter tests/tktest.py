import tkinter as tk

class Application(tk.Frame):
    def __init__(self, maste=None):
        super().__init__(maste)
        
        self.pack()

        self.hi_there = tk.Message()
        self.hi_there.pack()
        self.content = tk.Variable()
        self.content.set("Hello World")
        self.hi_there["textvariable"] = self.content
        
root = tk.Tk()
app = Application(maste=root)
app.mainloop()