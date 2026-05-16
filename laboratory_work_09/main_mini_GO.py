#!/usr/bin/env python3
import sys
import os

# Добавляем текущую директорию в путь для импорта
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from my_lexer import Lexer
from parser import Parser
from my_codegen import CodeGenerator


def main():
    # Пример программы на MiniGo
    text_input = """package main

func main() {
    print(4 + 4 - 2);
    print(10 * 2 / 4);
}"""

    print("=" * 70)
    print(" КОМПИЛЯТОР MINI GO")
    print("=" * 70)

    print("\nИсходный код:")
    print(text_input)

    print("\n" + "=" * 70)
    print("1. ЛЕКСИЧЕСКИЙ АНАЛИЗ")
    print("=" * 70)

    # Создаем лексер
    lexer_gen = Lexer()
    lexer = lexer_gen.get_lexer()

    # Токенизируем код
    tokens = list(lexer.lex(text_input))

    print(f"✓ Найдено токенов: {len(tokens)}")
    print("\nПримеры токенов:")
    for i, token in enumerate(tokens[:5]):
        print(f"  [{i:2d}] {token.gettokentype():15} '{token.getstr()}'")

    if len(tokens) > 5:
        print(f"  ... и еще {len(tokens) - 5} токенов")

    print("\n" + "=" * 70)
    print("2. СИНТАКСИЧЕСКИЙ АНАЛИЗ")
    print("=" * 70)

    # Создаем парсер
    parser_gen = Parser()
    parser = parser_gen.get_parser()

    try:
        # Парсим токены и получаем AST
        ast = parser.parse(iter(tokens))

        print("✓ Дерево AST успешно построено")
        print(f"  Тип корневого узла: {type(ast).__name__}")

        # Показываем структуру AST
        print("\n Структура AST:")


        print("\n" + "=" * 70)
        print("3. ВЫПОЛНЕНИЕ ПРОГРАММЫ (ИНТЕРПРЕТАЦИЯ)")
        print("=" * 70)

        print("Результат выполнения:")

        # Выполняем программу (интерпретация)
        ast.eval()

        print("\n" + "=" * 70)
        print("✓ ПРОГРАММА УСПЕШНО ВЫПОЛНЕНА (ИНТЕРПРЕТАТОР)")
        print("=" * 70)

        # ========== ДОБАВЛЕН КОДОГЕНЕРАТОР ==========
        print("\n" + "=" * 70)
        print("4. ГЕНЕРАЦИЯ КОДА И КОМПИЛЯЦИЯ")
        print("=" * 70)

        # Создаем кодогенератор
        codegen = CodeGenerator()

        # Генерируем LLVM IR код
        llvm_code, success = codegen.generate(ast, "minigo_program")

        if success:
            print("\n" + "=" * 70)
            print("✓ КОМПИЛЯЦИЯ ЗАВЕРШЕНА УСПЕШНО")
            print("=" * 70)

    except ValueError as e:
        print(f"✗ Ошибка синтаксического анализа: {e}")
    except ZeroDivisionError as e:
        print(f"✗ Ошибка выполнения: {e}")
    except Exception as e:
        print(f"✗ Неизвестная ошибка: {e}")
        import traceback
        traceback.print_exc()


def test_with_codegen():
    """Тест с полным циклом компиляции"""
    print("\n" + "=" * 70)
    print("ТЕСТ ПОЛНОГО ЦИКЛА КОМПИЛЯЦИИ")
    print("=" * 70)

    test_cases = [
        ("Простое сложение", "print(2 + 3);"),
        ("Арифметика", "print(2 + 3 * 4);"),
        ("Деление", "print(20 / 4);"),
        ("Комбинированное", "print((2 + 3) * (4 - 1));"),
    ]

    for test_name, test_code in test_cases:
        print(f"\n Тест: {test_name}")
        print(f"   Код: {test_code}")
        print("-" * 40)

        # Обертка кода в полную программу
        full_code = f"package main\nfunc main() {{\n    {test_code}\n}}"

        # Лексический анализ
        lexer_gen = Lexer()
        lexer = lexer_gen.get_lexer()
        tokens = list(lexer.lex(full_code))

        # Синтаксический анализ
        parser_gen = Parser()
        parser = parser_gen.get_parser()

        try:
            # Парсинг
            ast = parser.parse(iter(tokens))

            # Интерпретация
            print("   Интерпретация: ", end="")
            ast.eval()

            # Генерация кода
            codegen = CodeGenerator()
            llvm_code, success = codegen.generate(ast, f"test_{test_name.replace(' ', '_').lower()}")

            if success:
                print("    Кодогенерация: успешно")
            else:
                print("    Кодогенерация: ошибка")

        except Exception as e:
            print(f"    Ошибка: {e}")


def compile_file(filename):
    """Компилирует файл с исходным кодом"""
    if not os.path.exists(filename):
        print(f" Файл не найден: {filename}")
        return

    print(f"\n Компиляция файла: {filename}")
    print("=" * 70)

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            source_code = f.read()

        print("Исходный код:")
        print(source_code)

        # Лексический анализ
        lexer_gen = Lexer()
        lexer = lexer_gen.get_lexer()
        tokens = list(lexer.lex(source_code))

        print(f"\n✓ Токенов: {len(tokens)}")

        # Синтаксический анализ
        parser_gen = Parser()
        parser = parser_gen.get_parser()
        ast = parser.parse(iter(tokens))

        print("✓ AST построено")

        # Генерация кода
        codegen = CodeGenerator()
        base_name = os.path.splitext(os.path.basename(filename))[0]
        llvm_code, success = codegen.generate(ast, base_name)

        if success:
            print(f"\n Файл успешно скомпилирован!")
            print(f"   LLVM IR: output/{base_name}.ll")
            print(f"   Исполняемый файл: output/{base_name}")

    except Exception as e:
        print(f" Ошибка компиляции: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Компилятор MiniGo')
    parser.add_argument('file', nargs='?', help='Файл для компиляции')
    parser.add_argument('--test', action='store_true', help='Запустить тесты')

    args = parser.parse_args()

    if args.file:
        # Компилируем файл
        compile_file(args.file)
    elif args.test:
        # Запускаем тесты
        test_with_codegen()
    else:
        # Запускаем основной пример
        main()