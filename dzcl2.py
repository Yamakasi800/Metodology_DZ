#1)Создать класс с двумя переменными.
#Добавить метод вывода на экран и метод измене-ния этих переменных.
#Добавить метод, который находит сумму значений этих перемен-ных,
#и метод который находит наибольшее значение из этих двух переменных.

class MyClass:
    def __init__(self, x, y):
        """Инициализация класса с двумя переменными x и y."""
        self.x = x
        self.y = y

    def display(self):
        """Вывод значений переменных на экран."""
        print(f"Переменные: x = {self.x}, y = {self.y}")

    def update(self, new_x, new_y):
        """Изменение значений переменных."""
        self.x = new_x
        self.y = new_y

    def sum_values(self):
        """Вычисление суммы значений переменных."""
        return self.x + self.y

    def max_value(self):
        """Нахождение наибольшего из двух значений."""
        return max(self.x, self.y)


#2. Описать класс, реализующий десятичный счетчик, который может увеличивать или уменьшать свое значение на единицу в заданном диапазоне.
#Предусмот-реть инициализацию счетчика значениями по умолчанию и произвольными значения-ми.
#Счетчик имеет два метода: увеличения и уменьшения, — и свойство, позволяю-щее получить его текущее состояние.
#Написать программу, демонстрирующую все воз-можности класса.

class Counter:
    def __init__(self, min_value=0, max_value=100, start_value=None):
        """Инициализация счетчика.

        Аргументы:
        min_value (int) — минимальное значение счетчика.
        max_value (int) — максимальное значение счетчика.
        start_value (int) — начальное значение (если не задано, берется min_value).
        """
        self.min_value = min_value
        self.max_value = max_value
        self.value = start_value if start_value is not None else min_value

    def increase(self) -> None:
        """Увеличивает значение счетчика на 1, если не достигнут максимум."""
        if self.value < self.max_value:
            self.value += 1
        else:
            print("Достигнуто максимальное значение!")

    def decrease(self) -> None:
        """Уменьшает значение счетчика на 1, если не достигнут минимум."""
        if self.value > self.min_value:
            self.value -= 1
        else:
            print("Достигнуто минимальное значение!")

    def get_value(self) -> int:
        """Возвращает текущее значение счетчика."""
        return self.value

#3)Составить описание класса многочленов от одной переменной,
#задаваемых сте¬пенью многочлена и массивом коэффициентов.
#Предусмотреть методы для вы¬числения значения многочлена для заданного аргумента,
#операции сложения, вычитания и умножения мно-гочленов с получением нового объекта-многочлена.
class Polynomial:
    def __init__(self, coefficients):
        """Инициализация многочлена.

        Аргументы:
        coefficients (list) — список коэффициентов (от x^0 до x^n).
        """
        self.coefficients = coefficients  # Сохраняем коэффициенты

    def evaluate(self, x):
        """Вычисляет значение многочлена при заданном x.

        Аргументы:
        x (число) — значение, в котором нужно вычислить многочлен.

        Возвращает:
        число — результат вычисления.
        """
        result = 0
        for i in range(len(self.coefficients)):  # Проходим по коэффициентам
            result += self.coefficients[i] * (x ** i)  # Умножаем на x^i и суммируем
        return result

    def add(self, other):
        """Сложение двух многочленов.

        Аргументы:
        other (Polynomial) — другой многочлен.

        Возвращает:
        Polynomial — новый многочлен (сумма двух).
        """
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len  # Создаём список для новых коэффициентов

        # Складываем коэффициенты
        for i in range(len(self.coefficients)):
            new_coeffs[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            new_coeffs[i] += other.coefficients[i]

        return Polynomial(new_coeffs)

    def subtract(self, other):
        """Вычитание двух многочленов.

        Аргументы:
        other (Polynomial) — другой многочлен.

        Возвращает:
        Polynomial — новый многочлен (разность двух).
        """
        max_len = max(len(self.coefficients), len(other.coefficients))
        new_coeffs = [0] * max_len

        # Вычитаем коэффициенты
        for i in range(len(self.coefficients)):
            new_coeffs[i] += self.coefficients[i]
        for i in range(len(other.coefficients)):
            new_coeffs[i] -= other.coefficients[i]

        return Polynomial(new_coeffs)

    def multiply(self, other):
        """Умножение двух многочленов.

        Аргументы:
        other (Polynomial) — другой многочлен.

        Возвращает:
        Polynomial — новый многочлен (произведение двух).
        """
        new_coeffs = [0] * (len(self.coefficients) + len(other.coefficients) - 1)

        # Перемножаем коэффициенты
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                new_coeffs[i + j] += self.coefficients[i] * other.coefficients[j]

        return Polynomial(new_coeffs)

    def display(self):
        """Выводит многочлен в удобном виде."""
        terms = []
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:  # Пропускаем нулевые коэффициенты
                if i == 0:
                    terms.append(f"{self.coefficients[i]}")  # Просто число
                else:
                    terms.append(f"{self.coefficients[i]}x^{i}")  # Число с x^i
        print(" + ".join(terms) if terms else "0")  # Выводим многочлен


if "__main__" == __name__:
#Первое задание
    """
    obj = MyClass(10, 20)  # Создание объекта класса с начальными значениями 10 и 20
    obj.display()  # Вывод значений переменных
    print("Сумма:", obj.sum_values())  # Вывод суммы переменных
    print("Максимум:", obj.max_value())  # Вывод максимального значения

    obj.update(30, 15)  # Изменение значений переменных
    obj.display()  # Вывод новых значений
    print("Сумма после обновления:", obj.sum_values())  # Вывод суммы после обновления
    print("Максимум после обновления:", obj.max_value())  # Вывод максимума после обновления
    """
#Второе задание
    """
    counter = Counter(0, 10, 5)  # Создаем счетчик от 0 до 10, начальное значение 5
    
    print("Начальное значение:", counter.get_value())  # Вывод: 5

    counter.increase()
    print("После увеличения:", counter.get_value())  # Вывод: 6

    counter.decrease()
    counter.decrease()
    print("После двух уменьшений:", counter.get_value())  # Вывод: 4

    # Попытка выйти за границы диапазона
    for _ in range(10):
        counter.increase()
    print("После достижения максимума:", counter.get_value())  # Вывод: 10

    for _ in range(15):
        counter.decrease()
    print("После достижения минимума:", counter.get_value())  # Вывод: 0
    """    
#Третье задание
    """
    p1 = Polynomial([2, 3, 4])  # 2 + 3x + 4x^2
    p2 = Polynomial([1, -2, 1])  # 1 - 2x + x^2

    print("Многочлен 1:", end=" ")  
    p1.display()  # Вывод: 2 + 3x + 4x^2
    print("Многочлен 2:", end=" ")  
    p2.display()  # Вывод: 1 - 2x + x^2
    
    sum_poly = p1.add(p2)
    print("Сумма:", end=" ")  
    sum_poly.display()  # (2 + 3x + 4x^2) + (1 - 2x + x^2)
    
    diff_poly = p1.subtract(p2)
    print("Разность:", end=" ")  
    diff_poly.display()  # (2 + 3x + 4x^2) - (1 - 2x + x^2)
    
    prod_poly = p1.multiply(p2)
    print("Произведение:", end=" ")  
    prod_poly.display()  # (2 + 3x + 4x^2) * (1 - 2x + x^2)
    """
