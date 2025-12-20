"""
КОМПИЛЯТОР MINI-GO - ВСЕ В ОДНОМ ФАЙЛЕ
"""


# ========== AST ==========
class Number:
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()


class Sub:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() - self.right.eval()


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        result = self.value.eval()
        print(result)
        return result


# ========== ЛЕКСЕР ==========
def tokenize(code):
    tokens = []
    i = 0

    while i < len(code):
        if code[i] in ' \n\t':
            i += 1
            continue

        if code[i:i + 7] == 'package':
            tokens.append(('PACKAGE', 'package'))
            i += 7
            continue

        if code[i:i + 4] == 'func':
            tokens.append(('FUNC', 'func'))
            i += 4
            continue

        if code[i:i + 5] == 'print':
            tokens.append(('PRINT', 'print'))
            i += 5
            continue

        if code[i:i + 4] == 'main':
            tokens.append(('IDENTIFIER', 'main'))
            i += 4
            continue

        if code[i].isdigit():
            num = ''
            while i < len(code) and code[i].isdigit():
                num += code[i]
                i += 1
            tokens.append(('NUMBER', num))
            continue

        if code[i] == '+':
            tokens.append(('PLUS', '+'))
        elif code[i] == '-':
            tokens.append(('MINUS', '-'))
        elif code[i] == '(':
            tokens.append(('OPEN_PAREN', '('))
        elif code[i] == ')':
            tokens.append(('CLOSE_PAREN', ')'))
        elif code[i] == '{':
            tokens.append(('OPEN_BRACE', '{'))
        elif code[i] == '}':
            tokens.append(('CLOSE_BRACE', '}'))
        elif code[i] == ';':
            tokens.append(('SEMICOLON', ';'))
        else:
            i += 1
            continue

        i += 1

    return tokens


# ========== ПАРСЕР ==========
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current_token(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def eat(self, token_type):
        token = self.current_token()
        if token and token[0] == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Ожидался {token_type}, получен {token}")

    def parse(self):
        if self.current_token() and self.current_token()[0] == 'PACKAGE':
            self.eat('PACKAGE')
            self.eat('IDENTIFIER')

        self.eat('FUNC')
        self.eat('IDENTIFIER')
        self.eat('OPEN_PAREN')
        self.eat('CLOSE_PAREN')
        self.eat('OPEN_BRACE')

        while self.current_token() and self.current_token()[0] != 'CLOSE_BRACE':
            if self.current_token()[0] == 'PRINT':
                ast = self.parse_print()
            else:
                self.pos += 1

        self.eat('CLOSE_BRACE')
        return ast

    def parse_print(self):
        self.eat('PRINT')
        self.eat('OPEN_PAREN')
        expr = self.parse_expression()
        self.eat('CLOSE_PAREN')
        self.eat('SEMICOLON')
        return Print(expr)

    def parse_expression(self):
        left = self.parse_term()

        while self.current_token() and self.current_token()[0] in ('PLUS', 'MINUS'):
            op = self.current_token()
            self.eat(op[0])
            right = self.parse_term()

            if op[0] == 'PLUS':
                left = Sum(left, right)
            elif op[0] == 'MINUS':
                left = Sub(left, right)

        return left

    def parse_term(self):
        token = self.current_token()

        if token[0] == 'NUMBER':
            self.eat('NUMBER')
            return Number(token[1])
        elif token[0] == 'OPEN_PAREN':
            self.eat('OPEN_PAREN')
            expr = self.parse_expression()
            self.eat('CLOSE_PAREN')
            return expr

        raise SyntaxError(f"Неожиданный токен: {token}")


# ========== ГЛАВНАЯ ФУНКЦИЯ ==========
def main():
    code = """package main
func main() {
    print(4 + 4 - 2);
}"""

    print("Исходный код:")
    print(code)
    print("\n" + "=" * 50)

    print("1. Лексический анализ:")
    tokens = tokenize(code)
    print("Токены:")
    for i, token in enumerate(tokens):
        print(f"  [{i:2d}] {token[0]:12} '{token[1]}'")

    print("\n" + "=" * 50)
    print("2. Синтаксический анализ:")

    parser = Parser(tokens)
    ast = parser.parse()

    if ast:
        print("AST построен успешно!")

        print("\n" + "=" * 50)
        print("3. Выполнение программы:")
        print("Результат:")
        ast.eval()


if __name__ == "__main__":
    main()