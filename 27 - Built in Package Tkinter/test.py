import tkinter as tk
import tkinter.ttk as tkk

window = tk.Tk()

window.title("Test")
window.geometry('800x500')

cmb_1 = tkk.Combobox(window, values=(1, 2, 3, 4), state=)
cmb_1.current(0)
cmb_1.grid(column=0, row=0, pady=30, padx=20)


window.mainloop()
