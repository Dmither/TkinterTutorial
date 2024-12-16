import tkinter as tk

window = tk.Tk()
entry = tk.Entry()
entry.pack()
entry.insert(0, "What is your name?")
window.mainloop()