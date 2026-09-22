from flask import Blueprint, request, jsonify

maintenance_bp = Blueprint("maintenance", __name__)

# Temporary in-memory maintenance records
maintenance_records = [
    {
        "maintenance_id": 1,
        "robot_id": "RA001",
        "maintenance_type": "Preventive Maintenance",
        "description": "Regular inspection",
        "scheduled_date": "2026-08-25",
        "status": "Scheduled",
    }
]


# ---------------------------------------------------
# GET - Get all maintenance records
# ---------------------------------------------------
@maintenance_bp.route("/maintenance", methods=["GET"])
def get_maintenance():
    """
    Get all maintenance records
    ---
    tags:
      - Maintenance
    responses:
      200:
        description: List of maintenance records
    """
    return jsonify(maintenance_records), 200


# ---------------------------------------------------
# POST - Add maintenance record
# ---------------------------------------------------
@maintenance_bp.route("/maintenance", methods=["POST"])
def add_maintenance():
    """
    Add a new maintenance record
    ---
    tags:
      - Maintenance
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            robot_id:
              type: string
              example: RA002
            maintenance_type:
              type: string
              example: Preventive Maintenance
            description:
              type: string
              example: Motor inspection
            scheduled_date:
              type: string
              example: 2026-08-30
            status:
              type: string
              example: Scheduled
    responses:
      201:
        description: Maintenance added successfully
      400:
        description: JSON data is required
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    data["maintenance_id"] = len(maintenance_records) + 1

    maintenance_records.append(data)

    return jsonify({"message": "Maintenance added successfully", "data": data}), 201


# ---------------------------------------------------
# GET - Get maintenance record by ID
# ---------------------------------------------------
@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["GET"])
def get_maintenance_by_id(maintenance_id):
    """
    Get maintenance record by ID
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Maintenance record found
      404:
        description: Maintenance not found
    """

    for record in maintenance_records:

        if record["maintenance_id"] == maintenance_id:
            return jsonify(record), 200

    return jsonify({"error": "Maintenance not found"}), 404


# ---------------------------------------------------
# PUT - Update maintenance record
# ---------------------------------------------------
@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["PUT"])
def update_maintenance(maintenance_id):
    """
    Update maintenance record
    ---
    tags:
      - Maintenance
    consumes:
      - application/json
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        example: 1
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            robot_id:
              type: string
              example: RA001
            maintenance_type:
              type: string
              example: Corrective Maintenance
            description:
              type: string
              example: Motor replacement
            scheduled_date:
              type: string
              example: 2026-09-01
            status:
              type: string
              example: Completed
    responses:
      200:
        description: Maintenance updated successfully
      400:
        description: JSON data is required
      404:
        description: Maintenance not found
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    for index, record in enumerate(maintenance_records):

        if record["maintenance_id"] == maintenance_id:

            data["maintenance_id"] = maintenance_id

            maintenance_records[index] = data

            return (
                jsonify({"message": "Maintenance updated successfully", "data": data}),
                200,
            )

    return jsonify({"error": "Maintenance not found"}), 404


# ---------------------------------------------------
# DELETE - Delete maintenance record
# ---------------------------------------------------
@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["DELETE"])
def delete_maintenance(maintenance_id):
    """
    Delete maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        required: true
        type: integer
        example: 1
    responses:
      200:
        description: Maintenance deleted successfully
      404:
        description: Maintenance not found
    """

    for index, record in enumerate(maintenance_records):

        if record["maintenance_id"] == maintenance_id:

            deleted = maintenance_records.pop(index)

            return (
                jsonify(
                    {"message": "Maintenance deleted successfully", "data": deleted}
                ),
                200,
            )

    return jsonify({"error": "Maintenance not found"}), 404
