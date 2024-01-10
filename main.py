import Mathematical_operations

# A dictionary represents all the available operators.
# The key is the operator's symbol and the value is its precedence + a function in which the operands will be sent
OPERATOR_MAP = {'+': [1, Mathematical_operations.addition], '-': [1, Mathematical_operations.subtraction],
                '*': [2, Mathematical_operations.multiplication],
                '/': [2, Mathematical_operations.division], '^': [3, Mathematical_operations.power],
                '%': [4, Mathematical_operations.modulo],
                '@': [5, Mathematical_operations.average], '$': [5, Mathematical_operations.max_operand],
                '&': [5, Mathematical_operations.min_operand],
                '~': [6, Mathematical_operations.neg], '!': [6, Mathematical_operations.factorial]}


def is_operator(char: str) -> bool:
    """
    Method returns whether the given char is an operator or not.
    :param: a char.
    :return: true if operator, false otherwise.
    """
    return char in OPERATOR_MAP.keys()


def is_unary(operator: str) -> bool:
    """
    Method returns whether the given operator is unary or not.
    :param: an operator.
    :return: true if unary, false otherwise.
    """
    return is_operator(operator) and operator in ["!", "~"]


def execute_operation(operand_stack: list, operator_stack: list):
    """
    Method calculate a simple binary/unary expression with two given lists, one for operators and second for operands.
    Eventually the result is pushed into the operands stack.
    :param: list represents a stack of operands.
    :param: list represents a stack of operators.
    """
    operator = operator_stack.pop()
    if is_unary(operator):
        if operand_stack:
            operand = float(operand_stack.pop())
            operand_stack.append(list(map(OPERATOR_MAP[operator][1], [operand]))[0])
        else:
            raise SyntaxError("Your expression is invalid")
    elif len(operand_stack) > 1:
        operand1 = float(operand_stack.pop())
        operand2 = float(operand_stack.pop())
        operand_stack.append(list(map(OPERATOR_MAP[operator][1], [operand2], [operand1]))[0])
    else:
        raise SyntaxError("Your expression is invalid")


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
        # Receiving a number.
        if expression[i].isdigit() or expression[i] == '.':
            if previous == '' or (is_operator(previous) and previous != '!') or previous == '(':
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
                i = j - 1
                operand_stack.append(float(single_operand))
            else:
                raise SyntaxError("Your expression is invalid")
        # Receiving an operator.
        elif is_operator(expression[i]):
            current = expression[i]
            if not is_operator(previous):
                if previous != '' and is_unary(current) and current != '!' and current != '-':
                    raise SyntaxError(f"{current} cannot occur after operand")
            elif previous == current != '!':
                raise SyntaxError(f"{current} cannot occur in a row")
            elif previous == current and current != '-' and current != '!':
                raise SyntaxError(f"{current} cannot occur in row")
            elif not is_unary(previous) and not is_unary(current) and current != '-':
                raise SyntaxError(f"the follow operations: {previous}, {current} cannot occur in a row")

            flag = True
            previous = expression[i]
            current_operator = OPERATOR_MAP[expression[i]]
            while operator_stack and operand_stack and flag:
                operator_top_stack = OPERATOR_MAP[operator_stack[-1]]
                if current_operator[0] <= operator_top_stack[0]:
                    execute_operation(operand_stack, operator_stack)
                else:
                    flag = False
            operator_stack.append(expression[i])
        else:
            raise ValueError(f"Your expression contains invalid character(s) - '{expression[i]}'")

        i += 1

    # In case there are any operators left in the list (referred as stack)
    while operator_stack:
        execute_operation(operand_stack, operator_stack)

    if operand_stack:
        result = float(operand_stack.pop())
        if result.is_integer():
            print(int(result))
        else:
            print(result)
    else:
        raise SyntaxError("Empty statement cannot be calculated")


def main():
    my_eval(input("Insert expression: "))


if __name__ == '__main__':
    main()
