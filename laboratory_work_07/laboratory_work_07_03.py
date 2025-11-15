import turtle
import random
import math


def setup_screen():
    screen = turtle.Screen()
    screen.setup(1000, 800)
    screen.title("Монте-Карло: Площадь фигуры")
    screen.bgcolor("white")
    screen.tracer(0, 0)
    return screen


def draw_axes(t, R):
    """Рисование осей"""
    scale = 25

    t.penup()
    t.goto(-R * scale - 20, 0)
    t.pendown()
    t.goto(R * scale + 20, 0)

    t.penup()
    t.goto(0, -R * scale - 20)
    t.pendown()
    t.goto(0, R * scale + 20)

    t.penup()


def draw_figure(t, R):
    """Рисование фигуры"""
    scale = 25

    t.pensize(2)
    t.color("black")

    # Полукруг (не входит в фигуру)
    t.penup()
    t.goto(-R * scale, 0)
    t.pendown()
    for angle in range(0, 181):
        x = R * math.cos(math.radians(angle))
        y = R * math.sin(math.radians(angle))
        t.goto(x * scale, y * scale)

    # Треугольник (не входит в фигуру)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.goto(-R * scale, -R * scale)
    t.goto(0, -R * scale)
    t.goto(0, 0)

    t.penup()


def is_point_in_figure(x, y, R):
    """Проверка попадания точки в фигуру"""
    if x ** 2 + y ** 2 <= R ** 2 and y >= 0 and -R <= x <= R:
        return False
    elif -R <= x <= 0 and y <= x and -R <= y <= 0:
        return False
    else:
        return True


def monte_carlo(R, N):
    """Метод Монте-Карло с быстрой отрисовкой"""
    scale = 25
    points_inside = 0

    # Создаем черепашки для разных цветов точек
    hit_turtle = turtle.Turtle()  # Для попаданий (внутри фигуры)
    miss_turtle = turtle.Turtle()  # Для промахов (вне фигуры)

    for t in [hit_turtle, miss_turtle]:
        t.hideturtle()
        t.speed(0)
        t.penup()

    # Назначаем цвета
    hit_turtle.color("blue")  # Точки внутри фигуры - синие
    miss_turtle.color("red")  # Точки вне фигуры - красные

    # Основной цикл генерации точек
    for i in range(N):
        x = random.uniform(-R, R)
        y = random.uniform(-R, R)

        if is_point_in_figure(x, y, R):
            points_inside += 1
            current_turtle = hit_turtle  # Синяя точка
        else:
            current_turtle = miss_turtle  # Красная точка

        # Быстрая отрисовка точки
        current_turtle.goto(x * scale, y * scale)
        current_turtle.dot(3)

    # Вычисляем результаты
    rect_area = 4 * R * R
    estimated_area = (rect_area * points_inside) / N
    exact_area = rect_area - (math.pi * R ** 2) / 2 - (R * R) / 2

    return estimated_area, exact_area, points_inside


def show_results(R, estimated, exact, points, N):
    """Отображение результатов справа от графика"""
    scale = 25
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # Позиция для текста - справа от графика
    text_x = R * scale + 50

    t.goto(text_x, R * scale + 40)
    t.color("black")
    t.write("РЕЗУЛЬТАТЫ", font=("Arial", 14, "bold"))

    t.goto(text_x, R * scale + 10)
    t.write(f"Параметры:", font=("Arial", 10, "bold"))
    t.goto(text_x, R * scale - 10)
    t.write(f"  R = {R}", font=("Arial", 10))
    t.goto(text_x, R * scale - 30)
    t.write(f"  Всего точек: {N}", font=("Arial", 10))
    t.goto(text_x, R * scale - 50)
    t.write(f"  Внутри фигуры: {points}", font=("Arial", 10))
    t.goto(text_x, R * scale - 70)
    t.write(f"  Доля: {points / N * 100:.1f}%", font=("Arial", 10))

    t.goto(text_x, R * scale - 100)
    t.write(f"Площадь:", font=("Arial", 10, "bold"))
    t.goto(text_x, R * scale - 120)
    t.write(f"  Точная: {exact:.4f}", font=("Arial", 10))
    t.goto(text_x, R * scale - 140)
    t.write(f"  Монте-Карло: {estimated:.4f}", font=("Arial", 10))

    t.goto(text_x, R * scale - 170)
    t.write(f"Погрешность:", font=("Arial", 10, "bold"))
    t.goto(text_x, R * scale - 190)
    t.write(f"  Абсолютная: {abs(exact - estimated):.4f}", font=("Arial", 10))
    t.goto(text_x, R * scale - 210)
    t.write(f"  Относительная: {abs(exact - estimated) / exact * 100:.2f}%",
            font=("Arial", 10))


def show_legend(R):
    """Отображение легенды внизу"""
    scale = 25
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.penup()

    # Легенда внизу
    t.goto(-R * scale, -R * scale - 60)
    t.color("black")
    t.write("ЛЕГЕНДА:", font=("Arial", 10, "bold"))

    t.goto(-R * scale, -R * scale - 80)
    t.color("blue")
    t.write("● - точки ВНУТРИ фигуры (попадания)", font=("Arial", 9))

    t.goto(-R * scale, -R * scale - 100)
    t.color("red")
    t.write("● - точки ВНЕ фигуры (промахи)", font=("Arial", 9))

    t.goto(-R * scale, -R * scale - 120)
    t.color("black")
    t.write("▬ - границы вычитаемых областей", font=("Arial", 9))
    t.goto(-R * scale, -R * scale - 140)
    t.write("   (полукруг и треугольник)", font=("Arial", 9))


def main():
    """Основная функция"""
    R = 4  # Радиус
    N = 3000  # Количество точек

    print("=" * 50)
    print("МЕТОД МОНТЕ-КАРЛО ДЛЯ ВЫЧИСЛЕНИЯ ПЛОЩАДИ")
    print("=" * 50)
    print(f"Параметры: R = {R}, N = {N}")
    print("Запуск симуляции...")

    # Настройка экрана
    screen = setup_screen()

    # Создаем основную черепашку для осей и фигуры
    main_turtle = turtle.Turtle()
    main_turtle.hideturtle()
    main_turtle.speed(0)

    # Рисуем основу
    draw_axes(main_turtle, R)
    draw_figure(main_turtle, R)

    # Запускаем Монте-Карло
    estimated, exact, points = monte_carlo(R, N)

    # Показываем результаты
    show_results(R, estimated, exact, points, N)
    show_legend(R)

    # Обновляем экран
    turtle.update()

    # Вывод в консоль
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)
    print(f"Точная площадь: {exact:.4f}")
    print(f"Оценка Монте-Карло: {estimated:.4f}")
    print(f"Абсолютная погрешность: {abs(exact - estimated):.4f}")
    print(f"Относительная погрешность: {abs(exact - estimated) / exact * 100:.2f}%")
    print(f"Точек внутри фигуры: {points} из {N} ({points / N * 100:.1f}%)")
    print("\nЗакройте окно для выхода...")

    turtle.done()


if __name__ == "__main__":
    main()