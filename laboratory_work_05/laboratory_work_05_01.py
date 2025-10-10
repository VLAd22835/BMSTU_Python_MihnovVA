import numpy as np


def process_matrix(matrix):
    """
    Обрабатывает квадратную матрицу согласно заданиям
    """
    matrix = np.array(matrix)
    n = matrix.shape[0]

    print("Исходная матрица:")
    print(matrix)
    print()

    # Задание 1: Произведение элементов в строках, которые не содержат отрицательных элементов
    print("1. Произведение элементов в строках без отрицательных элементов:")
    products = []
    for i in range(n):
        if all(matrix[i, j] >= 0 for j in range(n)):
            product = np.prod(matrix[i, :])
            products.append(product)
            print(f"Строка {i}: {matrix[i, :]} -> Произведение = {product}")
        else:
            print(f"Строка {i}: {matrix[i, :]} -> содержит отрицательные элементы")

    print(f"Результат задания 1: {products}")
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

    return products, max_sum


# Пример использования
if __name__ == "__main__":
    # Пример матрицы 4x4
    example_matrix = [
        [2, 1, 3, 4],
        [0, 5, -2, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 2]
    ]

    products, max_diagonal_sum = process_matrix(example_matrix)

    print("\n" + "=" * 50)
    print("Итоговые результаты:")
    print(f"1. Произведения строк без отрицательных элементов: {products}")
    print(f"2. Максимальная сумма диагоналей: {max_diagonal_sum}")