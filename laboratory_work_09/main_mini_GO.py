from my_lexer import Lexer
from parser import Parser



def main():
    # Пример программы на MiniGo
    text_input = """package main

func main() {
    print(4 + 4 - 2);
    print(10 * 2 / 4);
}"""

    print("=" * 70)
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

    print(f"Найдено токенов: {len(tokens)}")
    print("\nСписок токенов:")
    for i, token in enumerate(tokens):
        print(f"  [{i:2d}] {token.gettokentype():15} '{token.getstr()}'")

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
        print(f"  Представление AST: {ast}")

        print("\n" + "=" * 70)
        print("3. ВЫПОЛНЕНИЕ ПРОГРАММЫ")
        print("=" * 70)

        print("Результат выполнения:")

        # Выполняем программу
        ast.eval()

        print("\n" + "=" * 70)
        print("✓ ПРОГРАММА УСПЕШНО ВЫПОЛНЕНА")
        print("=" * 70)
    except ValueError as e:
        print(f"✗ Ошибка синтаксического анализа: {e}")
    except ZeroDivisionError as e:
        print(f"✗ Ошибка выполнения: {e}")
    except Exception as e:
        print(f"✗ Неизвестная ошибка: {e}")
        import traceback
        traceback.print_exc()


def test_simple():
    """Тест простого выражения"""
    print("\n" + "=" * 70)
    print("ТЕСТ ПРОСТОГО ВЫРАЖЕНИЯ")
    print("=" * 70)

    test_code = "print(2 + 3 * 4);"

    lexer_gen = Lexer()
    lexer = lexer_gen.get_lexer()
    tokens = list(lexer.lex(test_code))

    parser_gen = Parser()
    parser = parser_gen.get_parser()

    # Добавляем обертку для теста
    full_code = f"package test\nfunc main() {{\n    {test_code}\n}}"
    tokens = list(lexer.lex(full_code))

    try:
        ast = parser.parse(iter(tokens))
        print(f"Исходный код: {test_code}")
        print(f"AST: {ast}")
        print("Результат:")
        ast.eval()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
    # test_simple()  # Раскомментируйте для дополнительного теста