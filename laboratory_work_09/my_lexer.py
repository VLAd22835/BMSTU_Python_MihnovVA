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

        # Комбинируем все паттерны
        token_regex = '|'.join(f'(?P<{name}>{pattern})' for pattern, name in patterns)

        pos = 0
        self.tokens = []

        while pos < len(text):
            # Пропускаем пробелы, табуляции и переносы строк
            if text[pos] in ' \t\n':
                pos += 1
                continue

            # Ищем соответствие
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
                # Если не нашли, пропускаем символ
                pos += 1

        return self.tokens