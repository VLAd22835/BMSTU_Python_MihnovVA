"""
Лабораторная работа №7
Построение графика кусочно-заданной функции с использованием turtle
"""

import turtle as tr
from math import sqrt


class PiecewiseFunction:
    """
    Класс для представления кусочно-заданной функции
    Функция определена на интервале x ∈ [-∞, 6]
    """

    def __init__(self):
        """Инициализация функции"""
        pass

    def calculate(self, x):
        """
        Вычисляет значение функции в точке x

        Args:
            x: аргумент функции

        Returns:
            значение функции или None, если функция не определена
        """
        if x <= 0:
            return -0.5 * x - 3
        elif 0 <= x < 3:
            return -sqrt(9 - x ** 2)
        elif 3 <= x <= 6:
            return sqrt(9 - (x - 6) ** 2)
        else:  # x > 6
            return None

    def is_defined(self, x):
        """
        Проверяет, определена ли функция в точке x

        Args:
            x: аргумент функции

        Returns:
            True если функция определена, False в противном случае
        """
        return x <= 6


class CoordinateSystem:
    """Класс для управления координатной системой и масштабированием"""

    def __init__(self, x_min=-10, x_max=10, y_min=-5, y_max=5, pixels_per_unit=30):
        """
        Инициализация координатной системы

        Args:
            x_min: минимальное значение X
            x_max: максимальное значение X
            y_min: минимальное значение Y
            y_max: максимальное значение Y
            pixels_per_unit: количество пикселей на единицу (масштаб)
        """
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.pixels_per_unit = pixels_per_unit

        # Вычисляем размеры окна
        self.width = int((x_max - x_min) * pixels_per_unit)
        self.height = int((y_max - y_min) * pixels_per_unit)

    def setup_screen(self):
        """Настраивает экран turtle с правильными координатами"""
        tr.setup(self.width, self.height)
        tr.reset()
        tr.setworldcoordinates(self.x_min, self.y_min, self.x_max, self.y_max)
        tr.title("График кусочно-заданной функции")
        tr.tracer(0, 0)  # Отключаем анимацию для быстрой отрисовки

    def scale_point(self, x, y):
        """
        Преобразование математических координат в экранные

        Args:
            x: координата X в математической системе
            y: координата Y в математической системе

        Returns:
            кортеж (x_экран, y_экран)
        """
        # При использовании setworldcoordinates преобразование не требуется
        return (x, y)


class AxisDrawer:
    """Класс для рисования осей координат"""

    def __init__(self, turtle_obj, coord_system):
        """
        Инициализация рисовальщика осей

        Args:
            turtle_obj: объект turtle для рисования
            coord_system: объект координатной системы
        """
        self.turtle = turtle_obj
        self.coord_system = coord_system

    def draw_axes(self):
        """Рисует оси координат, стрелки и деления"""
        self.turtle.color("black", "black")
        self.turtle.width(2)
        self.turtle.ht()

        # Рисуем оси
        self._draw_x_axis()
        self._draw_y_axis()

        # Рисуем деления и подписи
        self._draw_ticks()

        # Рисуем стрелки
        self._draw_arrows()

    def _draw_x_axis(self):
        """Рисует ось X"""
        self.turtle.up()
        self.turtle.goto(self.coord_system.x_min, 0)
        self.turtle.down()
        self.turtle.goto(self.coord_system.x_max, 0)
        self.turtle.up()

    def _draw_y_axis(self):
        """Рисует ось Y"""
        self.turtle.up()
        self.turtle.goto(0, self.coord_system.y_min)
        self.turtle.down()
        self.turtle.goto(0, self.coord_system.y_max)
        self.turtle.up()

    def _draw_ticks(self):
        """Рисует деления на осях"""
        # Деления на оси X
        for t in range(int(self.coord_system.x_min), int(self.coord_system.x_max) + 1):
            if t != 0:  # Пропускаем 0, чтобы не дублировать с осями
                self._draw_x_tick(t)

        # Деления на оси Y
        for t in range(int(self.coord_system.y_min), int(self.coord_system.y_max) + 1):
            if t != 0:
                self._draw_y_tick(t)

    def _draw_x_tick(self, x_value):
        """Рисует деление на оси X"""
        self.turtle.up()
        self.turtle.goto(x_value, 0)
        self.turtle.down()
        self.turtle.goto(x_value, 0.2)
        self.turtle.up()

        # Подпись
        if x_value > 0:
            label_x = x_value - 0.2
        else:
            label_x = x_value - 0.3
        self.turtle.goto(label_x, -0.5)
        self.turtle.write(str(x_value), font=("Arial", 10, "normal"))

    def _draw_y_tick(self, y_value):
        """Рисует деление на оси Y"""
        self.turtle.up()
        self.turtle.goto(0, y_value)
        self.turtle.down()
        self.turtle.goto(0.2, y_value)
        self.turtle.up()

        # Подпись
        if y_value > 0:
            label_y = y_value - 0.2
        else:
            label_y = y_value - 0.3
        self.turtle.goto(-0.7, label_y)
        self.turtle.write(str(y_value), font=("Arial", 10, "normal"))

    def _draw_arrows(self):
        """Рисует стрелки на осях"""
        # Стрелка на оси X
        self.turtle.up()
        self.turtle.goto(self.coord_system.x_max, 0)
        self._draw_arrow(angle=0)
        self.turtle.goto(self.coord_system.x_max - 0.5, -1.0)
        self.turtle.write("X", font=("Arial", 14, "bold"))

        # Стрелка на оси Y
        self.turtle.up()
        self.turtle.goto(0, self.coord_system.y_max)
        self._draw_arrow(angle=90)
        self.turtle.goto(0.2, self.coord_system.y_max - 0.5)
        self.turtle.write("Y", font=("Arial", 14, "bold"))

    def _draw_arrow(self, angle=0):
        """Рисует стрелку в заданном направлении

        Args:
            angle: угол поворота стрелки (0 - вправо, 90 - вверх)
        """
        self.turtle.setheading(angle)
        self.turtle.down()
        self.turtle.forward(0.3)
        self.turtle.left(135)
        self.turtle.forward(0.2)
        self.turtle.backward(0.2)
        self.turtle.right(90)
        self.turtle.forward(0.2)
        self.turtle.up()
        self.turtle.setheading(0)


