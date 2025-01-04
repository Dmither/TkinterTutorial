import tkinter as tk
import random


def randomize():
    lbl_value["text"] = str(random.randint(1, 6))


window = tk.Tk()

window.rowconfigure([0, 1], minsize=50, weight=1)
window.columnconfigure(0, minsize=150, weight=1)

lbl_value = tk.Label(text="press Roll!")
lbl_value.grid(row=0, column=0)

btn_roll = tk.Button(text="Roll", command=randomize)
btn_roll.grid(row=1, column=0, sticky="news")

window.mainloop()