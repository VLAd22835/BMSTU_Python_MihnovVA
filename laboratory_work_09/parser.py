from my_ast import Number, Sum, Sub, Print, Block, Function, Package


class Parser:
    def __init__(self):
        self.tokens = []
        self.pos = 0

    def parse(self, tokens):
        self.tokens = tokens
        self.pos = 0

        # Пропускаем 'package main'
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

        # Парсим операторы внутри функции
        statements = []
        while self.current_token() and self.current_token().type != 'CLOSE_BRACE':
            if self.current_token().type == 'PRINT':
                statements.append(self.parse_print())
            else:
                # Пропускаем неизвестные токены
                self.pos += 1

        self.consume('CLOSE_BRACE')

        # Создаем функцию main
        func = Function(func_name, [], Block(statements))
        return Package('main', [func])

    def parse_print(self):
        self.consume('PRINT')
        self.consume('OPEN_PAREN')
        expr = self.parse_expression()
        self.consume('CLOSE_PAREN')
        self.consume('SEMICOLON')
        return Print(expr)

    def parse_expression(self):
        # Парсим первый терм
        left = self.parse_term()

        # Парсим операции + и -
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
            # Для простоты возвращаем Number(0) для переменных
            return Number(0)
        elif token.type == 'OPEN_PAREN':
            self.consume('OPEN_PAREN')
            expr = self.parse_expression()
            self.consume('CLOSE_PAREN')
            return expr

        raise SyntaxError(f"Неожиданный токен: {token}")