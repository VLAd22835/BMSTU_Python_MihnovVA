from rply.token import BaseBox


class ASTNode(BaseBox):
    def eval(self):
        pass


class NumberNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value.getstr())

    def __repr__(self):
        return f"Number({self.value.getstr()})"


class BinaryOpNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class SumNode(BinaryOpNode):
    def eval(self):
        return self.left.eval() + self.right.eval()

    def __repr__(self):
        return f"Sum({self.left}, {self.right})"


class SubNode(BinaryOpNode):
    def eval(self):
        return self.left.eval() - self.right.eval()

    def __repr__(self):
        return f"Sub({self.left}, {self.right})"


class MulNode(BinaryOpNode):
    def eval(self):
        return self.left.eval() * self.right.eval()

    def __repr__(self):
        return f"Mul({self.left}, {self.right})"


class DivNode(BinaryOpNode):
    def eval(self):
        right_val = self.right.eval()
        if right_val == 0:
            raise ZeroDivisionError("Деление на ноль")
        return self.left.eval() / right_val

    def __repr__(self):
        return f"Div({self.left}, {self.right})"


class PrintNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def eval(self):
        result = self.value.eval()
        print(result)
        return result

    def __repr__(self):
        return f"Print({self.value})"


class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        for statement in self.statements:
            statement.eval()

    def __repr__(self):
        return f"Block({self.statements})"


class FunctionNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

    def eval(self):
        return self.body.eval()

    def __repr__(self):
        return f"Function({self.name.getstr()}, {self.body})"


class PackageNode(ASTNode):
    def __init__(self, name, functions):
        self.name = name
        self.functions = functions

    def eval(self):
        for func in self.functions:
            func.eval()

    def __repr__(self):
        return f"Package({self.name.getstr()}, {self.functions})"