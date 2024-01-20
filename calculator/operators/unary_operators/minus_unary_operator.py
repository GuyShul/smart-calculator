from calculator import mathematical_operations
from calculator.operators.binary_operator import BinaryOperator
from calculator.operators.unary_operators.left_unary_operator import LeftUnaryOperator


class MinusUnaryOperator(LeftUnaryOperator, BinaryOperator):
    """
    Class represents unary minus operator
    """

    def __init__(self, precedence: int, operation: mathematical_operations):
        """
        Method initializes a new MinusUnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)
