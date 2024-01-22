import pytest
from calculator.parser import evaluate
from calculator.utills.custom_exceptions.operator_syntax_error import OperatorSyntaxError
from calculator.utills.custom_exceptions.parentheses_syntax_error import ParenthesesSyntaxError
from calculator.utills.custom_exceptions.unknown_character_error import UnknownCharacterError
from calculator.utills.custom_exceptions.number_format_error import NumberFormatError


@pytest.mark.parametrize("expression, exception", [
    ("6^@9 ", OperatorSyntaxError),
    ("+7+1", OperatorSyntaxError),
    ("3//5 ", OperatorSyntaxError),
    ("4**8 ", OperatorSyntaxError),
    ("32- ", OperatorSyntaxError),
    ("*34*2/", OperatorSyntaxError),
    ("", ValueError),
    ("      ", ValueError),
    ("a", UnknownCharacterError)
])
def test_simple_invalid(expression, exception):
    """
    Testing simple invalid expression examples.
    :param expression: An expression to be tested.
    :raise exception: The expected exception from the calculation.
    """
    with pytest.raises(exception):
        evaluate(expression)


@pytest.mark.parametrize("expression, expected", [
    (".5^ 2", 0.25),
    ("5+~7 ", -2),
    ("3!!", 720),
    ("~-5!", 120),
    ("4 & 6 @ 8", 6),
    ("999#", 27),
    ("7 % 4", 3),
    ("8 $ 2", 8),
    ("15 /- 5", -3),
    ("9--9", 18),
    ("5/(0+4)", 1.25),
    ("2^0.5", 1.4142135624),
    ("(6+4)*(2+4)", 60),
    ("~--9", -9),
    ("-4!", -24),
])
def test_valid_expressions(expression, expected):
    """
    Testing simple valid expression examples.
    :param expression: An expression to be tested.
    :param expected: The expected result of the calculation.
    """
    assert evaluate(expression) == expected


@pytest.mark.parametrize("expression, expected", [
    (" (5$ 4.5@(5!*3)*2--1)#", 15),
    ("~((2/2) ^ (3!!))/3/3", -0.1111111111),
    ("((300-4010)*-0.1+2!!)##", 4),
    ("~(((50 *0.2 + 10)*30+60)^0.5)", -25.6904651573),
    ("(49 % (7 + 70)) @ 7 @ 1", 14.5),
    ("3 / 6.5 / 9 / ~12 / 0.1", -0.042735043),
    ("(((~(~(567#)))#!#/2--4.5)/2)!", 362880),
    ("4$3%4^~-(9+(8))##!&(76-18)", 0),
    ("(((4.5 + 3.5)/ 2) ! *       4) % (2+3)", 1),
    ("  2^10/( ( 10 ) )+-(100#!!)", 101.4),
    ("31 + (5 - (9 + 1.7#))", 19),
    ("(~-(----(- ------(5))) -- 4)", -1),
    ("((89) / (47#   ) + 3!!)*-1", -728.0909090909),
    ("(~-5*2+3/5) *5/7   /6/-3/ ~4", 0.1051587302),
    ("~-(((~-2)^    (1/3)) #)#", 6),
    ("(3$(44#!/1000@500)#/7)!!", 720),
    ("(31 + (5 - (9 + 1.7#)))##", 1),
    ("((3!+1 *( 3 ) - 5)/2*18#)#", 9),
    ("(((9@~- - 3) %    10 ---5)*-1)!", 2),
    ("((( 5!)/6+100)#!!#)--2@15", 2.5),
])
def test_valid_complex_expressions(expression, expected):
    """
    Testing complex valid expression examples.
    :param expression: An expression to be tested.
    :param expected: The expected result of the calculation.
    """
    assert evaluate(expression) == expected


@pytest.mark.parametrize("expression, exception", [
    ("3^.0+", OperatorSyntaxError),
    ("5/-0", ZeroDivisionError),
    ("6*/2", OperatorSyntaxError),
    ("3--+10", OperatorSyntaxError),
    ("9~2", OperatorSyntaxError),
    ("6+4.6.4", NumberFormatError),
    ("2+-2#", ArithmeticError),
    ("~2!-3", ArithmeticError),
    ("()", ParenthesesSyntaxError),
    ("((7) * 6))", ParenthesesSyntaxError),
    ("4*(3+4", ParenthesesSyntaxError),
    ("2~!", OperatorSyntaxError),
    ("!5", OperatorSyntaxError),
    ("4@(3+4", ParenthesesSyntaxError),
])
def test_complex_invalid(expression, exception):
    """
    Testing complex invalid expression examples.
    :param expression: An expression to be tested.
    :raise exception: The expected exception from the calculation.
    """
    with pytest.raises(exception):
        evaluate(expression)
