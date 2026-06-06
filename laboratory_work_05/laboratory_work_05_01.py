"""
Модуль для работы с матрицами (лабораторная работа №5)
"""
import numpy as np
import random

__all__ = ['MatrixProcessor', 'generate_random_matrix', 'process_matrix', 'main']


class MatrixProcessor:
    """Класс для обработки матриц"""

    def __init__(self, matrix):
        self.matrix = np.array(matrix)
        self.n = self.matrix.shape[0]

    def product_of_rows_without_negatives(self):
        """Произведение элементов в строках, которые не содержат отрицательных элементов"""
        total_product = 1
        found_positive_rows = False

        for i in range(self.n):
            if all(self.matrix[i, j] >= 0 for j in range(self.n)):
                product = np.prod(self.matrix[i, :])
                total_product *= product
                found_positive_rows = True

        return total_product if found_positive_rows else 0

    def max_sum_of_parallel_diagonals(self):
        """Максимум среди сумм элементов диагоналей, параллельных главной"""
        diagonal_sums = []

        # Диагонали выше главной
        for k in range(1, self.n):
            diagonal = np.diagonal(self.matrix, offset=k)
            diagonal_sums.append(np.sum(diagonal))

        # Главная диагональ
        diagonal_sums.append(np.sum(np.diagonal(self.matrix, offset=0)))

        # Диагонали ниже главной
        for k in range(1, self.n):
            diagonal = np.diagonal(self.matrix, offset=-k)
            diagonal_sums.append(np.sum(diagonal))

        return max(diagonal_sums)

    def get_detailed_info(self):
        """Получение подробной информации о всех диагоналях"""
        info = {
            'above': [],
            'main': [],
            'below': []
        }

        for k in range(1, self.n):
            diag = np.diagonal(self.matrix, offset=k)
            info['above'].append({'offset': k, 'values': diag, 'sum': np.sum(diag)})

        info['main'] = {'values': np.diagonal(self.matrix, offset=0),
                        'sum': np.sum(np.diagonal(self.matrix, offset=0))}

        for k in range(1, self.n):
            diag = np.diagonal(self.matrix, offset=-k)
            info['below'].append({'offset': k, 'values': diag, 'sum': np.sum(diag)})

        return info


def generate_random_matrix(size=4, min_val=-5, max_val=10):
    """Генерация случайной квадратной матрицы"""
    return [[random.randint(min_val, max_val) for _ in range(size)] for _ in range(size)]


def process_matrix(matrix):
    """Функция для обработки матрицы"""
    processor = MatrixProcessor(matrix)
    total_product = processor.product_of_rows_without_negatives()
    max_diagonal_sum = processor.max_sum_of_parallel_diagonals()
    return total_product, max_diagonal_sum


def main():
    """Основная функция программы"""
    print("=" * 60)
    print("ГЕНЕРАЦИЯ СЛУЧАЙНОЙ МАТРИЦЫ И ВЫПОЛНЕНИЕ ЗАДАНИЙ")
    print("=" * 60)

    try:
        custom_size = int(input("Введите размер матрицы (например, 3, 4, 5): "))

        custom_matrix = generate_random_matrix(custom_size, -2, 6)

        print(f"\nСгенерированная матрица {custom_size}x{custom_size}:")
        for row in custom_matrix:
            print(row)
        print()

        total_product, max_diagonal_sum = process_matrix(custom_matrix)

        processor = MatrixProcessor(custom_matrix)
        info = processor.get_detailed_info()

        print("\nДетальный анализ диагоналей:")
        print("Диагонали выше главной:")
        for diag in info['above']:
            print(f"  Смещение +{diag['offset']}: {diag['values']} -> Сумма = {diag['sum']:.2f}")

        print(f"Главная диагональ: {info['main']['values']} -> Сумма = {info['main']['sum']:.2f}")

        print("Диагонали ниже главной:")
        for diag in info['below']:
            print(f"  Смещение -{diag['offset']}: {diag['values']} -> Сумма = {diag['sum']:.2f}")

        print("\n" + "=" * 50)
        print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ:")
        print(f"1. Произведение строк без отрицательных элементов: {total_product}")
        print(f"2. Максимальная сумма диагоналей: {max_diagonal_sum:.2f}")

    except ValueError:
        print("Ошибка: введите целое число для размера матрицы")
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    print("Программа запущена как основная")
    main()
else:
    print("Модуль lab5_matrices импортирован")