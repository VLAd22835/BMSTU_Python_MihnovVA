from my_lexer import Lexer
from parser import Parser


def main():
    # Упрощенный пример программы на MiniGo
    text_input = """
    package main

    func main() {
        print(4 + 4 - 2);
    }
    """

    print("Исходный код:")
    print(text_input)
    print("\nЛексический анализ:")

    # Создаем лексер и токенизируем код
    lexer = Lexer()
    tokens = lexer.tokenize(text_input)

    print("Токены:")
    for token in tokens:
        print(f"  {token}")

    print("\nСинтаксический анализ и выполнение:")

    # Создаем парсер и парсим токены
    parser = Parser()

    try:
        # Парсим и получаем AST
        ast = parser.parse(tokens)

        # Выполняем AST
        if ast:
            ast.eval()
    except Exception as e:
        print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()