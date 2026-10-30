"""Simple Flask service with a liveness probe and an integer addition endpoint."""

from flask import Flask, jsonify, request

__version__ = "1.0.0"

app = Flask(__name__)


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
