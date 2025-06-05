import tkinter as tk
import math

# Функция для рисования делений на осях координат
def drawScale(isVertical, scale, center_x, center_y, length):
    '''
    Рисует деления на осях координат.

    Parameters:
    isVertical (bool): True для вертикальной оси, False — для горизонтальной.
    scale (int): Масштаб, количество пикселей на единицу координат.
    center_x (int): Координата X центра оси.
    center_y (int): Координата Y центра оси.
    length (int): Длина оси в пикселях.
    '''
    if isVertical:
        for i in range(-length // (2 * scale), length // (2 * scale) + 1):
            y = center_y - i * scale
            canv.create_line(center_x - 5, y, center_x + 5, y, fill='gray')  # черточки делений
            canv.create_text(center_x - 15, y, text=str(i), font=("Arial", 8))  # подписи делений
    else:
        for i in range(-length // (2 * scale), length // (2 * scale) + 1):
            x = center_x + i * scale
            canv.create_line(x, center_y - 5, x, center_y + 5, fill='gray')
            canv.create_text(x, center_y + 15, text=str(i), font=("Arial", 8))

# Функция для рисования одной координатной оси (X или Y)
def drawAxe(center_x, center_y, scale, isVertical=1, length=800, fill='black'):
    '''
    Рисует одну координатную ось (X или Y).

    Parameters:
    center_x (int): Координата X центра.
    center_y (int): Координата Y центра.
    scale (int): Масштаб.
    isVertical (int): 1 — вертикальная ось, 0 — горизонтальная.
    length (int): Длина оси.
    fill (str): Цвет линии оси.
    '''
    if isVertical:
        y_shift = (height - length) // 2
        canv.create_line(center_x, y_shift, center_x, y_shift + length, arrow='first', fill=fill, width=2)  # ось Y
        drawScale(1, scale, center_x, center_y, length)
        canv.create_text(center_x + 15, y_shift, text='Y', font=("Arial", 12, "bold"), fill=fill)
    else:
        x_shift = (width - length) // 2
        canv.create_line(x_shift, center_y, x_shift + length, center_y, arrow='last', fill=fill, width=2)  # ось X
        drawScale(0, scale, center_x, center_y, length)
        canv.create_text(x_shift + length, center_y - 15, text='X', font=("Arial", 12, "bold"), fill=fill)

# Функция для создания координатной плоскости (оси + сетка)
def create_dpsk(axesx=1, axesy=1, scale=10, center_x=500, center_y=400, fill='black'):
    '''
    Создает декартову систему координат с сеткой.

    Parameters:
    axesx (int): Показывать ось X (1 — да, 0 — нет).
    axesy (int): Показывать ось Y (1 — да, 0 — нет).
    scale (int): Масштаб (пикселей на единицу).
    center_x (int): Центр по X.
    center_y (int): Центр по Y.
    fill (str): Цвет осей.
    '''
    if axesy:
        drawAxe(center_x=center_x, center_y=center_y, scale=scale, fill=fill, isVertical=1, length=height)
    if axesx:
        drawAxe(center_x=center_x, center_y=center_y, scale=scale, fill=fill, isVertical=0, length=width)
    draw_grid(scale, center_x, center_y)

# Функция для рисования фоновой сетки
def draw_grid(scale, center_x, center_y):
    '''
    Рисует фоновую сетку.

    Parameters:
    scale (int): Масштаб.
    center_x (int): Центр по X (не используется).
    center_y (int): Центр по Y (не используется).
    '''
    for x in range(0, width, scale):
        canv.create_line(x, 0, x, height, fill='#ddd')  # вертикальные линии
    for y in range(0, height, scale):
        canv.create_line(0, y, width, y, fill='#ddd')  # горизонтальные линии

# Целевая функция — синус
def f(x):
    '''
    Целевая функция для построения (синус).

    Parameters:
    x (float): Значение аргумента.

    Returns:
    float: Значение синуса от x.
    '''
    return math.sin(x)

# Функция для рисования графика функции и точки
def draw_func(func, a, b, scale, center_x, center_y, x, fill='black', width=1, fill_dot='red'):
    '''
    Рисует график функции на отрезке [a, b] с отметкой точки x.

    Parameters:
    func (callable): Функция для построения.
    a (float): Левая граница интервала.
    b (float): Правая граница интервала.
    scale (int): Масштаб.
    center_x (int): Центр по X.
    center_y (int): Центр по Y.
    x (float): Точка, которую нужно отметить на графике.
    fill (str): Цвет линии графика.
    width (int): Толщина линии графика.
    fill_dot (str): Цвет отмеченной точки.
    '''
    length = b - a
    h = 0.1
    n = int(length / h)
    for i in range(n):
        x0 = (a + i * h) * scale
        y0 = func(a + i * h) * scale
        x1 = (a + (i + 1) * h) * scale
        y1 = func(a + (i + 1) * h) * scale
        canv.create_line(center_x + x0, center_y - y0, center_x + x1, center_y - y1, fill=fill, width=width)

    y = func(x)
    canvas_coord_x = center_x + x * scale
    canvas_coord_y = center_y - y * scale
    r = 4
    canv.create_oval(canvas_coord_x - r, canvas_coord_y - r, canvas_coord_x + r, canvas_coord_y + r, fill=fill_dot)
    canv.create_text(canvas_coord_x + 30, canvas_coord_y - 10, text=f'{x:.2f}, {y:.2f}', font=("Arial", 10))

# --- Параметры окна и графика ---
width = 1000       # ширина окна
height = 800       # высота окна
s = 100            # масштаб: 1 ед. координат = 100 пикселей
center_x = width // 2   # центр X
center_y = height // 2  # центр Y
width_func_f = 3        # толщина линии графика

# --- Настройка окна tkinter ---
root = tk.Tk()
root.title("График функции")
canv = tk.Canvas(root, width=width, height=height, bg='white')
canv.pack()
root.resizable(False, False)

# --- Рисуем координатную плоскость и график функции ---
create_dpsk(axesx=1, axesy=1, scale=s, center_x=center_x, center_y=center_y, fill='black')
draw_func(f, -7, 7, scale=s, center_x=center_x, center_y=center_y, x=2, fill='orange', fill_dot='red', width=width_func_f)

# --- Запуск графического интерфейса ---
root.mainloop()
