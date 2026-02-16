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

### Testing the API (curl Examples)

Below are ready-to-use `curl` commands to test the `/predict` endpoint for three different Iris species.

#### 1. Setosa
```bash
curl --location 'http://127.0.0.1:8000/predict' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}'
```

#### 2. Versicolor
```bash
curl --location 'http://127.0.0.1:8000/predict' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "sepal_length": 6.0,
  "sepal_width": 3.0,
  "petal_length": 4.5,
  "petal_width": 1.5
}'
```

#### 3. Virginica
```bash
curl --location 'http://127.0.0.1:8000/predict' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "sepal_length": 7.3,
  "sepal_width": 2.9,
  "petal_length": 6.3,
  "petal_width": 1.8
}'
```
