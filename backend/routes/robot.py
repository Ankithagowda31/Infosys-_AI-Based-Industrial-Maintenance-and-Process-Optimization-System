from flask import Blueprint, jsonify

robot_bp = Blueprint("robot", __name__)


@robot_bp.route("/robots", methods=["GET"])
def get_robot():
    """
    Get robot information
    ---
    tags:
      - Robot
    responses:
      200:
        description: Robot information
    """

    return jsonify(
        {
            "robot_id": "RA001",
            "robot_name": "Industrial Robotic Arm",
            "machine_type": "6-Axis Robot",
            "location": "Production Line 1",
            "status": "Active",
        }
    )
