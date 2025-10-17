from math import sqrt
import turtle as tr


def function(x):
    y = 0.0
    if x <= 0:
        y = -0.5 * x - 3
    elif 0 <= x < 3:
        y = -sqrt(9 - x ** 2)
    elif 3 <= x <= 6:
        y = sqrt(9 - (x - 6) ** 2)
    elif x > 6:
        y = None  # Графика нет после x = 6
    return y


def plot_axis(min_value, max_value, ax="X"):
    tr.up()
    if ax == "X":
        begin = (min_value, 0)
        end = (max_value, 0)
    else:
        begin = (0, min_value)
        end = (0, max_value)
    tr.goto(begin)
    tr.down()
    tr.goto(end)


def plot_mark(min_value, max_value, ax="X"):
    tr.up()
    for t in range(min_value, max_value + 1):
        if t == 0:  # Пропускаем 0, чтобы не дублировать с осями
            continue
        if ax == "X":
            point_begin = (t, 0)
            point_end = (t, 0.2)
            if t > 0:
                point_width = (t - 0.2, -0.5)
            else:
                point_width = (t - 0.3, -0.5)
        else:
            point_begin = (0, t)
            point_end = (0.2, t)
            if t > 0:
                point_width = (-0.7, t - 0.2)
            else:
                point_width = (-0.7, t - 0.3)
        tr.goto(point_begin)
        tr.down()
        tr.goto(point_end)
        tr.up()
        tr.goto(point_width)
        tr.write(str(t), font=("Arial", 10, "normal"))


def plot_arrow(max_value, ax="X"):
    triangle = [(0.1, -0.1), (0, 0.3), (-0.1, -0.1)]
    tr.up()
    tr.goto(0, 0)
    tr.begin_poly()
    for couple in triangle:
        tr.goto(couple)
    tr.end_poly()
    arrow = tr.get_poly()
    tr.register_shape("myArrow", arrow)
    tr.resizemode("myArrow")
    tr.shapesize(1, 2, 1)
    if ax == "X":
        tr.tiltangle(0)
        tr.goto(max_value + 0.2, 0)
        point_width = (max_value - 0.5, -1.0)
    else:
        tr.tiltangle(90)
        tr.goto(0, max_value + 0.2)
        point_width = (0.2, max_value - 0.5)
    tr.stamp()
    tr.goto(point_width)
    tr.write(ax, font=("Arial", 14, "bold"))


def plot_function(min_value, max_value, n_max=1000):
    tr.color("red")
    tr.width(2)
    dx = (max_value - min_value) / n_max

    x = min_value
    y = function(x)
    tr.up()
    tr.goto(x, y)
    tr.down()

    while x <= max_value:
        x = x + dx
        y = function(x)
        if y is None:  # Если графика нет, поднимаем перо
            tr.up()
            continue
        else:
            if not tr.isdown():
                tr.down()
            tr.goto(x, y)


if __name__ == "__main__":
    # Масштаб 1:1 - устанавливаем одинаковые физические размеры для единичных отрезков
    aX = (-10, 10)
    aY = (-5, 5)

    # Вычисляем размеры окна для масштаба 1:1
    # 20 единиц по X и 10 единиц по Y
    # Чтобы сохранить пропорции, берем одинаковый размер пикселя для обеих осей
    pixels_per_unit = 30  # 30 пикселей на одну единицу
    Dx = int((aX[1] - aX[0]) * pixels_per_unit)  # 20 * 30 = 600
    Dy = int((aY[1] - aY[0]) * pixels_per_unit)  # 10 * 30 = 300

    tr.setup(Dx, Dy)
    tr.reset()

    tr.setworldcoordinates(aX[0], aY[0], aX[1], aY[1])

    tr.title("График функции (масштаб 1:1)")
    tr.width(2)
    tr.color("black", "black")

    tr.ht()
    tr.tracer(0, 0)

    # Рисуем оси
    plot_axis(aX[0], aX[1], "X")
    plot_mark(aX[0], aX[1], "X")
    plot_arrow(aX[1], "X")

    plot_axis(aY[0], aY[1], "Y")
    plot_mark(aY[0], aY[1], "Y")
    plot_arrow(aY[1], "Y")

    # Рисуем функцию только до x = 6
    plot_function(-10, 6, 2000)

    tr.update()
    tr.mainloop()