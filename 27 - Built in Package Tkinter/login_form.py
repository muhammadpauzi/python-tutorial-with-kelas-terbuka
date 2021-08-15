from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('400x300')

c = ttk.Frame(root, padding=(10))
c.grid(column=0, row=0, sticky=(N, W, E, S))

lbl_title = ttk.Label(c, text="Login Form")
lbl_title.grid(column=0,row=0)

ntr_username = ttk.Entry(c)
ntr_username.grid(column=0,row=1,sticky=(W,E),pady=10)

root.mainloop()