from app.service import predict

def test_service_prediction():
    result = predict([5.1, 3.5, 1.4, 0.2])

    assert "flower_type" in result
    assert result["flower_type"] in [
        "Iris-setosa",
        "Iris-versicolor",
        "Iris-virginica"
    ]