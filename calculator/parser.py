from calculator.operators.operator_type import Operator
from calculator.operators.unary_operators.right_unary_operator import RightUnaryOperator
from calculator.operators.unary_operators.left_unary_operator import LeftUnaryOperator
from calculator.operators.binary_operator import BinaryOperator
from calculator.utills.calculator_info import OPERATOR_MAP
from calculator.utills.calculator_methods import (execute_operation, retrieve_until_parenthesis,
                                                  parse_operand, parse_operator)


def evaluate(expression: str):
    """
    Method responsible for calculations and Validity checks for user input.
    :param: str expression to be calculated.
    :return: the result.
    :raise TypeError: if the input is not str type.
    :raise SyntaxError: for invalid expression syntax.
    """
    if not isinstance(expression, str):
        raise TypeError("str type expression excepted")

    previous = ''
    operand_stack = []
    operator_stack = []

    i = 0
    while i < len(expression):
        current = expression[i]

        if current == '(':
            if previous == '' or isinstance(previous, (LeftUnaryOperator, BinaryOperator)):
                previous = OPERATOR_MAP.get(current)
                operator_stack.append(current)
            elif isinstance(previous, RightUnaryOperator):
                raise SyntaxError(f"missing binary operation between '{expression[i - 1]}' and parentheses")
            else:
                raise SyntaxError("'(' cannot occur after an operand")

        elif current.isdigit() or current == '.':
            i, previous = parse_operand(expression, i, previous, operand_stack)

        elif current in OPERATOR_MAP.keys():
            i, previous = parse_operator(expression, i, previous, operand_stack, operator_stack)

        elif current == ')':
            if not isinstance(previous, Operator) or isinstance(previous, RightUnaryOperator):
                retrieve_until_parenthesis(operand_stack, operator_stack)
                previous = current
            else:
                raise SyntaxError(f"')' is invalid after '{expression[i - 1]}, missing operand")

        elif current != " " and current != "\t":
            raise SyntaxError(f"Your expression contains invalid character(s) - '{current}'")

        i += 1

    # In case there are any operators left in the list (referred as stack)
    while operator_stack:
        execute_operation(operand_stack, operator_stack)

    if operand_stack:
        result = operand_stack.pop()
        if int(result) == result:
            return int(result)
        else:
            return result
    else:
        raise SyntaxError("Empty statement cannot be calculated")
