from flask import Blueprint, request, jsonify

notification_bp = Blueprint("notification", __name__)


# =====================================================
# SAMPLE NOTIFICATIONS
# =====================================================

notifications = [
    {
        "notification_id": 1,
        "robot_id": "RA001",
        "type": "Warning",
        "message": "Maintenance required for Robot RA001",
        "status": "Unread",
        "date": "2026-08-25",
    },
    {
        "notification_id": 2,
        "robot_id": "RA002",
        "type": "Alert",
        "message": "High temperature detected",
        "status": "Unread",
        "date": "2026-08-26",
    },
    {
        "notification_id": 3,
        "robot_id": "RA003",
        "type": "Information",
        "message": "Preventive maintenance completed",
        "status": "Read",
        "date": "2026-08-27",
    },
]


# =====================================================
# GET ALL NOTIFICATIONS
# =====================================================


@notification_bp.route("/notifications", methods=["GET"])
def get_notifications():
    """
    Get all notifications
    ---
    tags:
      - Notification
    responses:
      200:
        description: Notification list
    """

    return jsonify(notifications), 200


# =====================================================
# GET NOTIFICATION BY ID
# =====================================================


@notification_bp.route("/notifications/<int:notification_id>", methods=["GET"])
def get_notification_by_id(notification_id):
    """
    Get notification by ID
    ---
    tags:
      - Notification
    """

    for notification in notifications:

        if notification["notification_id"] == notification_id:

            return jsonify(notification), 200

    return jsonify({"error": "Notification not found"}), 404


# =====================================================
# ADD NOTIFICATION
# =====================================================


@notification_bp.route("/notifications", methods=["POST"])
def add_notification():
    """
    Add notification
    ---
    tags:
      - Notification
    consumes:
      - application/json
    """

    data = request.get_json()

    if not data:

        return jsonify({"error": "JSON data is required"}), 400

    data["notification_id"] = len(notifications) + 1

    notifications.append(data)

    return jsonify({"message": "Notification added successfully", "data": data}), 201


# =====================================================
# UPDATE NOTIFICATION
# =====================================================


@notification_bp.route("/notifications/<int:notification_id>", methods=["PUT"])
def update_notification(notification_id):
    """
    Update notification
    ---
    tags:
      - Notification
    """

    data = request.get_json()

    if not data:

        return jsonify({"error": "JSON data is required"}), 400

    for index, notification in enumerate(notifications):

        if notification["notification_id"] == notification_id:

            data["notification_id"] = notification_id

            notifications[index] = data

            return (
                jsonify({"message": "Notification updated successfully", "data": data}),
                200,
            )

    return jsonify({"error": "Notification not found"}), 404


# =====================================================
# DELETE NOTIFICATION
# =====================================================


@notification_bp.route("/notifications/<int:notification_id>", methods=["DELETE"])
def delete_notification(notification_id):
    """
    Delete notification
    ---
    tags:
      - Notification
    """

    for index, notification in enumerate(notifications):

        if notification["notification_id"] == notification_id:

            deleted = notifications.pop(index)

            return (
                jsonify(
                    {"message": "Notification deleted successfully", "data": deleted}
                ),
                200,
            )

    return jsonify({"error": "Notification not found"}), 404
