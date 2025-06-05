from tkinter import *  # GUI библиотека
import math  # Математические функции

class GraphApp:
    def __init__(self, master):
        """
        Инициализация главного окна и параметров графика.

        Args:
            master: Главное окно Tkinter.
        """
        # Инициализация окна
        self.master = master
        self.master.title("Функциональный график")
        self.master.geometry("850x620")
        self.master.resizable(False, False)
        self.master.configure(bg="black")

        # Параметры сетки и смещения для отрисовки
        self.grid_zoom = 60       # Пикселей на единицу координат
        self.shift_x = 0          # Сдвиг по X (в пикселях)
        self.shift_y = 0          # Сдвиг по Y
        self.free_draw = False    # Режим свободного рисования (выключен)
        self.previous = None      # Предыдущая точка при рисовании

        # Доступные функции и константы для eval
        self.allowed = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log,
            "sqrt": math.sqrt,
            "e": math.e,
            "pi": math.pi
        }

        self.build_ui()      # Создаем элементы интерфейса
        self.set_bindings()  # Настраиваем обработчики событий

    def build_ui(self):
        """
        Создание интерфейса приложения: боковая панель и холст.
        """
        # Боковая панель для управления приложением
        self.sidebar = Frame(self.master, width=300, bg="gray")
        self.sidebar.pack(side=LEFT, fill=Y)

        # Ввод функции
        Label(self.sidebar, text="Введите функцию:", bg="dimgray", fg="white").pack(pady=(15, 5))
        self.input = Entry(self.sidebar, font=("Courier", 12))
        self.input.pack(padx=15, pady=5)

        # Кнопка построения графика
        Button(self.sidebar, text="Построить", command=self.render_graph,
               bg="dimgray", fg="white").pack(pady=10)
        # Переключение режима свободного рисования
        Button(self.sidebar, text="Свободное рисование", command=self.toggle_drawing_mode).pack()

        # Слайдер для изменения масштаба сетки
        Label(self.sidebar, text="Масштаб:", bg="dimgray", fg="white").pack(pady=(20, 5))
        self.zoom_slider = Scale(self.sidebar, from_=40, to=150, orient=HORIZONTAL,
                                 bg="dimgray", fg="white", troughcolor="#444",
                                 command=self.set_zoom)
        self.zoom_slider.set(self.grid_zoom)
        self.zoom_slider.pack(pady=5)

        # Панель навигации для сдвига графика
        nav_frame = Frame(self.sidebar, bg="gray")
        nav_frame.pack(pady=15)
        Button(nav_frame, text="↑", width=5, command=lambda: self.shift("up")).grid(row=0, column=1)
        Button(nav_frame, text="←", width=5, command=lambda: self.shift("left")).grid(row=1, column=0)
        Button(nav_frame, text="→", width=5, command=lambda: self.shift("right")).grid(row=1, column=2)
        Button(nav_frame, text="↓", width=5, command=lambda: self.shift("down")).grid(row=2, column=1)

        # Холст для рисования графика и свободного рисования
        self.canvas = Canvas(self.master, bg="dimgray")
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=True)

    def set_bindings(self):
        """
        Настройка обработчиков событий мыши для свободного рисования.
        """
        # Обработчики для начала и продолжения свободного рисования
        self.canvas.bind("<Button-1>", self.begin_draw)
        self.canvas.bind("<B1-Motion>", self.keep_drawing)

    def set_zoom(self, value):
        """
        Обновление масштаба сетки и перерисовка графика.

        Args:
            value: Новое значение масштаба из слайдера.
        """
        self.grid_zoom = int(value)
        self.render_graph()

    def toggle_drawing_mode(self):
        """
        Переключение режима свободного рисования (включение/выключение).
        """
        self.free_draw = not self.free_draw

    def begin_draw(self, event):
        """
        Метод вызывается при нажатии кнопки мыши: запоминает координаты первой точки,
        если включен режим свободного рисования.

        Args:
            event: Событие нажатия мыши с координатами event.x, event.y.
        """
        if self.free_draw:
            self.previous = (event.x, event.y)  # Запоминаем первую точку

    def keep_drawing(self, event):
        """
        Метод вызывается при перемещении мыши с зажатой кнопкой: рисует линию от предыдущей точки.

        Args:
            event: Событие движения мыши с координатами.
        """
        if self.free_draw and self.previous:
            x0, y0 = self.previous
            x1, y1 = event.x, event.y
            # Рисуем линию от предыдущей точки к текущей
            self.canvas.create_line(x0, y0, x1, y1, fill="red", width=2)
            self.previous = (x1, y1)

    def shift(self, direction):
        """
        Сдвигает центр координат в указанную сторону и перерисовывает график.

        Args:
            direction (str): "left", "right", "up" или "down".
        """
        delta = 25  # Количество пикселей смещения
        if direction == "left":
            self.shift_x += delta
        elif direction == "right":
            self.shift_x -= delta
        elif direction == "up":
            self.shift_y += delta
        elif direction == "down":
            self.shift_y -= delta
        self.render_graph()

    def render_graph(self):
        """
        Основной метод: очищает холст, рисует оси, сетку и график функции.
        """
        self.canvas.delete("all")  # Очищаем холст перед отрисовкой
        try:
            expr = self.input.get()  # Формула, введенная пользователем
            w = self.canvas.winfo_width()   # Текущая ширина холста
            h = self.canvas.winfo_height()  # Текущая высота холста
            cx, cy = w // 2 + self.shift_x, h // 2 + self.shift_y  # Координаты центра (0,0)

            # Рисуем оси X и Y
            self.canvas.create_line(0, cy, w, cy, fill="white")
            self.canvas.create_line(cx, 0, cx, h, fill="white")

            # Вертикальные линии сетки и подписи по X
            for i in range(0, w, self.grid_zoom):
                self.canvas.create_line(i, 0, i, h, fill="#303030")
                val = (i - cx) / self.grid_zoom  # Вычисляем значение X в математических координатах
                if abs(val) > 0.01:  # Пропускаем надпись в точке (0,0)
                    self.canvas.create_text(i, cy + 15, text=f"{val:.0f}", fill="white", font=("Courier", 8))

            # Горизонтальные линии сетки и подписи по Y
            for j in range(0, h, self.grid_zoom):
                self.canvas.create_line(0, j, w, j, fill="#303030")
                val = (cy - j) / self.grid_zoom  # Вычисляем значение Y в математических координатах
                if abs(val) > 0.01:
                    self.canvas.create_text(cx + 20, j, text=f"{val:.0f}", fill="white", font=("Courier", 8))

            # Рисуем график функции: перебираем каждый пиксель по X
            prev = None  # Хранит предыдущую выбранную точку (px, py)
            for px in range(w):
                x = (px - cx) / self.grid_zoom  # Преобразуем экранные координаты в математические
                try:
                    # Вычисляем y = f(x) с помощью eval и безопасного словаря
                    y = eval(expr, {"x": x, "math": math, **self.allowed})
                    py = cy - y * self.grid_zoom  # Преобразуем математическую Y в экранную
                    if prev:
                        # Рисуем линию от предыдущей точки к новой для плавного графика
                        self.canvas.create_line(prev[0], prev[1], px, py, fill="red")
                    prev = (px, py)  # Сохраняем текущую точку для следующей итерации
                except:
                    # При ошибке (например, деление на ноль) разрываем график
                    prev = None
        except Exception as e:
            # В случае общей ошибки выводим её в консоль
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    root = Tk()
    app = GraphApp(root)
    root.mainloop()
