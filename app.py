from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    """Liveness probe: returns 200 while the app is running."""
    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
