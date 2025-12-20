from my_ast import Number, Sum, Sub, Print


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        if self.current_token().type == 'PACKAGE':
            self.eat('PACKAGE')
            self.eat('IDENTIFIER')

        self.eat('FUNC')
        self.eat('IDENTIFIER')
        self.eat('OPEN_PAREN')
        self.eat('CLOSE_PAREN')
        self.eat('OPEN_BRACE')

        while self.current_token().type != 'CLOSE_BRACE':
            if self.current_token().type == 'PRINT':
                ast = self.parse_print()
            else:
                self.pos += 1

        self.eat('CLOSE_BRACE')
        return ast

    def current_token(self):
        return self.tokens[self.pos]

    def eat(self, token_type):
        token = self.current_token()
        if token.type == token_type:
            self.pos += 1
            return token
        raise SyntaxError(f"Ожидался {token_type}")

    def parse_print(self):
        self.eat('PRINT')
        self.eat('OPEN_PAREN')
        expr = self.parse_expression()
        self.eat('CLOSE_PAREN')
        self.eat('SEMICOLON')
        return Print(expr)

    def parse_expression(self):
        left = self.parse_term()

        while self.current_token().type in ('PLUS', 'MINUS'):
            op = self.current_token().type
            self.eat(op)
            right = self.parse_term()

            if op == 'PLUS':
                left = Sum(left, right)
            elif op == 'MINUS':
                left = Sub(left, right)

        return left

    def parse_term(self):
        token = self.current_token()

        if token.type == 'NUMBER':
            self.eat('NUMBER')
            return Number(token.value)
        elif token.type == 'OPEN_PAREN':
            self.eat('OPEN_PAREN')
            expr = self.parse_expression()
            self.eat('CLOSE_PAREN')
            return expr

        raise SyntaxError(f"Неожиданный токен: {token}")