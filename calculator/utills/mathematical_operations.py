from math import pow


def addition(operand1: float, operand2: float) -> float:
    """
    Method calculates the addition of two operand.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: Sum of two operands.
    """
    return operand1 + operand2


def subtraction(operand1: float, operand2: float) -> float:
    """
    Method calculates the subtraction of two operands.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: Differance of two operands.
    """
    return operand1 - operand2


def multiplication(operand1: float, operand2: float) -> float:
    """
    Method multiplies two operands.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: Product of two operands.
    """
    return operand1 * operand2


def division(operand1: float, operand2: float) -> float:
    """
    Method divides two operands.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: Quotient of two operands.
    :raise ZeroDivisionError: when divider (second operand) is zero.
    """
    try:
        return operand1 / operand2
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")


def power(operand1: float, operand2: float) -> float:
    """
    Method increases first operand in the power on the second operand.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: first operand in the power on the second operand.
    :raise OverFlowError: for especially large numbers which cannot be handled.
    :raise ArithmeticError: for illogical math errors.
    """
    if operand1 == 0 and operand2 < 0:
        raise ArithmeticError("0 cannot be raised to a negative power")
    try:
        return pow(operand1, operand2)
    except OverflowError:
        raise OverflowError("math range exceeded, number is too large")
    except ArithmeticError:
        raise ArithmeticError("Cannot execute power on negative base and decimal exponent (integrating square root)")


def average(operand1: float, operand2: float) -> float:
    """
    Method calculates the average of first operand and second operand.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: average of first operand and second operand.
    """
    return (operand1 + operand2) / 2


def max_operand(operand1: float, operand2: float) -> float:
    """
    Method returns the max operand between two given operands.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: max operand between two given operands.
    """
    return operand1 if operand1 > operand2 else operand2


def min_operand(operand1: float, operand2: float) -> float:
    """
    Method returns the min operand between two given operands.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: min operand between two given operands.
    """
    return operand1 if operand1 < operand2 else operand2


def modulo(operand1: float, operand2: float) -> float:
    """
    Method calculates the remainder of dividing operand1 by operand2.
    :param operand1: first operand.
    :param operand2: second operand.
    :return: The remainder of dividing operand1 by operand2.
    :raise ZeroDivisionError: when divider (second operand) is zero.
    """
    try:
        return operand1 % operand2
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")


def neg(operand: float) -> float:
    """
    Method inverts the sign of the operand.
    :param operand: a given operand.
    :return: the given operand with inverted sign.
    """
    return -operand


def factorial(operand: float) -> float:
    """
    Method calculates the factorial of a given operand.
    :param: a given operand.
    :return: factorial of the given operand.
    :raise ArithmeticError: when the operand is negative or decimal.
    """
    result = 1
    x = 2
    if operand < 0:
        raise ArithmeticError("Cannot execute factorial operation on a negative number")
    if not int(operand) == operand:
        raise ArithmeticError("Cannot execute factorial operation on a decimal number")
    for x in range(x, int(operand + 1)):
        result *= x
    return result


def sum_digits(operand: float) -> int:
    """
    Method sums all the digits of a number.
    :param: a given operand.
    :return: addition of number's digits.
    :raise ArithmeticError: when the operand is negative.
    """
    result = 0
    if operand < 0:
        raise ArithmeticError('Cannot execute "sum digits" operation on a negative number')
    operand = format(operand, '.10f')
    operand = operand.replace('.', '')
    for digit in operand:
        result += int(digit)
    return result
