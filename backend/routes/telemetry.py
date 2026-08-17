from flask import Blueprint, jsonify

telemetry_bp = Blueprint("telemetry", __name__)


@telemetry_bp.route("/telemetry", methods=["GET"])
def get_telemetry():
    """
    Get telemetry data
    ---
    tags:
      - Telemetry
    responses:
      200:
        description: Telemetry information
    """

    return jsonify(
        {
            "temperature": 45,
            "vibration": 5,
            "pressure": 100,
            "speed": 1200,
            "status": "Normal",
        }
    )
