from flask import Blueprint, request, jsonify

maintenance_bp = Blueprint("maintenance", __name__)

maintenance_data = []


@maintenance_bp.route("/maintenance", methods=["GET"])
def get_maintenance():
    """Get all maintenance records
    ---
    tags:
      - Maintenance
    responses:
      200:
        description: Maintenance records
    """
    return jsonify(maintenance_data), 200


@maintenance_bp.route("/maintenance", methods=["POST"])
def add_maintenance():
    """Add maintenance record
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
              example: RA001
            description:
              type: string
              example: Motor inspection
            status:
              type: string
              example: Pending
    responses:
      201:
        description: Maintenance record added
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    maintenance_id = len(maintenance_data)

    data["maintenance_id"] = maintenance_id

    maintenance_data.append(data)

    return (
        jsonify({"message": "Maintenance record added successfully", "data": data}),
        201,
    )


@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["GET"])
def get_maintenance_by_id(maintenance_id):
    """Get maintenance record by ID
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Maintenance record
      404:
        description: Maintenance record not found
    """

    if maintenance_id < 0 or maintenance_id >= len(maintenance_data):
        return jsonify({"error": "Maintenance record not found"}), 404

    return jsonify(maintenance_data[maintenance_id]), 200


@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["PUT"])
def update_maintenance(maintenance_id):
    """Update maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
    consumes:
      - application/json
    responses:
      200:
        description: Maintenance record updated
      404:
        description: Maintenance record not found
    """

    if maintenance_id < 0 or maintenance_id >= len(maintenance_data):
        return jsonify({"error": "Maintenance record not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    data["maintenance_id"] = maintenance_id

    maintenance_data[maintenance_id] = data

    return (
        jsonify({"message": "Maintenance record updated successfully", "data": data}),
        200,
    )


@maintenance_bp.route("/maintenance/<int:maintenance_id>", methods=["DELETE"])
def delete_maintenance(maintenance_id):
    """Delete maintenance record
    ---
    tags:
      - Maintenance
    parameters:
      - name: maintenance_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Maintenance record deleted
      404:
        description: Maintenance record not found
    """

    if maintenance_id < 0 or maintenance_id >= len(maintenance_data):
        return jsonify({"error": "Maintenance record not found"}), 404

    deleted = maintenance_data.pop(maintenance_id)

    return (
        jsonify(
            {"message": "Maintenance record deleted successfully", "data": deleted}
        ),
        200,
    )
