from my_lexer import Lexer, Token
from parser import Parser
from my_ast import Package


def main():
    # Пример программы на MiniGo
    code = """package main
func main() {
    print(4 + 4 - 2);
}"""

    print("=" * 60)
    print("=" * 60)
    print("\nИсходный код:")
    print(code)

    print("\n" + "=" * 60)
    print("1. ЛЕКСИЧЕСКИЙ АНАЛИЗ (my_lexer.py)")
    print("=" * 60)

    # Используем Lexer из my_lexer.py
    lexer = Lexer()
    tokens = lexer.tokenize(code)

    print("Найдено токенов:", len(tokens))
    print("\nСписок токенов:")
    for i, token in enumerate(tokens):
        print(f"  [{i:2d}] {token}")

    print("\n" + "=" * 60)
    print("2. СИНТАКСИЧЕСКИЙ АНАЛИЗ (parser.py)")
    print("=" * 60)

    # Используем Parser из parser.py
    parser = Parser()

    try:
        # Парсер зависит от my_ast.py (импортирует оттуда классы)
        ast = parser.parse(tokens)

        if isinstance(ast, Package):
            print("✓ Дерево AST успешно построено")
            print(f"  Тип: {type(ast).__name__}")
            print(f"  Имя пакета: {ast.name}")
            print(f"  Количество функций: {len(ast.functions)}")
        else:
            print("✗ Ошибка: ожидался узел Package")
            return

        print("\n" + "=" * 60)
        print("3. ВЫПОЛНЕНИЕ ПРОГРАММЫ")
        print("=" * 60)

        # Выполнение (метод eval() определен в my_ast.py)
        print("Результат выполнения:")
        ast.eval()

        print("\n" + "=" * 60)
        print("✓ ПРОГРАММА УСПЕШНО ВЫПОЛНЕНА")
        print("=" * 60)
    except SyntaxError as e:
        print(f"✗ Ошибка синтаксического анализа: {e}")
    except Exception as e:
        print(f"✗ Ошибка выполнения: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()