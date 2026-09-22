from ml.predict import predict_maintenance


def get_prediction(temperature, pressure, vibration):
    result = predict_maintenance(temperature, pressure, vibration)
    return result
