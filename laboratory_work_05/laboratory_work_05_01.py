import numpy as np
import random


def process_matrix(matrix):
    matrix = np.array(matrix)
    n = matrix.shape[0]

    print("Исходная матрица:")
    print(matrix)
    print()

    # Задание 1: Произведение элементов в строках, которые не содержат отрицательных элементов
    print("1. Произведение элементов в строках без отрицательных элементов:")
    total_product = 1
    found_positive_rows = False

    for i in range(n):
        if all(matrix[i, j] >= 0 for j in range(n)):
            product = np.prod(matrix[i, :])
            total_product *= product  # Перемножаем произведения всех подходящих строк
            found_positive_rows = True
            print(f"Строка {i}: {matrix[i, :]} -> Произведение = {product}")
        else:
            print(f"Строка {i}: {matrix[i, :]} -> содержит отрицательные элементы")

    if found_positive_rows:
        print(f"Общее произведение строк без отрицательных элементов: {total_product}")
    else:
        total_product = 0  # Если нет строк без отрицательных элементов
        print("Нет строк без отрицательных элементов")

    print()

    # Задание 2: Максимум среди сумм элементов диагоналей, параллельных главной диагонали
    print("2. Максимум среди сумм элементов диагоналей, параллельных главной диагонали:")

    diagonal_sums = []

    # Диагонали выше главной
    for k in range(1, n):
        diagonal = np.diagonal(matrix, offset=k)
        diagonal_sum = np.sum(diagonal)
        diagonal_sums.append(diagonal_sum)
        print(f"Диагональ выше главной (смещение +{k}): {diagonal} -> Сумма = {diagonal_sum}")

    # Главная диагональ
    main_diagonal = np.diagonal(matrix, offset=0)
    main_sum = np.sum(main_diagonal)
    diagonal_sums.append(main_sum)
    print(f"Главная диагональ: {main_diagonal} -> Сумма = {main_sum}")

    # Диагонали ниже главной
    for k in range(1, n):
        diagonal = np.diagonal(matrix, offset=-k)
        diagonal_sum = np.sum(diagonal)
        diagonal_sums.append(diagonal_sum)
        print(f"Диагональ ниже главной (смещение -{k}): {diagonal} -> Сумма = {diagonal_sum}")

    max_sum = max(diagonal_sums)
    print(f"Максимальная сумма среди всех диагоналей: {max_sum}")

    return total_product, max_sum


def generate_random_matrix(size=4, min_val=-5, max_val=10):
    """Генерирует случайную квадратную матрицу"""
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix


# Основная программа
if __name__ == "__main__":
    print("=" * 60)
    print("ГЕНЕРАЦИЯ СЛУЧАЙНОЙ МАТРИЦЫ И ВЫПОЛНЕНИЕ ЗАДАНИЙ")
    print("=" * 60)

    try:
        # Ввод размера матрицы
        custom_size = int(input("Введите размер матрицы (например, 3, 4, 5): ") or "4")

        # Генерация случайной матрицы
        custom_matrix = generate_random_matrix(custom_size, -2, 6)

        print(f"\nСгенерированная матрица {custom_size}x{custom_size}:")
        for row in custom_matrix:
            print(row)
        print()

        # Выполнение заданий
        total_product, max_diagonal_sum = process_matrix(custom_matrix)

        print("\n" + "=" * 50)
        print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
        print(f"1. Произведение строк без отрицательных элементов: {total_product}")
        print(f"2. Максимальная сумма диагоналей: {max_diagonal_sum}")

    except ValueError:
        print("Ошибка: введите целое число для размера матрицы")