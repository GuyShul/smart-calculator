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

    operand_stack = []
    i = 0

    while i < len(expression):
        # Receiving a number.
        if expression[i].isdigit() or expression[i] == '.':
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
            raise ValueError(f"Your expression contains invalid character(s) - '{expression[i]}'")

        i += 1

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
