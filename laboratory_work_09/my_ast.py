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