from calculator.utills import mathematical_operations
from calculator.operators.operator_type import Operator


class UnaryOperator(Operator):
    """
    Class represents unary operator, inherits from operator class.
    """

    def __init__(self, precedence: int, operation: mathematical_operations):
        """
        Method initializes a new UnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)
