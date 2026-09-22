from flask import Blueprint, request, jsonify

incident_bp = Blueprint("incident", __name__)

incidents = [
    {
        "incident_id": 1,
        "robot_id": "RA001",
        "incident_type": "High Temperature",
        "severity": "High",
        "description": "Robot temperature exceeded normal limit",
        "status": "Open",
    },
    {
        "incident_id": 2,
        "robot_id": "RA002",
        "incident_type": "Sensor Warning",
        "severity": "Medium",
        "description": "Abnormal sensor reading detected",
        "status": "Resolved",
    },
]


@incident_bp.route("/incidents", methods=["GET"])
def get_incidents():
    """
    Get all incidents
    ---
    tags:
      - Incident
    responses:
      200:
        description: List of all incidents
    """
    return jsonify(incidents), 200


@incident_bp.route("/incidents", methods=["POST"])
def add_incident():
    """
    Add a new incident
    ---
    tags:
      - Incident
    parameters:
      - in: body
        name: incident
        required: true
        schema:
          type: object
          properties:
            robot_id:
              type: string
            incident_type:
              type: string
            severity:
              type: string
            description:
              type: string
            status:
              type: string
    responses:
      201:
        description: Incident added successfully
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    new_id = len(incidents) + 1

    incident = {
        "incident_id": new_id,
        "robot_id": data.get("robot_id"),
        "incident_type": data.get("incident_type"),
        "severity": data.get("severity"),
        "description": data.get("description"),
        "status": data.get("status", "Open"),
    }

    incidents.append(incident)

    return jsonify({"message": "Incident added successfully", "data": incident}), 201


@incident_bp.route("/incidents/<int:incident_id>", methods=["GET"])
def get_incident_by_id(incident_id):
    """
    Get incident by ID
    ---
    tags:
      - Incident
    parameters:
      - name: incident_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Incident found
      404:
        description: Incident not found
    """
    for incident in incidents:
        if incident["incident_id"] == incident_id:
            return jsonify(incident), 200

    return jsonify({"error": "Incident not found"}), 404


@incident_bp.route("/incidents/<int:incident_id>", methods=["PUT"])
def update_incident(incident_id):
    """
    Update an incident
    ---
    tags:
      - Incident
    parameters:
      - name: incident_id
        in: path
        required: true
        type: integer
      - in: body
        name: incident
        required: true
        schema:
          type: object
    responses:
      200:
        description: Incident updated successfully
      404:
        description: Incident not found
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    for incident in incidents:

        if incident["incident_id"] == incident_id:

            incident.update(data)
            incident["incident_id"] = incident_id

            return (
                jsonify({"message": "Incident updated successfully", "data": incident}),
                200,
            )

    return jsonify({"error": "Incident not found"}), 404


@incident_bp.route("/incidents/<int:incident_id>", methods=["DELETE"])
def delete_incident(incident_id):
    """
    Delete an incident
    ---
    tags:
      - Incident
    parameters:
      - name: incident_id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Incident deleted successfully
      404:
        description: Incident not found
    """
    for i, incident in enumerate(incidents):

        if incident["incident_id"] == incident_id:

            deleted = incidents.pop(i)

            return (
                jsonify({"message": "Incident deleted successfully", "data": deleted}),
                200,
            )

    return jsonify({"error": "Incident not found"}), 404
