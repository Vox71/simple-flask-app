from calculator import add, subtract


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
