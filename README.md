# simple-flask-app

Educational Flask service with a liveness probe and an integer addition endpoint.
Version: **1.0.0**

## Endpoints

| Method | Path | Description | Example response |
| ------ | ---- | ----------- | ---------------- |
| GET | `/health` | Liveness probe | `{"status": "ok"}` |
| GET | `/add?a=2&b=3` | Sum of two integers, `400` if a parameter is missing or not an integer | `{"result": 5}` |

## Run locally

```bash
pip install -r requirements.txt
python app.py
curl http://localhost:5000/health
```

## Run with Docker

```bash
docker build -t simple-flask-app .
docker run -p 5000:5000 simple-flask-app
```

## Tests

```bash
pip install -r requirements-dev.txt
python -m pytest
```

## Documentation

The API reference is generated from docstrings by [pdoc](https://pdoc.dev) on every
push (see the `docs` job in `.github/workflows/Main.yml`) and published to GitHub Pages:

<https://vox71.github.io/simple-flask-app/>
