import joblib

model = joblib.load("ml/model.pkl")


def predict_maintenance(temperature, pressure, vibration):
    input_data = [[temperature, pressure, vibration]]
    prediction = model.predict(input_data)
    return prediction[0]
