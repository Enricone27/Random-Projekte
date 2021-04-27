from tkinter import * 


class Buttons:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="Print Massage", command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quittButton = Button(frame, text="Quit", command=frame.quit)
        self.quittButton.pack(side=LEFT)

    def printMessage(self):
        print("Niceee!!!")




root = Tk()
b = Buttons(root)
root.mainloop()