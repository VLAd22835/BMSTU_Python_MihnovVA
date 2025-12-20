"""
Компилятор MiniGo - полная версия в одном файле
"""

import re


# ==================== ТОКЕНЫ ====================
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, '{self.value}')"

    def __repr__(self):
        return self.__str__()


# ==================== AST КЛАССЫ ====================
class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp:
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub(BinaryOp):
    def eval(self):
        return self.left.eval() - self.right.eval()


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        result = self.value.eval()
        print(result)
        return result


class Block:
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        for statement in self.statements:
            statement.eval()


class Function:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def eval(self):
        return self.body.eval()


class Package:
    def __init__(self, name, functions):
        self.name = name
        self.functions = functions

    def eval(self):
        for func in self.functions:
            func.eval()


# ==================== ЛЕКСЕР ====================
class Lexer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, text):
        # Удаляем лишние пробелы в начале/конце
        text = text.strip()

        # Паттерны для токенов
        patterns = [
            (r'package\b', 'PACKAGE'),
            (r'func\b', 'FUNC'),
            (r'print\b', 'PRINT'),
            (r'\d+', 'NUMBER'),
            (r'[a-zA-Z_][a-zA-Z0-9_]*', 'IDENTIFIER'),
            (r'\+', 'PLUS'),
            (r'-', 'MINUS'),
            (r'\*', 'MULTIPLY'),
            (r'/', 'DIVIDE'),
            (r'=', 'ASSIGN'),
            (r'==', 'EQUAL'),
            (r'!=', 'NOT_EQUAL'),
            (r'>', 'GREATER'),
            (r'<', 'LESS'),
            (r'\(', 'OPEN_PAREN'),
            (r'\)', 'CLOSE_PAREN'),
            (r'\{', 'OPEN_BRACE'),
            (r'\}', 'CLOSE_BRACE'),
            (r';', 'SEMICOLON'),
        ]

        # Комбинируем все паттерны в одно регулярное выражение
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for pattern, name in patterns)

        pos = 0
        while pos < len(text):
            # Пропускаем пробелы и табуляции
            if text[pos] in ' \t\n':
                pos += 1
                continue

            # Пытаемся найти соответствие
            match = None
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(text, pos)
                if match:
                    value = match.group(0)
                    self.tokens.append(Token(token_type, value))
                    pos = match.end()
                    break

            if not match:
                # Если не нашли соответствие, пропускаем символ
                pos += 1

        return self.tokens


# ==================== ПАРСЕР ====================
class Parser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.pos = 0

        # Пропускаем 'package main' если есть
        if self.pos < len(self.tokens) and self.current_token().type == 'PACKAGE':
            self.consume('PACKAGE')
            self.consume('IDENTIFIER')  # main

        # Парсим функцию
        return self.parse_function()

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consume(self, expected_type):
        token = self.current_token()
        if token and token.type == expected_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Ожидался {expected_type}, получен {token}")

    def parse_function(self):
        self.consume('FUNC')
        func_name = self.consume('IDENTIFIER').value
        self.consume('OPEN_PAREN')
        self.consume('CLOSE_PAREN')
        self.consume('OPEN_BRACE')

        # Парсим все операторы внутри функции
        statements = []
        while self.current_token() and self.current_token().type != 'CLOSE_BRACE':
            if self.current_token().type == 'PRINT':
                statements.append(self.parse_print_statement())
            else:
                # Пропускаем неизвестные токены
                self.pos += 1

        self.consume('CLOSE_BRACE')

        # Создаем AST
        func = Function(func_name, [], Block(statements))
        return Package('main', [func])

    def parse_print_statement(self):
        self.consume('PRINT')
        self.consume('OPEN_PAREN')
        expr = self.parse_expression()
        self.consume('CLOSE_PAREN')
        self.consume('SEMICOLON')
        return Print(expr)

    def parse_expression(self):
        # Парсим первый терм
        left = self.parse_term()

        # Парсим остальные операции
        while self.current_token() and self.current_token().type in ('PLUS', 'MINUS'):
            op_token = self.current_token()
            self.consume(op_token.type)
            right = self.parse_term()

            if op_token.type == 'PLUS':
                left = Sum(left, right)
            elif op_token.type == 'MINUS':
                left = Sub(left, right)

        return left

    def parse_term(self):
        token = self.current_token()

        if token.type == 'NUMBER':
            self.consume('NUMBER')
            return Number(token.value)
        elif token.type == 'IDENTIFIER':
            self.consume('IDENTIFIER')
            # Для простоты возвращаем 0 для переменных
            return Number(0)
        elif token.type == 'OPEN_PAREN':
            self.consume('OPEN_PAREN')
            expr = self.parse_expression()
            self.consume('CLOSE_PAREN')
            return expr

        raise SyntaxError(f"Неожиданный токен: {token}")


# ==================== ГЛАВНАЯ ФУНКЦИЯ ====================
def main():
    # Пример программы на MiniGo
    code = """package main

func main() {
    print(4 + 4 - 2);
}"""

    print("=" * 60)
    print("КОМПИЛЯТОР MINIGO")
    print("=" * 60)
    print("\nИсходный код:")
    print(code)

    print("\n" + "=" * 60)
    print("1. ЛЕКСИЧЕСКИЙ АНАЛИЗ")
    print("=" * 60)

    # Лексический анализ
    lexer = Lexer()
    tokens = lexer.tokenize(code)

    print("Найдено токенов:", len(tokens))
    print("\nСписок токенов:")
    for i, token in enumerate(tokens):
        print(f"  [{i:2d}] {token}")

    print("\n" + "=" * 60)
    print("2. СИНТАКСИЧЕСКИЙ АНАЛИЗ")
    print("=" * 60)

    # Синтаксический анализ
    parser = Parser()

    try:
        ast = parser.parse(tokens)
        print("✓ Дерево AST успешно построено")

        print("\n" + "=" * 60)
        print("3. ВЫПОЛНЕНИЕ ПРОГРАММЫ")
        print("=" * 60)

        # Выполнение
        print("Результат выполнения:")
        ast.eval()

        print("\n" + "=" * 60)
        print("✓ ПРОГРАММА УСПЕШНО ВЫПОЛНЕНА")
        print("=" * 60)

    except SyntaxError as e:
        print(f"✗ Ошибка синтаксического анализа: {e}")
    except Exception as e:
        print(f"✗ Ошибка выполнения: {e}")


if __name__ == "__main__":
    main()