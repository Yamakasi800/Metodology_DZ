import math
import tkinter as tk

# Создаем окно приложения
root = tk.Tk()
root.title("Декартова система координат")
width, height = 1000, 800
canv = tk.Canvas(root, width=width, height=height, bg="white")
canv.pack()


def drawScale(isVertical=1, scale=10, center_x=500, center_y=400, length=500, fill='black'):
    """
    Рисует деления и подписи на заданной оси.

    - isVertical=1: вертикальная ось, иначе горизонтальная.
    - scale: количество пикселей на одну единицу координат.
    - center_x, center_y: экранные координаты начала (0,0).
    - length: длина оси в пикселях.
    - fill: цвет линий и подписей.
    """
    # Вычисляем длину штриха в зависимости от масштаба
    sc = scale // 10 if scale <= 50 else scale // 20

    if not isVertical:
        # Горизонтальные деления
        for i in range(-length // (2 * scale), length // (2 * scale) + 1):
            x = center_x + i * scale
            canv.create_line(x, center_y - sc, x, center_y + sc, fill=fill)
            canv.create_text(x, center_y + 3 * sc, text=str(i), fill=fill)
    else:
        # Вертикальные деления
        for i in range(-length // (2 * scale), length // (2 * scale) + 1):
            y = center_y - i * scale
            canv.create_line(center_x - sc, y, center_x + sc, y, fill=fill)
            canv.create_text(center_x - 3 * sc, y, text=str(i), fill=fill)


def drawAxe(isVertical=1, length=500, center_x=500, center_y=400, scale=10, fill='black'):
    """
    Рисует одну координатную ось с двумя стрелками и делениями.

    Параметры аналогичны drawScale, плюс length—длина самой оси.
    """
    if isVertical:
        # Вертикальная ось (стрелки вверх/вниз)
        canv.create_line(center_x, center_y - length // 2,
                        center_x, center_y + length // 2,
                        arrow='both', fill=fill)
        drawScale(1, scale, center_x, center_y, length)
    else:
        # Горизонтальная ось (стрелки влево/вправо)
        canv.create_line(center_x - length // 2, center_y,
                        center_x + length // 2, center_y,
                        arrow='both', fill=fill)
        drawScale(0, scale, center_x, center_y, length)


def create_dpsk(scale=20, center_x=500, center_y=400, fill='black'):
    """
    Рисует полностью декартову систему координат на холсте:
    сначала Y-ось, затем X-ось.
    """
    drawAxe(1, 800, center_x, center_y, scale, fill)
    drawAxe(0, 1000, center_x, center_y, scale, fill)


# Нарисуем систему координат сразу
create_dpsk()


class Figure:
    """Базовый класс для фигур. Реализует общий метод information()."""
    def information(self):
        print(f'Площадь = {self.ploshad():.2f}; Периметр = {self.perimeter():.2f}')


class Rectangle(Figure):
    """Прямоугольник (width × height)."""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def ploshad(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def draw(self, center_x=750, center_y=200, scale=20):
        # Вычисляем экранные координаты углов и рисуем прямоугольник
        x0 = center_x - (self.width * scale) // 2
        y0 = center_y - (self.height * scale) // 2
        x1 = center_x + (self.width * scale) // 2
        y1 = center_y + (self.height * scale) // 2
        canv.create_rectangle(x0, y0, x1, y1, outline='blue')


class Circle(Figure):
    """Круг (радиус r)."""
    def __init__(self, radius):
        self.radius = radius

    def ploshad(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self, center_x=250, center_y=200, scale=20):
        # Радиус в пикселях и рисуем овал
        r = self.radius * scale
        canv.create_oval(center_x - r, center_y - r,
                         center_x + r, center_y + r,
                         outline='red')


class Triangle(Figure):
    """Треугольник по трем сторонам (a, b, c)."""
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def ploshad(self):
        # Формула Герона для площади
        p = (self.a + self.b + self.c) / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def draw(self, center_x=250, center_y=600, scale=20):
        # Упрощенные координаты вершин для примера
        x1, y1 = center_x, center_y - self.a * scale
        x2, y2 = center_x - self.b * scale, center_y + self.b * scale
        x3, y3 = center_x + self.c * scale, center_y + self.c * scale
        canv.create_polygon(x1, y1, x2, y2, x3, y3,
                            outline='green', fill='')


# Создаем и рисуем фигуры, выводя их данные в консоль
rect = Rectangle(10, 5)
circ = Circle(7)
tri = Triangle(3, 4, 5)

rect.information()
rect.draw()

circ.information()
circ.draw()

tri.information()
tri.draw()

# Запускаем главный цикл Tkinter
root.mainloop()
