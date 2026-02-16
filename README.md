# AI Iris Service

## Project Structure
ai-iris-service/
├── app/        # FastAPI application (API, schemas, service layer)
├── ml/         # Model training script and saved model (.joblib)
├── tests/      # Pytest unit tests
├── pyproject.toml
└── README.md

## Requirements
- Python 3.14
- pip

## Setup

Install uv:
```bash
pip install uv
```

Install dependencies:
```bash
uv sync
```

## Run the app

```bash
uv run uvicorn app.main:app --reload
```

## The service will be available at: http://127.0.0.1:8000

## Train the Model (OPTIONAL)
```bash
uv run ml/train.py
```