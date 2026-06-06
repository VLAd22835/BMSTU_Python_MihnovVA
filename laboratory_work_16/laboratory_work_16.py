#!/usr/bin/env python3
"""
Лабораторная работа №16 — Регулярные выражения
Задание: найти в тексте различные паттерны (даты, время, числа, слова и т.д.)
"""

import re


def read_text_from_file(filename: str) -> str:
    """Читает текст из файла"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Ошибка: файл {filename} не найден!")
        return ""
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return ""


def task1_dates(text: str) -> list:
    """
    1. Даты в формате дд.мм.гг или дд.мм.гггг
    Примеры: 04.04.26, 04.04.2026
    """
    pattern = r'\b\d{2}\.\d{2}\.\d{2,4}\b'
    return re.findall(pattern, text)


def task2_times(text: str) -> list:
    """
    2. Время в формате чч.мм или чч:мм
    Примеры: 11:25, 11.25
    """
    pattern = r'\b\d{2}[.:]\d{2}\b'
    return re.findall(pattern, text)


def task3_integers(text: str) -> list:
    """
    3. Целые числа (со знаком и без)
    Примеры: 42, -17, +100
    """
    pattern = r'\b[+-]?\d+\b'
    return re.findall(pattern, text)


def task4_floats(text: str) -> list:
    """
    4. Вещественные числа (со знаком и без, с дробной частью и без, с целой частью и без)
    Примеры: 3.14, -0.5, .75, 42., +12.34
    """
    # Этот шаблон находит: целая часть (опционально), точка, дробная часть (опционально)
    # А также числа без целой части (.5) и без дробной (42.)
    pattern = r'[+-]?(?:\d+\.\d*|\.\d+|\d+\.?)'
    # Фильтруем, чтобы не захватить просто точки или лишнее
    matches = re.findall(pattern, text)
    # Очищаем от пустых и одиночных точек
    return [m for m in matches if m not in ['.', '+.', '-.', '+', '-'] and m.count('.') <= 1]


def task5_natural_numbers(text: str) -> list:
    """
    5. Натуральные числа (возможно, окружённые буквами)
    """
    pattern = r'\b\d+\b'
    return re.findall(pattern, text)


def task6_uppercase_words(text: str) -> list:
    """
    6. Слова, написанные капсом (строго заглавные), возможно внутри слов
    Пример: аааБББВВВ -> найдёт БББВВВ (но не ааа, так как они строчные)
    """
    # Ищем последовательности заглавных букв (латиница и кириллица)
    pattern = r'[A-ZА-ЯЁ]+'
    return re.findall(pattern, text)


def task7_russian_letter_then_digit(text: str) -> list:
    """
    7. Слова, в которых есть русская буква, а когда-нибудь за ней цифра
    """
    # Слово = последовательность букв/цифр, внутри есть русская буква и после неё (где-то) цифра
    pattern = r'\b[а-яА-ЯЁё0-9]*[а-яА-ЯЁё][а-яА-ЯЁё0-9]*\d[а-яА-ЯЁё0-9]*\b'
    return re.findall(pattern, text, re.IGNORECASE)


def task8_start_with_capital(text: str) -> list:
    """
    8. Слова, начинающиеся с русской или латинской большой буквы
    """
    pattern = r'\b[А-ЯЁA-Z][а-яА-ЯЁёa-zA-Z0-9]*\b'
    return re.findall(pattern, text)


def task9_start_with_vowel(text: str) -> list:
    """
    9. Слова, которые начинаются на гласную (русскую или латинскую)
    Гласные: а, е, ё, и, о, у, ы, э, ю, я и a, e, i, o, u, y
    """
    vowels = r'[аеёиоуыэюяaeyuio]'
    pattern = rf'\b{vowels}[а-яА-ЯЁёa-zA-Z]*\b'
    return re.findall(pattern, text, re.IGNORECASE)


def display_results(results: dict) -> None:
    """Красивый вывод результатов"""
    print("=" * 70)
    print("РЕЗУЛЬТАТЫ ПРОВЕРКИ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ")
    print("=" * 70)

    tasks = [
        ("1. Даты (дд.мм.гг или дд.мм.гггг)", task1_dates),
        ("2. Время (чч.мм или чч:мм)", task2_times),
        ("3. Целые числа (со знаком и без)", task3_integers),
        ("4. Вещественные числа", task4_floats),
        ("5. Натуральные числа", task5_natural_numbers),
        ("6. Слова заглавными буквами", task6_uppercase_words),
        ("7. Русская буква + где-то цифра", task7_russian_letter_then_digit),
        ("8. Начинаются с большой буквы (рус/лат)", task8_start_with_capital),
        ("9. Начинаются на гласную", task9_start_with_vowel),
    ]

    for title, func in tasks:
        print(f"\n{title}")
        print("-" * 50)
        found = func(results["text"])
        if found:
            for i, item in enumerate(found[:20], 1):  # показываем не более 20
                print(f"   {i}. {item}")
            if len(found) > 20:
                print(f"   ... и ещё {len(found) - 20}")
            print(f"   Всего найдено: {len(found)}")
        else:
            print("   Ничего не найдено")


def main():
    """Основная функция"""
    # Тестовый текст — можешь заменить на свой файл
    test_text = """
    Вот пример текста для проверки:
    Дата: 04.04.2026, а также 04.04.26 и 04.04.99.
    Время: 11:25, 23.59, а вот 25:70 — неправильное.
    Целые числа: 42, -17, +100, 0, -0, 12345.
    Вещественные: 3.14, -0.5, .75, 42., +12.34, 0.0, -3.1415.
    Натуральные числа: 15, 7, 999, abc123def.
    Слова капсом: ПРИВЕТ, WORLD, аааБББВВВ, ТЕСТ.
    Русская буква и цифра: а1, b2, слово3, test4, яблоко5.
    С большой буквы: Привет, World, Тест, Apple, Ёжик.
    На гласную: apple, яблоко, енот, Апельсин, Orange, утка.
    """

    print("Чтение текста...")
    # Если хочешь читать из файла — раскомментируй следующую строку:
    test_text = read_text_from_file("my_text")
    # Если файла нет — используем встроенный тестовый текст

    if not test_text:
        print("Нет текста для обработки.")
        return

    print(f"Текст получен, длина: {len(test_text)} символов\n")

    results = {"text": test_text}
    display_results(results)


if __name__ == "__main__":
    main()