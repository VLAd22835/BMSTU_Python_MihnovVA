import re


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, '{self.value}')"

    def __repr__(self):
        return self.__str__()


class Lexer:
    def __init__(self):
        self.tokens = []

    def tokenize(self, text):
        token_specs = [
            ('PACKAGE', r'package'),
            ('FUNC', r'func'),
            ('VAR', r'var'),
            ('IF', r'if'),
            ('ELSE', r'else'),
            ('FOR', r'for'),
            ('PRINT', r'print'),
            ('NUMBER', r'\d+'),
            ('IDENTIFIER', r'[a-zA-Z_][a-zA-Z0-9_]*'),
            ('PLUS', r'\+'),
            ('MINUS', r'-'),
            ('MULTIPLY', r'\*'),
            ('DIVIDE', r'/'),
            ('ASSIGN', r'='),
            ('EQUAL', r'=='),
            ('NOT_EQUAL', r'!='),
            ('GREATER', r'>'),
            ('LESS', r'<'),
            ('OPEN_PAREN', r'\('),
            ('CLOSE_PAREN', r'\)'),
            ('OPEN_BRACE', r'\{'),
            ('CLOSE_BRACE', r'\}'),
            ('SEMICOLON', r';'),
            ('NEWLINE', r'\n'),
            ('SKIP', r'[ \t]+'),
            ('MISMATCH', r'.'),
        ]

        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specs)
        self.tokens = []

        line_num = 1
        line_start = 0

        for mo in re.finditer(tok_regex, text):
            kind = mo.lastgroup
            value = mo.group()

            if kind == 'NEWLINE':
                line_start = mo.end()
                line_num += 1
            elif kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Неизвестный символ: {value} на строке {line_num}')
            else:
                self.tokens.append(Token(kind, value))

        return self.tokens