from tkinter import * 
import tkinter.messagebox
root = Tk()

# main Menu
def leer():
    print("lololol")



menüs = Menu(root)
root.config(menu=menüs)

subMenu = Menu(menüs, tearoff=0)
menüs.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New File", command= leer)
subMenu.add_command(label="New Window", command= leer)
subMenu.add_separator()
subMenu.add_command(label="Exit", command= root.quit)

editMenu = Menu(menüs)
menüs.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Lololo")


# Toolbar

toolbar = Frame(root, bg="blue")

insertButton = Button(toolbar, text="Bild", command=leer)
insertButton.pack(side=LEFT, padx=20, pady=2)
printButton = Button(toolbar, text="Druck", command=leer)
printButton.pack(side=LEFT, padx=10, pady=2)
exitButton = Button(toolbar, text="EXIT", command= root.quit)
exitButton.pack(side=LEFT)

toolbar.pack(side=TOP, fill=X)

# Statusbar

status = Label(root, text="Preparing", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

# MessageBox

#tkinter.messagebox.showinfo("Window Title", "777")

#antwort = tkinter.messagebox.askquestion("Que", "lol?" )

#if antwort == "yes":
 #   print(":)")

# Shapes

canvas = Canvas(root, width=200, height= 200)
canvas.pack()

blackline = canvas.create_line(0,0,200,50)
redline= canvas.create_line(0,100,200,50, fill="red")
greenbox = canvas.create_rectangle(25,25,60,70, fill="green")

canvas.delete(redline)

# photo

photo = PhotoImage(file="3 special.PNG")
photolabel = Label(root, image=photo)
photolabel.pack()


root.mainloop()