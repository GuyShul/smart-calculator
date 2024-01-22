from calculator.operators.binary_operator import BinaryOperator
from calculator.operators.operator_type import Operator
from calculator.operators.unary_operators.left_unary_operator import LeftUnaryOperator
from calculator.operators.unary_operators.minus_unary_operator import MinusUnaryOperator
from calculator.operators.unary_operators.right_unary_operator import RightUnaryOperator
from calculator.operators.unary_operators.unary_operator import UnaryOperator
from calculator.utills.calculator_info import OPERATOR_MAP
from calculator.utills.custom_exceptions.number_format_error import NumberFormatError
from calculator.utills.custom_exceptions.operator_syntax_error import OperatorSyntaxError
from calculator.utills.custom_exceptions.parentheses_syntax_error import ParenthesesSyntaxError


def execute_operation(operand_stack: list, operator_stack: list):
    """
    Method calculate a simple binary/unary expression with two given lists, one for operators and second for operands.
    Eventually the result is pushed into the operands stack.
    :param: list represents a stack of operands.
    :param: list represents a stack of operators.
    """
    key = operator_stack.pop()
    operator = OPERATOR_MAP[key]
    if key == '(':
        raise ParenthesesSyntaxError("Missing closing parenthesis")

    if isinstance(operator, UnaryOperator):
        if operand_stack:
            operand = operand_stack.pop()
            operand_stack.append(operator.get_operation()(operand))
        else:
            raise OperatorSyntaxError("Your expression is invalid, not enough operands for unary operation")
    elif len(operand_stack) > 1:
        operand1 = operand_stack.pop()
        operand2 = operand_stack.pop()
        operand_stack.append(round(operator.get_operation()(operand2, operand1), 10))
    else:
        raise OperatorSyntaxError("Your expression is invalid, not enough operands for binary operation")


def retrieve_until_parenthesis(operand_stack: list, operator_stack: list):
    """
    Method calculates unlimited amount of partial expressions until it encounters with opening parenthesis.
    :param: list represents a stack of operands.
    :param: list represents a stack of operators.
    """
    while operator_stack and operator_stack[-1] != '(' and operand_stack:
        execute_operation(operand_stack, operator_stack)
    if operator_stack:
        operator_stack.pop()
    else:
        raise ParenthesesSyntaxError("Missing opening parenthesis")


def parse_operand(expression: str, i: int, previous: str, operand_stack: list[float]):
    """
    Method responsible to analyze current operand.
    :param expression: the original expression.
    :param i: the current position (in the loop).
    :param previous: the previous operator or operand.
    :param operand_stack: stack of operands.
    :return: the updated position and previous.
    """
    if previous == '' or (isinstance(previous, (LeftUnaryOperator, BinaryOperator))):
        previous = expression[i]
        single_operand = ""
        j = i
        dots = 0
        is_over = False
        while j < len(expression) and not is_over:
            if expression[j].isdigit():
                single_operand += expression[j]
                j += 1
            elif expression[j] == '.':
                single_operand += expression[j]
                dots += 1
                j += 1
            else:
                is_over = True
        if single_operand.replace('.', '') == '':
            raise NumberFormatError(f"Illegal value - '{single_operand}'")
        elif dots > 1:
            raise NumberFormatError("Invalid decimal number - cannot contain two dots or more!")

        i = j - 1
        if single_operand.count('.') == 0:
            operand_stack.append(int(single_operand))
        else:
            operand_stack.append(float(single_operand))
    else:
        raise OperatorSyntaxError(f"missing binary operation between '{expression[i - 1]}' and operand")
    return i, previous


def parse_operator(expression, i, previous, operand_stack, operator_stack):
    """
    Method responsible to analyze current operator and make a decision on the right situation.
    :param expression: the original expression.
    :param i: the current position (in the loop).
    :param previous: the previous operator or operand.
    :param operand_stack: stack of operands.
    :param operator_stack: stack of operators.
    :return: the updated position and previous.
    """
    symbol = expression[i]
    current = OPERATOR_MAP.get(symbol)
    if isinstance(current, UnaryOperator) or symbol == '-':
        if isinstance(current, LeftUnaryOperator) or symbol == '-':
            if symbol == '-':
                if (previous == '' or (
                        isinstance(previous,
                                   LeftUnaryOperator) and previous.get_precedence() == 0) or
                        type(previous) is MinusUnaryOperator):
                    symbol = '--'
                    current = OPERATOR_MAP[symbol]
                elif isinstance(previous, (BinaryOperator, LeftUnaryOperator)):
                    symbol = '(-)'
                    current = OPERATOR_MAP[symbol]
                elif isinstance(previous, RightUnaryOperator) or not isinstance(previous, Operator):
                    pass
                else:
                    raise OperatorSyntaxError(
                        f"'{symbol}' cannot occur after an operator, it's must occur to the left of an "
                        f"operand")
            elif isinstance(previous, UnaryOperator) and previous.get_precedence() != 0:
                if current == previous:
                    raise OperatorSyntaxError(
                        f"Invalid use of unary operation, '{symbol}' cannot occur in a row")
                else:
                    raise OperatorSyntaxError(
                        f"Invalid use of unary operation - '{symbol}' must occur after binary "
                        f"operation or at the beginning of the expression")
            elif not isinstance(previous, Operator) and previous != '':
                raise OperatorSyntaxError(
                    f"Invalid use of unary operation - '{symbol}' cannot occur after an operand, it's must occur to "
                    f"the left of an operand")
        elif isinstance(previous, (BinaryOperator, LeftUnaryOperator)):
            raise OperatorSyntaxError(
                f"Invalid use of unary operation - '{symbol}' cannot occur after '{expression[i - 1]}', it's must "
                f"occur after an operand or expression")
        elif previous == '':
            raise OperatorSyntaxError(
                f"Invalid use of unary operation - expression cannot start with a '{symbol}', it's must occur after "
                f"an operand or an expression")
    elif previous == '':
        raise OperatorSyntaxError(
            f"Invalid use of binary operation - expression cannot start with a '{expression[i]}', it's must occur "
            f"after an operand or an expression")
    elif isinstance(previous, (LeftUnaryOperator, BinaryOperator)):
        if current == previous:
            raise OperatorSyntaxError(
                f"Invalid use of binary operation, '{expression[i]}' cannot occur in a row")
        else:
            raise OperatorSyntaxError(
                f"Invalid use of binary operation, '{expression[i - 1]}' and '{symbol}' cannot occur in a row")

    flag = True
    previous = OPERATOR_MAP.get(symbol)
    while operator_stack and operand_stack and flag:
        operator_top_stack = OPERATOR_MAP[operator_stack[-1]]
        if current.get_precedence() <= operator_top_stack.get_precedence() and symbol != '(-)':
            execute_operation(operand_stack, operator_stack)
        else:
            flag = False
    operator_stack.append(symbol)
    return i, previous
