import tkinter as tk

def check_enter(event):
    if event.keysym == "Return" or event.keysym == "KP_Enter":
        convert()

def convert():
    try:
        value = float(ent_temperature.get())
        result = round((value - 32) * 5 / 9, 1)
        lbl_result["text"] = f"{result}\N{DEGREE CELSIUS}"
    except:
        lbl_result["text"] = ""

window = tk.Tk()
window.title("F2C")
window.resizable(False, False)

frm_main = tk.Frame(master=window)
frm_main.pack(padx=10, pady=10)

frm_temp = tk.Frame(master=frm_main)
frm_temp.grid(row=0, column=0)

ent_temperature = tk.Entry(master=frm_temp, width=3)
ent_temperature.bind("<Key>", check_enter)
ent_temperature.grid(row=0, column=0)

lbl_far = tk.Label(master=frm_temp, text="\N{DEGREE FAHRENHEIT}")
lbl_far.grid(row=0, column=1)

btn_convert = tk.Button(
    master=frm_main, 
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=convert
)
btn_convert.grid(row=0, column=1, padx=10)

lbl_result = tk.Label(
    master=frm_main, 
    text="", 
    width=6,
    anchor="e"
)
lbl_result.grid(row=0, column=2)

window.mainloop()