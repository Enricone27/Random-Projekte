from tkinter import * 

root = Tk()

theLabel = Label(root, text="hello Buttons")
theLabel.pack()

topFrame2 = Frame(root)
topFrame2.pack()

bottomFrame2 = Frame(root)
bottomFrame2.pack()

button1 = Button(topFrame2, text="Button1", fg="red")
button2 = Button(topFrame2, text="Button2", fg="blue")
button3 = Button(topFrame2, text="Button3", fg="green")
button4 = Button(bottomFrame2, text="Button4", fg="purple")


button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)


frame3 = Frame(root)
frame3.pack()

one = Label(frame3, text="one", bg="green", fg="Red")
one.pack()
two = Label(frame3, text="two", bg="red", fg="Green")
two.pack(fill=X)
three = Label(frame3, text="three", bg="blue", fg="Green")
three.pack(side=LEFT, fill=Y)


frame4 = Frame(root)
frame4.pack()

label1 = Label(frame4, text="Name")
label2 = Label(frame4, text="Password")
entry1 = Entry(frame4)
entry2 = Entry(frame4)

label1.grid(row=0, sticky=W)
label2.grid(row=1, sticky=E)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(frame4, text="Bleiben? sdfgdsg")
c.grid(columnspan=2)


framefunk6 = Frame(root)
framefunk6.pack()

def printName(event):
    print("helloooo Tämu")

buttonf = Button(framefunk6, text="press", command=printName)
buttonf.pack()

buttonf2 = Button(framefunk6, text="press2")
buttonf2.bind("<Button-1>", printName)
buttonf2.pack()


framefunk7 = Frame(root)
framefunk7.pack()

def leftclick(event):
    print("Left")
def rightclick(event):
    print("Right")
def middleclick(event):
    print("Middle")


framein7 = Frame(framefunk7, width=300, height=250, bg="green")
framein7.bind("<Button-1>", leftclick)
framein7.bind("<Button-2>", middleclick)
framein7.bind("<Button-3>", rightclick)
framein7.pack()



root.mainloop()
