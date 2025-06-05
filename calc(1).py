from tkinter import *

# Создание основного окна приложения
win = Tk()
win.title("Калькулятор")  # Заголовок окна
win.geometry("325x325")   # Размеры окна
win.resizable(False, False)  # Запрет изменения размера окна

# Поле ввода для выражений и результата
entry = Entry(win, width=50, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Размещение в сетке

# Обработчик нажатия на кнопки цифр и операторов
def click(number):
    entry.insert(END, str(number))  # Добавляет символ в поле ввода

# Очистка поля ввода
def clear():
    entry.delete(0, END)  # Удаляет всё из поля ввода

# Вычисление выражения в поле ввода
def equal():
    try:
        result = eval(entry.get())  # Вычисляет выражение
        entry.delete(0, END)
        entry.insert(0, str(result))  # Выводит результат
    except:
        entry.delete(0, END)
        entry.insert(0, "Ошибка")  # Выводит сообщение об ошибке при неверном вводе

# --- Создание кнопок ---
# Каждая кнопка добавляется в нужную ячейку сетки (grid)
Button(win, text="1", padx=20, pady=10, command=lambda: click(1)).grid(row=1, column=0)
Button(win, text="2", padx=20, pady=10, command=lambda: click(2)).grid(row=1, column=1)
Button(win, text="3", padx=20, pady=10, command=lambda: click(3)).grid(row=1, column=2)

Button(win, text="4", padx=20, pady=10, command=lambda: click(4)).grid(row=2, column=0)
Button(win, text="5", padx=20, pady=10, command=lambda: click(5)).grid(row=2, column=1)
Button(win, text="6", padx=20, pady=10, command=lambda: click(6)).grid(row=2, column=2)

Button(win, text="7", padx=20, pady=10, command=lambda: click(7)).grid(row=3, column=0)
Button(win, text="8", padx=20, pady=10, command=lambda: click(8)).grid(row=3, column=1)
Button(win, text="9", padx=20, pady=10, command=lambda: click(9)).grid(row=3, column=2)

Button(win, text="0", padx=20, pady=10, command=lambda: click(0)).grid(row=4, column=0)
Button(win, text="+", padx=19, pady=10, command=lambda: click('+')).grid(row=4, column=1)
Button(win, text="-", padx=21, pady=10, command=lambda: click('-')).grid(row=4, column=2)

Button(win, text="*", padx=20, pady=10, command=lambda: click('*')).grid(row=5, column=0)
Button(win, text="/", padx=21, pady=10, command=lambda: click('/')).grid(row=5, column=1)
Button(win, text="C", padx=18, pady=10, command=clear).grid(row=5, column=2)  # Очистка

# Кнопка "равно" занимает всю ширину последней строки
Button(win, text="=", padx=60, pady=10, command=equal).grid(row=6, column=0, columnspan=3)

# Запуск главного цикла приложения
win.mainloop()
