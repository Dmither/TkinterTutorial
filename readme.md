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

## Working with widgets

Кожен віджет визначається класом.

Класичні віджети: пакет tkinter (tkinter.Label). Тематичні віджети: підмодуль ttk (tkinter.ttk.Label).

```py
import tkinter as tk
import tkinter.ttk as ttk
```

**Label** (tk.Label) - відображення тексту або зображень.

```py
label_text = "Hello, Tkinter!"
label = tk.Label(
    text=label_text,
    fg="white",
    bg="#111",
    height=3,
    width=(len(label_text) + 2)
)
```

**Button** (tk.Button) - кнопка, може містити текст, викликає подію.

**Entry** - однорядкове поле вводу. Можна отримати, видалити та додати текст в поле:
- `entry.get()` поверне рядок, введений в поле;
- `entry.delete(0)` видаляє за індексом/зрізом (0, tk.END);
- `entry.insert(0, "Hi!")` вставляє за індексом або в кінець

**Text** - багаторядкове поле вводу. Можна отримати, видалити та додати текст, індекс виду "1.0" вказує на перший рядок та перший символ:
- `text.get("1.0")` повертає за індексом/зрізом (1.0, tk.END);
- `text.delete("1.0")` видаляє за індексом/зрізом;
- `text.insert("1.0", "Hi!")` вставляє за індексом, в кінець рядка або в кінець тексту (tk.END, "\nPut on a new line")

**Frame** - прямокутна область (блок).

Для правильного розміщення кожному віджету може бути вказаний атрибут `master` (верхній рівень за умовчуванням). Порядок додавання віджетів визначається їх додаванням.

Розмір елементів label, button, entry та text (height та width) задається значенням висоти та ширини цифри "0". Розмір frame задається в пікселях.

`tk.END` посилається на кінцевий символ, кінець радка, тексту тощо.

Атрибут `relief` створює рамку навколо віджета: tk.FLAT не має ефекту (стандарт), tk.SUNKEN - втоплення, tk.RAISED - підйом, tk.GROOVE - рів, tk.RIDGE - ребро.

Іменування змінним доцільно давати з префіксом класу (lbl, btn, ent, txt, frm).

## Controlling Layout with Geometry Managers

Менеджер геометрії **.pack()** розміщує віджети у фрейм або вікно у вказаному порядку. За умовчуванням наступний об'єкт розміщується в найвищій позиції після попереднього і відцентровані.

Параметр **fill** визначає напрямок заповнення: tk.X, tk.Y, tk.BOTH

Параметр **side** визначає, з якого боку додається елемент: tk.TOP (за ум.), tk.BOTTOM, tk.LEFT, tk.RIGHT.

Для tk.TOP, tk.BOTTOM працює tk.X; для tk.LEFT, tk.RIGHT - tk.Y.

Параметр **expand=True** дає змогу розтягувати фрейми макету рівномірно у всі сторони разом з tk.BOTH. розтягує сусідні фрейми на однакову кількість пікселів.

Параметри **padx** і **pady** додають відступи навколо віджета.

```py
frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
frame1.pack(fill=BOTH, side=LEFT, expand=True)
frame2 = tk.Frame(master=window, width=200, width=100, bg="blue")
frame2.pack(fill=BOTH, side=LEFT, expand=True)
```

Менеджер геометрії **.place()** розміщує віджети за абсолютними координатами, кожен наступний поверх попереднього.

```py
frame=tk.Frame(master=window, width=150, height=150)
frame.pack()
label = tk.Label(master=frame, text="Hello!")
label.place(x=15, y=20)
```

Менеджер геометрії **.grid()** розділяє вікно або фрейм на рядки і стовпці, додає елемент у відповідну комірку по центру, кожен наступний поверх. Стовпці і рядки розтягуються під розмір найвищого/найширшого елемента.

Параметри **row** і **column** визначають індекси комірки.

Параметри **padx** і **pady** додають відступи навколо комірки.

Параметр **sticky** приймає рядок і одною або кількома літерами (news, як на компасі), за якими розміщає віджет всередині комірки. Регістр і порядок не має значення.

Завчасно для вікна та фрейма можна вказати мараметри рядка/стовпця методати **.columnconfigure()** та **.rowconfigure()**: приймає індекс, вагу (weight=, множник реакції на розтягнення), мінімальний розмір (minsize=)

```py
window.rowconfigure(0, minsize=50)
window.columnfigure([0, 1, 2, 3], minsize=50)
label1 = tk.Label(text="1", bg="black", fg="white")
label2 = tk.Label(text="2", bg="black", fg="white")
label3 = tk.Label(text="3", bg="black", fg="white")
label4 = tk.Label(text="4", bg="black", fg="white")
label1.grid(row=0, column=0)    # центр
label2.grid(row=0, column=1, sticky="ew")   # горизонтально
label3.grid(row=0, column=2, sticky="ns")   # вертикально
label4.grid(row=0, column=3, sticky="news") # на всю комірку
```