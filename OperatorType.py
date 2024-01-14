import Mathematical_operations


class Operator(object):
    """
    Class represents basic operator.
    """

    def __init__(self, precedence: int, operation: Mathematical_operations):
        """
        Method initializes a new Operator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        self.__precedence = precedence
        self.__operation = operation

    def get_precedence(self) -> int:
        """
        Method returns the operator's precedence.
        :return: operator's precedence.
        """
        return self.__precedence

    def get_operation(self) -> Mathematical_operations:
        """
        Method returns the operator's arithmetic operation.
        :return: operator's operation.
        """
        return self.__operation


class BinaryOperator(Operator):
    """
    Class represents Binary operator, inherits from operator class.
    """

    def __init__(self, precedence: int, operation: Mathematical_operations):
        """
        Method initializes a new BinaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)


class UnaryOperator(Operator):
    """
    Class represents unary operator, inherits from operator class.
    """

    def __init__(self, precedence: int, operation: Mathematical_operations):
        """
        Method initializes a new UnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)


class LeftUnaryOperator(UnaryOperator):
    """
    Class represents unary operator that can only appear to the left of an operand, inherits from Unary Operator class.
    """

    def __init__(self, precedence: int, operation: Mathematical_operations):
        """
        Method initializes a new LeftUnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)


class RightUnaryOperator(UnaryOperator):
    """
    Class represents unary operator that can only appear to the right of an operand, inherits from Unary Operator class.
    """

    def __init__(self, precedence: int, operation: Mathematical_operations):
        """
        Method initializes a new RightUnaryOperator instance.
        :param precedence: The precedence of the operator.
        :param operation: an arithmetic function taken from "Mathematical_operations" file.
        """
        super().__init__(precedence, operation)
