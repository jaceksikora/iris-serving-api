from fastapi import APIRouter

from app.schemas import IrisInput
from app.service import predict

router = APIRouter()

@router.post("/predict")
def predict_iris(iris: IrisInput):
    features = [
        iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width
    ]

    return predict(features)
