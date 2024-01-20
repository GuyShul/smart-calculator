from calculator.utills import mathematical_operations
from calculator.operators.unary_operators.unary_operator import UnaryOperator


class RightUnaryOperator(UnaryOperator):
    """
    Class represents unary operator that can only appear to the right of an operand, inherits from Unary Operator class.
    """

    def __init__(self, precedence: int, operation: mathematical_operations):
        """
        Method initializes a new RightUnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)
