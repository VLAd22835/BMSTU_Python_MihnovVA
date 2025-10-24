import random
import os


def generate_input_file(filename='input4.txt', count=10):
    """Создает файл со случайными числами если он не существует"""
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            for i in range(count):
                # Генерируем случайные числа от -10 до 10
                num = random.uniform(-10, 10)
                f.write(f"{num:.3f} ")
        print(f"Создан файл {filename} с {count} случайными числами")
    else:
        print(f"Файл {filename} уже существует")


def main():
    # Создаем файл input4.txt если его нет
    generate_input_file()

    # Чтение данных из файла
    with open('input4.txt', 'r') as f:
        # Читаем весь файл, разделяем по пробелам и преобразуем в float
        data = f.read().strip()
        # Разделяем строку по пробелам и фильтруем пустые строки
        arr = list(map(float, filter(None, data.split())))

    n = len(arr)

    print("Исходный массив:")
    for i in range(n):
        print(f"{arr[i]:8.3f}", end=" ")
    print()

    # 1. Сумма элементов с нечетными номерами
    sum_odd = 0.0
    for i in range(n):
        if i % 2 == 0:  # Индексы 0, 2, 4... (нечетные номера)
            sum_odd += arr[i]

    # 2. Сумма элементов между первым и последним отрицательными элементами
    # Находим индекс первого отрицательного элемента
    first_negative_index = -1
    for i in range(n):
        if arr[i] < 0:
            first_negative_index = i
            break

    # Находим индекс последнего отрицательного элемента
    last_negative_index = -1
    for i in range(n - 1, -1, -1):
        if arr[i] < 0:
            last_negative_index = i
            break

    sum_between_negatives = 0.0
    has_negatives = (first_negative_index != -1 and last_negative_index != -1)

    if has_negatives and first_negative_index != last_negative_index:
        start_index = min(first_negative_index, last_negative_index)
        end_index = max(first_negative_index, last_negative_index)

        for i in range(start_index + 1, end_index):
            sum_between_negatives += arr[i]
    else:
        sum_between_negatives = 0.0

    # 3. Сжать массив, удалив элементы с модулем <= 1
    compressed_arr = []
    for num in arr:
        if abs(num) > 1:
            compressed_arr.append(num)

    # Заполняем оставшиеся позиции нулями
    while len(compressed_arr) < n:
        compressed_arr.append(0.0)

    # Запись результатов в файл
    with open('output4.txt', 'w') as f:
        f.write(f"1. Сумма элементов с нечетными номерами: {sum_odd:.3f}\n")

        if has_negatives:
            f.write(
                f"2. Сумма элементов между первым и последним отрицательными элементами: {sum_between_negatives:.3f}\n")
        else:
            f.write("2. В массиве нет отрицательных элементов\n")

        f.write("3. Сжатый массив (элементы с |x| > 1, остальные заменены нулями):\n")
        for i in range(n):
            f.write(f"{compressed_arr[i]:8.3f} ")
        f.write("\n")

    # Вывод в консоль для проверки
    print("\nРезультаты:")
    print(f"1. Сумма элементов с нечетными номерами: {sum_odd:.3f}")

    if has_negatives:
        print(f"2. Сумма элементов между первым и последним отрицательными элементами: {sum_between_negatives:.3f}")
        print(f"   Первый отрицательный: arr[{first_negative_index}] = {arr[first_negative_index]:.3f}")
        print(f"   Последний отрицательный: arr[{last_negative_index}] = {arr[last_negative_index]:.3f}")
    else:
        print("2. В массиве нет отрицательных элементов")

    print("3. Сжатый массив (элементы с |x| > 1, остальные заменены нулями):")
    for i in range(n):
        print(f"{compressed_arr[i]:8.3f}", end=" ")
    print()

    print("\nDone! Результаты записаны в output4.txt")


if __name__ == "__main__":
    main()