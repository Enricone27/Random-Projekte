from tkinter import * 
from tkinter.ttk import *
from turtle import *
from time import *
root = Tk()

lost = ["lil"," lol", "lel"]

tucan = Canvas(root, width= 500, height=500)
tucan.pack()

t= RawTurtle(tucan)
t.forward(50)

aussuch = Combobox(root, height = 5 , width =15, values=lost)
aussuch.pack()
aussuch.set(lost[0])

"""


for ii in range(10):
    for i in lost:
        a= i
        text = Label(root, text=a)
        text.grid(row=1, column=1)
        time.sleep(0.5)
        root.mainloop

"""     

f = Frame(root)
f.pack()

l1 = Label(f, text="123")
l2 = Label(f, text="456")
ll = Label(f, text="000",  relief=SUNKEN)

l1.grid(row=0, column=0)
l2.grid(row=1, column=1)
ll.grid(row=2, column=0, columnspan=2,sticky=W+E)


root.mainloop()