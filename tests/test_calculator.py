import pytest

from calculator import add, divide, multiply, subtract


def test_add_positive_integers():
    assert add(2, 3) == 5


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative():
    assert add(-5, 2) == -3


def test_subtract_positive_integers():
    assert subtract(7, 4) == 3


def test_subtract_negative_result():
    assert subtract(2, 7) == -5


def test_subtract_negative_operands():
    assert subtract(-5, -2) == -3


def test_subtract_zero():
    assert subtract(0, 0) == 0


def test_multiply_positive_integers():
    assert multiply(3, 4) == 12


def test_multiply_negative():
    assert multiply(-3, 4) == -12


def test_multiply_zero():
    assert multiply(0, 99) == 0


def test_divide_positive_integers():
    assert divide(8, 2) == 4.0


def test_divide_returns_float():
    assert divide(7, 2) == 3.5


def test_divide_negative():
    assert divide(-8, 2) == -4.0


def test_divide_zero_numerator():
    assert divide(0, 5) == 0.0


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="division by zero"):
        divide(1, 0)


def test_divide_zero_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="division by zero"):
        divide(0, 0)
