# My personal Tkinter Tutorial

## Building my first Python GUI App with Tkinter

**Вікно** - основиний елемент GUI Tkinter. В ньому перебувають **віджети** - усі інші елементи GUI.

```py
import tkinter as tk
window = tk.Tk()    # створює екземпляр вікна
greeting = tk.Label(text="Hello, Tkinter")
# створює мітку (текстове поле)
greeting.pack() # додає мітку до вікна
window.mainloop()
```

Команда `window.mainloop()` запускає цикл подій. Він відстежує події і блокує будь-який код, надісланий після запуску (блокує оболонку).
