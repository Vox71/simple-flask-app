from app import add, app


def make_client():
    return app.test_client()


def test_health():
    response = make_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_add_function():
    assert add(2, 3) == 5


def test_add():
    response = make_client().get("/add?a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_add_negative():
    response = make_client().get("/add?a=-5&b=2")
    assert response.status_code == 200
    assert response.get_json() == {"result": -3}


def test_add_missing_param():
    response = make_client().get("/add?a=2")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_add_invalid_param():
    response = make_client().get("/add?a=x&b=1")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_add_no_params():
    response = make_client().get("/add")
    assert response.status_code == 400


def test_calc_add_endpoint():
    response = make_client().get("/calc?op=add&a=2&b=3")
    assert response.status_code == 200
    assert response.get_json() == {"result": 5}


def test_calc_subtract_endpoint():
    response = make_client().get("/calc?op=subtract&a=7&b=4")
    assert response.status_code == 200
    assert response.get_json() == {"result": 3}


def test_calc_multiply_endpoint():
    response = make_client().get("/calc?op=multiply&a=3&b=4")
    assert response.status_code == 200
    assert response.get_json() == {"result": 12}


def test_calc_divide_endpoint():
    response = make_client().get("/calc?op=divide&a=8&b=2")
    assert response.status_code == 200
    assert response.get_json() == {"result": 4.0}


def test_calc_divide_fractional():
    response = make_client().get("/calc?op=divide&a=7&b=2")
    assert response.status_code == 200
    assert response.get_json() == {"result": 3.5}


def test_calc_divide_by_zero_returns_400():
    response = make_client().get("/calc?op=divide&a=1&b=0")
    assert response.status_code == 400
    assert response.get_json() == {"error": "division by zero"}


def test_calc_missing_a_returns_400():
    response = make_client().get("/calc?op=add&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_calc_missing_b_returns_400():
    response = make_client().get("/calc?op=add&a=2")
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_calc_missing_op_returns_400():
    response = make_client().get("/calc?a=2&b=3")
    assert response.status_code == 400
    assert "error" in response.get_json()
