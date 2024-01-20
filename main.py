from calculator.mathematical_operations import (addition, subtraction, multiplication, division, power, modulo,
                                                average, max_operand, min_operand, neg, factorial, sum_digits)
from calculator.operators.binary_operator import BinaryOperator
from calculator.operators.operator_type import Operator
from calculator.operators.unary_operators.left_unary_operator import LeftUnaryOperator
from calculator.operators.unary_operators.minus_unary_operator import MinusUnaryOperator
from calculator.operators.unary_operators.right_unary_operator import RightUnaryOperator
from calculator.operators.unary_operators.unary_operator import UnaryOperator

# A dictionary represents all the available operators.
# The key is the operator's symbol and the value is an instance of it's appropriate class,
# including precedence and a function in which the operands will be sent.
OPERATOR_MAP = {'+': BinaryOperator(1, addition),
                '-': BinaryOperator(1, subtraction),
                '*': BinaryOperator(2, multiplication),
                '/': BinaryOperator(2, division),
                '^': BinaryOperator(3, power),
                '%': BinaryOperator(4, modulo),
                '@': BinaryOperator(5, average),
                '$': BinaryOperator(5, max_operand),
                '&': BinaryOperator(5, min_operand),
                '~': LeftUnaryOperator(6, neg),
                '!': RightUnaryOperator(6, factorial),
                '#': RightUnaryOperator(6, sum_digits),
                '--': MinusUnaryOperator(1, neg),
                '(-)': LeftUnaryOperator(7, neg),
                '(': LeftUnaryOperator(0, None)}


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
        raise SyntaxError("Missing closing parenthesis")

    if isinstance(operator, UnaryOperator):
        if operand_stack:
            operand = operand_stack.pop()
            operand_stack.append(operator.get_operation()(operand))
        else:
            raise SyntaxError("Your expression is invalid, not enough operands for unary operation")
    elif len(operand_stack) > 1:
        operand1 = operand_stack.pop()
        operand2 = operand_stack.pop()
        operand_stack.append(round(operator.get_operation()(operand2, operand1), 10))
    else:
        raise SyntaxError("Your expression is invalid, not enough operands for binary operation")


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
        raise SyntaxError("Missing opening parenthesis")


def my_eval(expression: str):
    """
    Method responsible for calculations and Validity checks for user input.
    :param: str expression to be calculated.
    :return: the result.
    :raise TypeError: if the input is not str type.
    :raise SyntaxError: for invalid expression syntax.
    :raise ValueError: for invalid characters.
    """
    if not isinstance(expression, str):
        raise TypeError("str type expression excepted")

    previous = ''
    operand_stack = []
    operator_stack = []

    i = 0
    while i < len(expression):
        # Encountering an opening parenthesis.
        if expression[i] == '(':
            if previous == '' or isinstance(previous, Operator):
                previous = OPERATOR_MAP.get(expression[i])
                operator_stack.append(expression[i])
            else:
                raise SyntaxError("'(' cannot occur after an operand")
        # Receiving a number.
        elif expression[i].isdigit() or expression[i] == '.':
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
                if dots > 1:
                    raise SyntaxError("Invalid decimal number - cannot contain two dots or more!")
                elif single_operand == '.':
                    raise SyntaxError("Illegal value - '.'")
                i = j - 1
                operand_stack.append(float(single_operand))
            else:
                raise SyntaxError("Your expression is invalid")
        # Receiving an operator.
        elif expression[i] in OPERATOR_MAP.keys():
            symbol = expression[i]
            current = OPERATOR_MAP.get(symbol)
            if isinstance(current, UnaryOperator) or symbol == '-':
                if isinstance(current, LeftUnaryOperator) or symbol == '-':
                    if symbol == '-':
                        if (previous == '' or (
                                isinstance(previous,
                                           LeftUnaryOperator) and previous.get_precedence() == 0) or
                                isinstance(previous, MinusUnaryOperator)):
                            symbol = '--'
                            current = OPERATOR_MAP[symbol]
                        elif isinstance(previous, (BinaryOperator, LeftUnaryOperator)):
                            symbol = '(-)'
                            current = OPERATOR_MAP[symbol]
                        elif isinstance(previous, RightUnaryOperator) or not isinstance(previous, Operator):
                            pass
                        else:
                            raise SyntaxError(
                                f"'{symbol}' cannot occur after an operator, it's must occur to the left of an "
                                f"operand")
                    elif isinstance(previous, UnaryOperator) and previous.get_precedence() != 0:
                        if current == previous:
                            raise SyntaxError(
                                f"'{symbol}' cannot occur in a row")
                        else:
                            raise SyntaxError(
                                f"'Illegal use of '{symbol}', must occur after binary or at the beginning of the "
                                f"expression")
                    elif not isinstance(previous, Operator) and previous != '':
                        raise SyntaxError(
                            f"'{symbol}' cannot occur after an operand, it's must occur to the left of an "
                            f"operand")
                elif isinstance(previous, (BinaryOperator, LeftUnaryOperator)):
                    raise SyntaxError(
                        f"'{symbol}' cannot occur after '{expression[i - 1]}', it's must occur after"
                        f" an operand or expression")
                elif previous == '':
                    raise SyntaxError(
                        f"expression cannot start with a '{symbol}', it's must occur after an operand or "
                        f" an expression")
            elif previous == '':
                raise SyntaxError(
                    f"expression cannot start with a '{expression[i]}', it's must occur after an operand or an "
                    f"expression")
            elif isinstance(previous, (LeftUnaryOperator, BinaryOperator)):
                if current == previous:
                    raise SyntaxError(
                        f"'{expression[i]}' cannot occur in a row")
                else:
                    raise SyntaxError(
                        f"the follow operations: '{expression[i - 1]}', '{symbol}' cannot occur in a row")

            flag = True
            previous = OPERATOR_MAP.get(symbol)
            while operator_stack and operand_stack and flag:
                operator_top_stack = OPERATOR_MAP[operator_stack[-1]]
                if current.get_precedence() <= operator_top_stack.get_precedence() and symbol != '(-)':
                    execute_operation(operand_stack, operator_stack)
                else:
                    flag = False
            operator_stack.append(symbol)
        # Encountering a closing parenthesis.
        elif expression[i] == ')':
            if not isinstance(previous, Operator) or isinstance(previous, RightUnaryOperator):
                retrieve_until_parenthesis(operand_stack, operator_stack)
                previous = expression[i]
            else:
                raise SyntaxError(f"')' is invalid after '{expression[i - 1]}, missing operand")
        elif expression[i] != " " and expression[i] != "\t":
            raise SyntaxError(f"Your expression contains invalid character(s) - '{expression[i]}'")

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


def main():
    while True:
        try:
            print("Result:", my_eval(input("Insert expression: ")))
        except (EOFError, KeyboardInterrupt):
            print("Message: Shutting down...")
            return
        except Exception as e:
            print(f"Error: {type(e).__name__}, Message: {e}")


if __name__ == '__main__':
    main()
