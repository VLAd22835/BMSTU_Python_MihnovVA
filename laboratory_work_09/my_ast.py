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


class Mul(BinaryOp):
    def eval(self):
        return self.left.eval() * self.right.eval()


class Div(BinaryOp):
    def eval(self):
        right_val = self.right.eval()
        if right_val == 0:
            raise ZeroDivisionError("Деление на ноль")
        return self.left.eval() / right_val


class Greater(BinaryOp):
    def eval(self):
        return self.left.eval() > self.right.eval()


class Less(BinaryOp):
    def eval(self):
        return self.left.eval() < self.right.eval()


class Equal(BinaryOp):
    def eval(self):
        return self.left.eval() == self.right.eval()


class NotEqual(BinaryOp):
    def eval(self):
        return self.left.eval() != self.right.eval()


class Variable:
    def __init__(self, name):
        self.name = name

    def eval(self):
        return 0


class Assignment:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def eval(self):
        return self.value.eval()


class VarDeclaration:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def eval(self):
        if self.value:
            return self.value.eval()
        return 0


class Print:
    def __init__(self, value):
        self.value = value

    def eval(self):
        result = self.value.eval()
        print(result)
        return result


class IfStatement:
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

    def eval(self):
        if self.condition.eval():
            if isinstance(self.then_branch, list):
                for statement in self.then_branch:
                    statement.eval()
            else:
                self.then_branch.eval()
        elif self.else_branch:
            if isinstance(self.else_branch, list):
                for statement in self.else_branch:
                    statement.eval()
            else:
                self.else_branch.eval()


class ForLoop:
    def __init__(self, init, condition, update, body):
        self.init = init
        self.condition = condition
        self.update = update
        self.body = body

    def eval(self):
        if self.init:
            self.init.eval()

        while self.condition.eval():
            if isinstance(self.body, list):
                for statement in self.body:
                    statement.eval()
            else:
                self.body.eval()

            if self.update:
                self.update.eval()


class Block:
    def __init__(self, statements):
        self.statements = statements

    def eval(self):
        if isinstance(self.statements, list):
            for statement in self.statements:
                statement.eval()
        else:
            self.statements.eval()


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
        if isinstance(self.functions, list):
            for func in self.functions:
                func.eval()
        else:
            self.functions.eval()