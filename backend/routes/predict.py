from flask import Blueprint, request, jsonify
import joblib
import os

predict_bp = Blueprint("predict", __name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")

model = joblib.load(MODEL_PATH)


@predict_bp.route("/predict", methods=["POST"])
def predict():
    """
    Predict machine maintenance status
    ---
    tags:
      - Prediction
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            temperature:
              type: number
              example: 45
            vibration:
              type: number
              example: 5
    responses:
      200:
        description: Prediction result
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    temperature = data.get("temperature")
    vibration = data.get("vibration")

    if temperature is None or vibration is None:
        return jsonify({"error": "temperature and vibration are required"}), 400

    prediction = model.predict([[temperature, vibration]])

    return jsonify(
        {
            "temperature": temperature,
            "vibration": vibration,
            "prediction": str(prediction[0]),
        }
    )
