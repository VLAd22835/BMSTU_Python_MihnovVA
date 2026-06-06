"""
Модуль для тригонометрических вычислений (лабораторная работа №1)
"""
from math import cos, sin, tan

__all__ = ['calculate_z1_z2', 'main']


def calculate_z1_z2(alfa):
    """
    Вычисляет значения z1 и z2 по заданным формулам
    """
    z1 = 2 * cos(alfa) * sin(2 * alfa) - sin(alfa) / cos(alfa) - 2 * sin(alfa) * sin(2 * alfa)
    z2 = tan(3 * alfa)
    return z1, z2


def main():
    """
    Основная функция для запуска программы
    """
    try:
        alfa = float(input("Введите значение альфа (в радианах): "))
        z1, z2 = calculate_z1_z2(alfa)

        print("Вы дали значение альфа: {0:.2f}".format(alfa))
        print("Вы получили z1: {0:.2f}".format(z1))
        print("Вы получили z2: {0:.2f}".format(z2))
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    print("Программа запущена как основная")
    main()
else:
    print("Модуль lab1_trigonometry импортирован")