import tkinter as tk

window = tk.Tk()

frm_main = tk.Frame(master=window, padx=5, pady=5)
frm_main.pack(fill=tk.X)


frm_fields = tk.Frame(
    master=frm_main,
    relief=tk.SUNKEN,
    borderwidth=2,
    padx=3,
    pady=3
)
frm_fields.pack(fill=tk.X)

frm_fields.columnconfigure(0, weight=0, minsize=50)
frm_fields.columnconfigure(1, weight=1, minsize=50)

fields = [
    "First Name",
    "Last Name",
    "Address Line 1",
    "Address Line 2",
    "City",
    "State/Province",
    "Postal Code",
    "Country"
]

for i in range(len(fields)):
    frm_left = tk.Frame(master=frm_fields)
    frm_left.grid(column=0, row=i, sticky="news")
    lbl = tk.Label(master=frm_left, text=fields[i])
    lbl.pack(side=tk.RIGHT)

    frm_right = tk.Frame(master=frm_fields)
    frm_right.grid(column=1, row=i, sticky="news")
    ent = tk.Entry(master=frm_right)
    ent.pack(fill=tk.X)

frm_sep = tk.Frame(master=frm_main, height=3)
frm_sep.pack(fill=tk.X)

frm_buttons = tk.Frame(master=frm_main, padx=3)
frm_buttons.pack(fill=tk.X)

btn_submit = tk.Button(master=frm_buttons, text="Submit")
btn_submit.pack(side=tk.RIGHT, padx=5)
btn_clear = tk.Button(master=frm_buttons, text="Clear")
btn_clear.pack(side=tk.RIGHT)

window.mainloop()