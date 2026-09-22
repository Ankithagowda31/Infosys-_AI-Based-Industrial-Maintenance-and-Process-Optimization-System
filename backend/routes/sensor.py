from flask import Blueprint, jsonify

sensor_bp = Blueprint("sensor", __name__)


@sensor_bp.route("/sensors", methods=["GET"])
def get_sensor():
    """
    Get sensor data
    ---
    tags:
      - Sensor
    responses:
      200:
        description: Sensor data
    """

    return jsonify(
        {"temperature": 45, "vibration": 5, "pressure": 100, "status": "Normal"}
    )
