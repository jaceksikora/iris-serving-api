import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "ml" / "iris_model.joblib"

TARGET_NAMES = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

model = joblib.load(MODEL_PATH)

def predict(features: list[float]) -> dict:
    prediction = model.predict([features])
    class_index = int(prediction[0])

    return {
        "prediction": class_index,
        "flower_type": TARGET_NAMES[class_index],
    }