from rply import LexerGenerator
from my_token import TokenType


class Lexer:
    def __init__(self):
        self.lg = LexerGenerator()
        self._add_tokens()

    def _add_tokens(self):
        # Ключевые слова
        self.lg.add(TokenType.PACKAGE, r'package')
        self.lg.add(TokenType.FUNC, r'func')
        self.lg.add(TokenType.PRINT, r'print')

        # Идентификаторы и числа
        self.lg.add(TokenType.NUMBER, r'\d+')
        self.lg.add(TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*')

        # Операторы
        self.lg.add(TokenType.PLUS, r'\+')
        self.lg.add(TokenType.MINUS, r'-')
        self.lg.add(TokenType.MULTIPLY, r'\*')
        self.lg.add(TokenType.DIVIDE, r'/')
        self.lg.add(TokenType.ASSIGN, r'=')
        self.lg.add(TokenType.EQUAL, r'==')
        self.lg.add(TokenType.NOT_EQUAL, r'!=')
        self.lg.add(TokenType.GREATER, r'>')
        self.lg.add(TokenType.LESS, r'<')

        # Скобки и разделители
        self.lg.add(TokenType.OPEN_PAREN, r'\(')
        self.lg.add(TokenType.CLOSE_PAREN, r'\)')
        self.lg.add(TokenType.OPEN_BRACE, r'\{')
        self.lg.add(TokenType.CLOSE_BRACE, r'\}')
        self.lg.add(TokenType.SEMICOLON, r';')

        # Игнорируем пробелы
        self.lg.ignore(r'\s+')

    def get_lexer(self):
        return self.lg.build()