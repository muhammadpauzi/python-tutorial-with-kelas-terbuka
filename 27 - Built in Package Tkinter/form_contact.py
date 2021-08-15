import tkinter as tk

window = tk.Tk()
window.title('Test 2')
window.geometry('400x500')

window.resizable(0, 0)

# Title
frame_title = tk.Frame(window)
lbl_title = tk.Label(master=frame_title, font=(
    "Arial", 15), text="Data Contacts")

# Input
frame_input = tk.Frame(window)
lbl_name = tk.Label(master=frame_input, font=(
    "Arial", 10), text="Name", width=30, anchor="w", justify=tk.LEFT)
ntr_name = tk.Entry(master=frame_input, width=40)

lbl_number = tk.Label(master=frame_input, font=(
    "Arial", 10), text="Number", width=30, anchor="w", justify=tk.LEFT)
ntr_number = tk.Entry(master=frame_input, width=40)


# Button
frame_button = tk.Frame(window)
btn_add = tk.Button(master=frame_button, text="Add",
                    width=12, relief=tk.FLAT, bg="#aaa", fg="white")

# Listbox
list_data = tk.Listbox(window, width=64, height=19)

# Title Pack
frame_title.pack(pady=10)
lbl_title.pack()

# Input Pack
frame_input.pack()
lbl_name.pack(pady=3)
ntr_name.pack()

lbl_number.pack(pady=3)
ntr_number.pack()

# Button Pack
frame_button.pack()
btn_add.pack(pady=10)

# Listbox Pack
list_data.pack()

window.mainloop()
