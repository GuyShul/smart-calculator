from calculator.operators.binary_operator import BinaryOperator
from calculator.operators.unary_operators.left_unary_operator import LeftUnaryOperator
from calculator.operators.unary_operators.minus_unary_operator import MinusUnaryOperator
from calculator.operators.unary_operators.right_unary_operator import RightUnaryOperator
from calculator.utills.mathematical_operations import (addition, subtraction, multiplication, division, power, modulo,
                                                       average, max_operand, min_operand, neg, factorial, sum_digits)

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
