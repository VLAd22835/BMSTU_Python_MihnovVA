"""
Модуль для работы с одномерными массивами (лабораторная работа №4)
"""
import random

__all__ = ['generate_array', 'sum_odd_indices', 'sum_between_negatives',
           'compress_array', 'main', 'ArrayProcessor']


class ArrayProcessor:
    """Класс для обработки массива"""

    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def sum_odd_indices(self):
        """Сумма элементов с нечетными номерами (индексы 0,2,4...)"""
        sum_odd = 0.0
        for i in range(self.n):
            if i % 2 == 0:
                sum_odd += self.arr[i]
        return sum_odd

    def sum_between_negatives(self):
        """Сумма элементов между первым и последним отрицательными элементами"""
        first_negative_index = -1
        last_negative_index = -1

        # Поиск первого отрицательного
        for i in range(self.n):
            if self.arr[i] < 0:
                first_negative_index = i
                break

        # Поиск последнего отрицательного
        for i in range(self.n - 1, -1, -1):
            if self.arr[i] < 0:
                last_negative_index = i
                break

        sum_between = 0.0
        has_negatives = (first_negative_index != -1 and last_negative_index != -1)

        if has_negatives and first_negative_index != last_negative_index:
            start = min(first_negative_index, last_negative_index)
            end = max(first_negative_index, last_negative_index)
            for i in range(start + 1, end):
                sum_between += self.arr[i]

        return sum_between, first_negative_index, last_negative_index, has_negatives

    def compress_array(self):
        """Сжатие массива: элементы с |x| > 1, остальные - нули"""
        compressed = [num for num in self.arr if abs(num) > 1]
        while len(compressed) < self.n:
            compressed.append(0.0)
        return compressed


def generate_array(n, min_val=-10, max_val=10):
    """Генерация массива из n случайных чисел"""
    return [random.uniform(min_val, max_val) for _ in range(n)]


def sum_odd_indices(arr):
    """Функция для суммы элементов с нечетными номерами"""
    processor = ArrayProcessor(arr)
    return processor.sum_odd_indices()


def sum_between_negatives(arr):
    """Функция для суммы между отрицательными элементами"""
    processor = ArrayProcessor(arr)
    return processor.sum_between_negatives()


def compress_array(arr):
    """Функция для сжатия массива"""
    processor = ArrayProcessor(arr)
    return processor.compress_array()


def main():
    """Основная функция программы"""
    try:
        n = int(input("Введите количество элементов массива (n): "))

        arr = generate_array(n)

        print("Исходный массив:")
        for i in range(n):
            print(f"{arr[i]:.3f}", end=" ")
        print()

        # Обработка
        processor = ArrayProcessor(arr)
        sum_odd = processor.sum_odd_indices()
        sum_between, first_idx, last_idx, has_neg = processor.sum_between_negatives()
        compressed = processor.compress_array()

        # Вывод результатов
        print("\nРезультаты:")
        print(f"1. Сумма элементов с нечетными номерами: {sum_odd:.3f}")

        if has_neg:
            print(f"2. Сумма элементов между первым и последним отрицательными: {sum_between:.3f}")
            print(f"   Первый отрицательный: arr[{first_idx}] = {arr[first_idx]:.3f}")
            print(f"   Последний отрицательный: arr[{last_idx}] = {arr[last_idx]:.3f}")
        else:
            print("2. В массиве нет отрицательных элементов")

        print("3. Сжатый массив (элементы с |x| > 1, остальные нули):")
        for i in range(n):
            print(f"{compressed[i]:.3f}", end=" ")
        print()

    except ValueError:
        print("Ошибка: введите корректное число")


if __name__ == "__main__":
    print("Программа запущена как основная")
    main()
else:
    print("Модуль lab4_arrays импортирован")