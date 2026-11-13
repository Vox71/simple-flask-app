import pytest

from app import app
from calculator import add, calculate, divide, multiply, subtract


def make_client():
    return app.test_client()


def test_iteration_01_add():
    assert add(2, 3) == 5


def test_iteration_02_subtract():
    assert subtract(7, 4) == 3


def test_iteration_03_multiply():
    assert multiply(3, 4) == 12


def test_iteration_04_divide():
    assert divide(8, 2) == 4.0


def test_iteration_05_divide_by_zero():
    with pytest.raises(ValueError, match="division by zero"):
        divide(1, 0)


def test_iteration_06_calc_add():
    response = make_client().get("/calc?op=add&a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_iteration_07_calc_subtract():
    response = make_client().get("/calc?op=subtract&a=7&b=4")
    assert response.status_code == 200
    assert response.get_json() == {"result": 3}


def test_iteration_08_calc_multiply():
    response = make_client().get("/calc?op=multiply&a=3&b=4")
    assert response.status_code == 200
    assert response.get_json() == {"result": 12}


def test_iteration_09_calc_divide():
    response = make_client().get("/calc?op=divide&a=8&b=2")
    assert response.status_code == 200
    assert response.get_json() == {"result": 4.0}


def test_iteration_10_calc_divide_by_zero():
    response = make_client().get("/calc?op=divide&a=1&b=0")
    assert response.status_code == 400
    assert response.get_json() == {"error": "division by zero"}


def test_iteration_11_calc_missing_params():
    response = make_client().get("/calc?op=add&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_iteration_12_calc_invalid_params():
    response = make_client().get("/calc?op=add&a=x&b=1")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_iteration_13_calculate_dispatcher():
    assert calculate("add", 2, 3) == 5


def test_iteration_14_float_params():
    response = make_client().get("/calc?op=add&a=2.5&b=0.5")
    assert response.status_code == 200
    assert response.get_json() == {"result": 3.0}


def test_iteration_15_final_regression():
    response = make_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
