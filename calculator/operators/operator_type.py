from calculator import mathematical_operations


class Operator(object):
    """
    Class represents basic operator.
    """

    def __init__(self, precedence: int, operation: mathematical_operations):
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

    def get_operation(self) -> mathematical_operations:
        """
        Method returns the operator's arithmetic operation.
        :return: operator's operation.
        """
        return self.__operation
