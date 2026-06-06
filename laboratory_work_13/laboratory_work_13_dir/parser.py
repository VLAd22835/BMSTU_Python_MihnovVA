from rply import ParserGenerator
from laboratory_work_13.laboratory_work_13_dir.my_token import TokenType
from laboratory_work_13.laboratory_work_13_dir.my_ast import *


class Parser:
    def __init__(self):
        self.pg = ParserGenerator(
            # Все токены, которые принимает парсер
            [TokenType.PACKAGE, TokenType.FUNC, TokenType.PRINT,
             TokenType.NUMBER, TokenType.IDENTIFIER,
             TokenType.PLUS, TokenType.MINUS, TokenType.MULTIPLY, TokenType.DIVIDE,
             TokenType.ASSIGN, TokenType.EQUAL, TokenType.NOT_EQUAL,
             TokenType.GREATER, TokenType.LESS,
             TokenType.OPEN_PAREN, TokenType.CLOSE_PAREN,
             TokenType.OPEN_BRACE, TokenType.CLOSE_BRACE,
             TokenType.SEMICOLON]
        )
        self._build_parser()

    def _build_parser(self):
        @self.pg.production('program : package_decl')
        def program(p):
            return p[0]

        @self.pg.production('package_decl : PACKAGE IDENTIFIER functions')
        def package_decl(p):
            return PackageNode(p[1], p[2])

        @self.pg.production('functions : function functions')
        def functions_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('functions : function')
        def functions_single(p):
            return [p[0]]

        @self.pg.production('function : FUNC IDENTIFIER OPEN_PAREN CLOSE_PAREN OPEN_BRACE statements CLOSE_BRACE')
        def function(p):
            return FunctionNode(p[1], [], BlockNode(p[5]))

        @self.pg.production('statements : statement statements')
        def statements_multiple(p):
            return [p[0]] + p[1]

        @self.pg.production('statements : statement')
        def statements_single(p):
            return [p[0]]

        @self.pg.production('statement : print_stmt')
        def statement(p):
            return p[0]

        @self.pg.production('print_stmt : PRINT OPEN_PAREN expression CLOSE_PAREN SEMICOLON')
        def print_stmt(p):
            return PrintNode(p[2])

        @self.pg.production('expression : expression PLUS term')
        @self.pg.production('expression : expression MINUS term')
        def expression_binop(p):
            left = p[0]
            right = p[2]
            op = p[1]

            if op.gettokentype() == TokenType.PLUS:
                return SumNode(left, right)
            elif op.gettokentype() == TokenType.MINUS:
                return SubNode(left, right)

        @self.pg.production('expression : term')
        def expression_term(p):
            return p[0]

        @self.pg.production('term : term MULTIPLY factor')
        @self.pg.production('term : term DIVIDE factor')
        def term_binop(p):
            left = p[0]
            right = p[2]
            op = p[1]

            if op.gettokentype() == TokenType.MULTIPLY:
                return MulNode(left, right)
            elif op.gettokentype() == TokenType.DIVIDE:
                return DivNode(left, right)

        @self.pg.production('term : factor')
        def term_factor(p):
            return p[0]

        @self.pg.production('factor : NUMBER')
        def factor_number(p):
            return NumberNode(p[0])

        @self.pg.production('factor : IDENTIFIER')
        def factor_identifier(p):
            # Для простоты возвращаем NumberNode с 0 для переменных
            return NumberNode("0")

        @self.pg.production('factor : OPEN_PAREN expression CLOSE_PAREN')
        def factor_paren(p):
            return p[1]

        @self.pg.error
        def error_handler(token):
            raise ValueError(f"Неожиданный токен: {token}")

    def get_parser(self):
        return self.pg.build()