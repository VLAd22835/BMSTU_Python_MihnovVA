from math import *


def taylor_ln1_plus_x(x, epsilon=1e-6):

    if x <= -1 or x > 1:
        return None, 0

    n = 0
    term = x  # первый член ряда: x
    total = term
    terms_count = 1

    while abs(term) > epsilon:
        n += 1
        term = ((-1) ** n) * (x ** (n + 1)) / (n + 1)
        total += term
        terms_count += 1

        # Защита от бесконечного цикла
        if terms_count > 1000:
            break

    return total, terms_count


def main():
    # Ввод параметров
    print("Вычисление функции ln(1+x) с помощью ряда Тейлора")
    print("Ряд: ln(1+x) = x - x²/2 + x³/3 - x⁴/4 + ... для -1 < x ≤ 1")
    print()

    try:
        x_start = float(input("Введите начальное значение X (Xнач): "))
        x_end = float(input("Введите конечное значение X (Хкон): "))
        dx = float(input("Введите шаг dx: "))
        epsilon = float(input("Введите точность ε: "))
    except ValueError:
        print("Ошибка: введите числовые значения")
        return

    # Проверка корректности ввода
    if dx <= 0:
        print("Ошибка: шаг dx должен быть положительным")
        return

    if epsilon <= 0:
        print("Ошибка: точность ε должна быть положительной")
        return

    # Вывод заголовка таблицы
    print("\n" + "=" * 65)
    print(f"Таблица значений функции ln(1+x)")
    print("Вычислено с помощью ряда Тейлора")
    print("=" * 65)
    print(f"{'Аргумент (x)':^15} {'ln(1+x) (ряд)':^18} {'ln(1+x) (math)':^18} {'Членов ряда':^12}")
    print("-" * 65)

    # Вычисление и вывод значений
    x = x_start
    while x <= x_end:
        # Вычисление через ряд Тейлора
        taylor_result, terms_count = taylor_ln1_plus_x(x, epsilon)

        # Вычисление через встроенную функцию для сравнения
        math_result = math.log1p(x)  # math.log1p(x) = ln(1+x)

        if taylor_result is not None:
            print(f"{x:^15.4f} {taylor_result:^18.6f} {math_result:^18.6f} {terms_count:^12}")
        else:
            print(f"{x:^15.4f} {'вне ОДЗ':^18} {math_result:^18.6f} {'-':^12}")

        x += dx

    print("=" * 65)


if __name__ == "__main__":
    main()