class FunctionPlotter:
    """Класс для построения графиков функций"""

    def __init__(self, turtle_obj, function):
        """
        Инициализация построителя графиков

        Args:
            turtle_obj: объект turtle для рисования
            function: объект функции с методом calculate()
        """
        self.turtle = turtle_obj
        self.function = function

    def plot(self, x_min, x_max, num_points=2000):
        """
        Строит график функции на заданном интервале

        Args:
            x_min: минимальное значение X
            x_max: максимальное значение X
            num_points: количество точек для построения
        """
        self.turtle.color("red")
        self.turtle.width(2)

        dx = (x_max - x_min) / num_points
        x = x_min

        # Находим первую точку, где функция определена
        while x <= x_max and not self.function.is_defined(x):
            x += dx

        if x > x_max:
            return  # Функция не определена на всем интервале

        # Перемещаемся в первую точку
        y = self.function.calculate(x)
        self.turtle.up()
        self.turtle.goto(x, y)
        self.turtle.down()

        # Рисуем график
        while x <= x_max:
            x += dx
            y = self.function.calculate(x)

            if y is None:
                # Если графика нет, поднимаем перо
                self.turtle.up()
            else:
                if not self.turtle.isdown():
                    self.turtle.down()
                self.turtle.goto(x, y)


class GraphApp:
    """Главный класс приложения"""

    def __init__(self):
        """Инициализация приложения"""
        # Параметры координатной системы
        self.x_min = -10
        self.x_max = 10
        self.y_min = -5
        self.y_max = 5
        self.pixels_per_unit = 30

        # Создание объектов
        self.coord_system = CoordinateSystem(
            self.x_min, self.x_max,
            self.y_min, self.y_max,
            self.pixels_per_unit
        )

        self.function = PiecewiseFunction()

        # Объекты для рисования (будут созданы в run)
        self.axes_turtle = None
        self.graph_turtle = None
        self.axis_drawer = None
        self.function_plotter = None

    def run(self):
        """Запускает приложение"""
        # Настройка экрана
        self.coord_system.setup_screen()

        # Создание объектов turtle
        self.axes_turtle = tr.Turtle()
        self.graph_turtle = tr.Turtle()

        # Создание вспомогательных объектов
        self.axis_drawer = AxisDrawer(self.axes_turtle, self.coord_system)
        self.function_plotter = FunctionPlotter(self.graph_turtle, self.function)

        # Рисование
        self.axis_drawer.draw_axes()
        self.function_plotter.plot(self.x_min, 6, 2000)  # Функция определена только до x=6

        # Завершение
        tr.update()
        tr.mainloop()


# Основная программа
if __name__ == "__main__":
    app = GraphApp()
    app.run()