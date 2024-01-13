import Mathematical_operations


# base class represents an operator
class Operator(object):
    def __init__(self, precedence: int, operation: Mathematical_operations):
        self.precedence = precedence
        self.operation = operation

    def get_precedence(self) -> int:
        return self.precedence

    def set_precedence(self, precedence):
        self.precedence = precedence

    def get_operation(self) -> int:
        return self.precedence

    def set_operation(self, operation):
        self.operation = operation

    def __str__(self):
        return f"precedence - {self.precedence}"


class BinaryOperator(Operator):
    def __init__(self, precedence: int, operation: Mathematical_operations):
        super().__init__(precedence, operation)


class UnaryOperator(Operator):

    def __init__(self, precedence: int, operation: Mathematical_operations):
        super().__init__(precedence, operation)


class LeftUnaryOperator(UnaryOperator):

    def __init__(self, precedence: int, operation: Mathematical_operations):
        super().__init__(precedence, operation)


class RightUnaryOperator(UnaryOperator):

    def __init__(self, precedence: int, operation: Mathematical_operations):
        super().__init__(precedence, operation)
