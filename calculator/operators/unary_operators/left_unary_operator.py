from calculator.utills import mathematical_operations
from calculator.operators.unary_operators.unary_operator import UnaryOperator


class LeftUnaryOperator(UnaryOperator):
    """
    Class represents unary operator that can only appear to the left of an operand, inherits from Unary Operator class.
    """

    def __init__(self, precedence: int, operation: mathematical_operations):
        """
        Method initializes a new LeftUnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)
