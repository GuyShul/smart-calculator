import pytest
from main import my_eval


@pytest.mark.parametrize("expression", [
    "6^@9 ",
    "+7+1",
    "3//5 ",
    "4**8 ",
    "32- ",
    "*34*2/",
    "",
    "      ",
    "a",
])
def test_simple_invalid(expression):
    """
    Testing simple invalid expression examples.
    :param expression: An expression to be tested.
    """
    with pytest.raises(SyntaxError):
        my_eval(expression)


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
    assert my_eval(expression) == expected


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
    assert my_eval(expression) == expected


@pytest.mark.parametrize("expression, exception", [
    ("3^.0+", SyntaxError),
    ("5/-0", ZeroDivisionError),
    ("6*/2", SyntaxError),
    ("3--+10", SyntaxError),
    ("9~2", SyntaxError),
    ("6+4.6.4", SyntaxError),
    ("a", SyntaxError),
    ("2+-2#", ValueError),
    ("~2!-3", ValueError),
    ("((7) * 6))", SyntaxError),
    ("4*(3+4", SyntaxError),
    ("2~!", SyntaxError),
    ("!5", SyntaxError),
    ("4@(3+4", SyntaxError),

])
def test_complex_invalid(expression, exception):
    """
    Testing complex invalid expression examples.
    :param expression: An expression to be tested.
    :raise exception: The expected exception from the calculation.

    """
    with pytest.raises(exception):
        my_eval(expression)
