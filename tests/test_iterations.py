import pytest

from app import __version__, app
from calculator import add, calculate, divide, multiply, subtract


def make_client():
    return app.test_client()


def test_iteration_01_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-5, 2) == -3


def test_iteration_02_subtract():
    assert subtract(7, 4) == 3
    assert subtract(2, 7) == -5
    assert subtract(-5, -2) == -3
    assert subtract(0, 0) == 0


def test_iteration_03_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-3, 4) == -12
    assert multiply(0, 99) == 0


def test_iteration_04_divide():
    assert divide(8, 2) == 4.0
    assert divide(7, 2) == 3.5
    assert divide(-8, 2) == -4.0
    assert divide(0, 5) == 0.0


def test_iteration_05_divide_by_zero():
    with pytest.raises(ValueError, match="division by zero"):
        divide(1, 0)
    with pytest.raises(ValueError, match="division by zero"):
        divide(0, 0)


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
    client = make_client()
    exact = client.get("/calc?op=divide&a=8&b=2")
    fractional = client.get("/calc?op=divide&a=7&b=2")
    assert exact.status_code == 200
    assert exact.get_json() == {"result": 4.0}
    assert fractional.status_code == 200
    assert fractional.get_json() == {"result": 3.5}


def test_iteration_10_calc_divide_by_zero():
    response = make_client().get("/calc?op=divide&a=1&b=0")
    assert response.status_code == 400
    assert response.get_json() == {"error": "division by zero"}


def test_iteration_11_calc_missing_params():
    client = make_client()
    for url in [
        "/calc?op=add&b=3",
        "/calc?op=add&a=2",
        "/calc?a=2&b=3",
    ]:
        response = client.get(url)
        assert response.status_code == 400
        assert "error" in response.get_json()


def test_iteration_12_calc_invalid_params():
    client = make_client()
    for url in [
        "/calc?op=add&a=x&b=1",
        "/calc?op=add&a=1&b=x",
    ]:
        response = client.get(url)
        assert response.status_code == 400
        assert "error" in response.get_json()


def test_iteration_13_calculate_dispatcher():
    assert calculate("add", 2, 3) == 5
    assert calculate("subtract", 7, 4) == 3
    assert calculate("multiply", 3, 4) == 12
    assert calculate("divide", 8, 2) == 4.0
    with pytest.raises(ValueError, match="unsupported operation"):
        calculate("pow", 2, 3)
    response = make_client().get("/calc?op=pow&a=2&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_iteration_14_float_params():
    client = make_client()
    float_response = client.get("/calc?op=add&a=2.5&b=0.5")
    assert float_response.status_code == 200
    assert float_response.get_json() == {"result": 3.0}

    integer_response = client.get("/calc?op=add&a=2&b=3")
    integer_result = integer_response.get_json()["result"]
    assert integer_result == 5
    assert isinstance(integer_result, int)

    divide_response = client.get("/calc?op=divide&a=8&b=2")
    divide_result = divide_response.get_json()["result"]
    assert divide_result == 4.0
    assert isinstance(divide_result, float)


def test_iteration_15_final_regression():
    client = make_client()
    assert __version__ == "1.1.0"

    health = client.get("/health")
    assert health.status_code == 200
    assert health.get_json() == {"status": "ok"}

    legacy = client.get("/add?a=2&b=3")
    assert legacy.status_code == 200
    assert legacy.get_json() == {"result": 5}
    assert client.get("/add?a=2").status_code == 400
    assert client.get("/add?a=x&b=1").status_code == 400

    expected = {
        "add": 5,
        "subtract": -1,
        "multiply": 6,
        "divide": 2 / 3,
    }
    for operation, result in expected.items():
        response = client.get(f"/calc?op={operation}&a=2&b=3")
        assert response.status_code == 200
        assert response.get_json() == {"result": result}
