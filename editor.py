import tkinter as tk
# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfilename
import filedialpy   # require pip install filedialpy


def open_file():
    # filepath = askopenfilename(
    #     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    # )
    filepath = filedialpy.openFile()
    print(filepath)
    if not filepath:
        return
    txt_text.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_text.insert(tk.END, text)
    window.title(f"Text Editor - {filepath}")

def save_file():
    # filepath = asksaveasfilename(
    #     defaultextension=".txt",
    #     filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    # )
    filepath = filedialpy.saveFile()
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_text.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Text Editor - {filepath}")


window = tk.Tk()
window.title("Text Editor")

window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(0, minsize=50, weight=0)
window.columnconfigure(1, minsize=100, weight=1)

frm_side = tk.Frame(master=window)
frm_side.grid(row=0, column=0, sticky="ns", padx=5, pady=5)

btn_open = tk.Button(
    master=frm_side, 
    text="OPEN", 
    width=7,
    command=open_file
)
btn_open.grid(row=0, column=0, padx=5, pady=5)

btn_save = tk.Button(
    master=frm_side, 
    text="SAVE AS", 
    width=7,
    command=save_file
)
btn_save.grid(row=1, column=0, padx=5, pady=5)

txt_text = tk.Text(master=window)
txt_text.grid(row=0, column=1, sticky="news")

window.mainloop()