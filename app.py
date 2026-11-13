"""Simple Flask service with a liveness probe and an integer addition endpoint."""

from flask import Flask, jsonify, request

from calculator import add, calculate

__version__ = "1.0.0"

app = Flask(__name__)


@app.get("/health")
def health():
    """Liveness probe: returns 200 while the app is running."""
    return jsonify(status="ok"), 200


@app.get("/add")
def add_endpoint():
    """Return the sum of the 'a' and 'b' query parameters."""
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return jsonify(error="params 'a' and 'b' must be integers"), 400
    return jsonify(result=add(a, b)), 200


@app.get("/calc")
def calc_endpoint():
    """Return the result of a calculator operation."""
    op = request.args.get("op")
    a_raw = request.args.get("a")
    b_raw = request.args.get("b")
    if op is None or a_raw is None or b_raw is None:
        return jsonify(error="params op, a and b are required"), 400
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    if a is None or b is None:
        return jsonify(error="params a and b must be numbers"), 400
    try:
        return jsonify(result=calculate(op, a, b)), 200
    except ValueError as exc:
        return jsonify(error=str(exc)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
