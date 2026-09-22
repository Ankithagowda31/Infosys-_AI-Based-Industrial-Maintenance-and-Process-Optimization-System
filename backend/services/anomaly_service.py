def detect_anomaly(temperature, vibration):
    if temperature > 70 or vibration > 10:
        return "Anomaly Detected"
    return "Normal"
