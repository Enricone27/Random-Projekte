from tkinter import *

root = Tk()
root.title("TOP")

f2 = Frame(root, bg="blue")
f2.pack(fill=X)
ex = Entry(f2, width=50, bg ="red", fg="white", borderwidth=5)
ex.pack()

e=Entry(f2, width=50)
e.pack()
e.insert(0, "name: ")
e.delete(3, END)
l = Label(root)

"""
def delite():
    l.pack_forget()
"""
print(l.winfo_exists())
def lolo(lettr):
    global l
    l.destroy()
    hello = e.get()
    l= Label(f2, text=hello+lettr)
    l.pack()

b = Button(f2, text="Submit", command=lambda: lolo("f"))
b.pack(pady=10)

"""
b2 = Button(f2, text="Delite", command=delite)
b2.pack(pady=10)
"""
bd = Button(f2, text="not da")
bd.pack(pady=10)
bd['state']= DISABLED





lol= Frame(root)
lol.pack()


status = Label(lol ,  text="tel",relief= SUNKEN)
status2 = Label(lol ,  text="let", relief= SUNKEN)
st3 = Label(lol, text="lach", relief=SUNKEN)

status2.grid(row=1, column=0)

status.grid(row=0, column=1)

st3.grid(row=3, columnspan=2, sticky=E+W)










root.mainloop()