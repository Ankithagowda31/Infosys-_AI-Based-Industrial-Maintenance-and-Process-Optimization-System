from flask import Blueprint, request, jsonify

notification_bp = Blueprint("notification", __name__)

notifications = []


@notification_bp.route("/notifications", methods=["GET"])
def get_notifications():
    """
    Get notifications
    ---
    tags:
      - Notification
    responses:
      200:
        description: Notification list
    """

    return jsonify(notifications)


@notification_bp.route("/notifications", methods=["POST"])
def add_notification():
    """
    Add notification
    ---
    tags:
      - Notification
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            message:
              type: string
              example: Maintenance required
            type:
              type: string
              example: Warning
    responses:
      201:
        description: Notification created
    """

    data = request.get_json()

    notifications.append(data)

    return jsonify({"message": "Notification added successfully", "data": data}), 201
