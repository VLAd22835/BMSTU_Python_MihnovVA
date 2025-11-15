import math
import turtle


def taylor_ln1px(x, n_terms):
    """Вычисление ln(1+x) с помощью ряда Тейлора"""
    if abs(x) >= 1:
        return None
    sum_series = 0
    for n in range(1, n_terms + 1):
        term = ((-1) ** (n + 1)) * (x ** n) / n
        sum_series += term
    return sum_series


def setup_screen():
    """Настройка экрана turtle"""
    screen = turtle.Screen()
    screen.setup(1000, 700)
    screen.title("Ряд Тейлора для ln(1+x)")
    screen.bgcolor("white")
    return screen


def draw_axes(t):
    """Рисование осей координат"""
    t.speed(0)
    t.penup()

    # Ось X
    t.goto(-300, 0)
    t.pendown()
    t.goto(300, 0)
    t.penup()

    # Ось Y
    t.goto(0, -200)
    t.pendown()
    t.goto(0, 200)
    t.penup()

    # Разметка оси X
    for x in range(-8, 9, 2):
        t.goto(x * 40, -10)
        t.pendown()
        t.goto(x * 40, 10)
        t.penup()
        t.goto(x * 40 - 10, -25)
        t.write(f"{x / 10:.1f}", font=("Arial", 8))

    # Разметка оси Y
    for y in range(-5, 6):
        t.goto(-10, y * 40)
        t.pendown()
        t.goto(10, y * 40)
        t.penup()
        if y != 0:
            t.goto(-30, y * 40 - 5)
            t.write(f"{y}", font=("Arial", 8))

    # Подписи осей
    t.goto(280, -30)
    t.write("x", font=("Arial", 12))
    t.goto(-20, 180)
    t.write("y", font=("Arial", 12))


def draw_exact_function(t):
    """Рисование точной функции ln(1+x)"""
    t.penup()
    t.color("blue")
    t.pensize(2)

    for x in range(-90, 90):
        x_val = x / 100
        try:
            y_val = math.log(1 + x_val)
            if abs(y_val) < 5:
                t.goto(x_val * 100, y_val * 40)
                t.pendown()
        except:
            continue

    t.penup()
    t.goto(100, 150)
    t.write("ln(1+x)", font=("Arial", 12, "bold"), align="left")


def draw_taylor_approximation(t, n_terms):
    """Рисование приближения рядом Тейлора"""
    t.penup()
    t.color("red")
    t.pensize(1)

    for x in range(-90, 90):
        x_val = x / 100
        y_val = taylor_ln1px(x_val, n_terms)
        if y_val is not None and abs(y_val) < 5:
            t.goto(x_val * 100, y_val * 40)
            t.pendown()

    t.penup()
    t.goto(100, 130)
    t.write(f"Ряд Тейлора (n={n_terms})", font=("Arial", 10), align="left")


def show_convergence(t, x_point, max_terms=10):
    """Показать сходимость в одной точке"""
    exact_y = math.log(1 + x_point)

    # Линия точного значения
    t.penup()
    t.color("green")
    t.goto(-300, exact_y * 40)
    t.pendown()
    t.goto(300, exact_y * 40)
    t.penup()

    # Точка на оси X
    t.goto(x_point * 100, -15)
    t.pendown()
    t.goto(x_point * 100, 15)
    t.penup()

    # Анимация сходимости
    t.color("orange")
    sum_series = 0

    for n in range(1, max_terms + 1):
        term = ((-1) ** (n + 1)) * (x_point ** n) / n
        sum_series += term

        t.goto(x_point * 100, sum_series * 40)
        t.dot(8)

        # Соединяем точки
        if n < max_terms:
            t.pendown()
            next_term = ((-1) ** (n + 2)) * (x_point ** (n + 1)) / (n + 1)
            next_sum = sum_series + next_term
            t.goto(x_point * 100, next_sum * 40)
            t.penup()

    # Вывод информации
    error = abs(exact_y - sum_series)
    t.goto(-280, 180)
    t.color("black")
    t.write(f"Для x = {x_point:.2f}:", font=("Arial", 10))
    t.goto(-280, 160)
    t.write(f"Точное: {exact_y:.6f}", font=("Arial", 10))
    t.goto(-280, 140)
    t.write(f"Приближение: {sum_series:.6f}", font=("Arial", 10))
    t.goto(-280, 120)
    t.write(f"Погрешность: {error:.6f}", font=("Arial", 10))
    t.goto(-280, 100)
    t.write(f"Членов ряда: {max_terms}", font=("Arial", 10))


def main():
    """Основная функция"""
    # Настройка
    screen = setup_screen()
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    # Параметры визуализации
    n_terms = 7  # Количество членов ряда
    x_point = 0.6  # Точка для демонстрации сходимости

    print("=" * 50)
    print("Визуализация ряда Тейлора для ln(1+x)")
    print("=" * 50)
    print("График строится в окне turtle...")
    print("Синий график - точная функция ln(1+x)")
    print(f"Красный график - ряд Тейлора ({n_terms} членов)")
    print(f"Зеленая линия - точное значение в точке x={x_point}")
    print("Оранжевые точки - последовательные приближения")
    print("\nЗакройте окно turtle для выхода")

    # Рисование
    draw_axes(t)
    draw_exact_function(t)
    draw_taylor_approximation(t, n_terms)
    show_convergence(t, x_point)

    # Легенда
    t.goto(-280, -180)
    t.write("Сравнение ряда Тейлора с точной функцией", font=("Arial", 12, "bold"))

    # Удерживаем окно открытым
    turtle.done()


if __name__ == "__main__":
    main()