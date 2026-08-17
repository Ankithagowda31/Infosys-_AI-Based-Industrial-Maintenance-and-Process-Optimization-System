from flask import Blueprint, request, jsonify

incident_bp = Blueprint("incident", __name__)

incidents = []


@incident_bp.route("/incidents", methods=["GET"])
def get_incidents():
    return jsonify(incidents), 200


@incident_bp.route("/incidents", methods=["POST"])
def add_incident():
    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    data["incident_id"] = len(incidents)
    incidents.append(data)

    return jsonify({"message": "Incident added successfully", "data": data}), 201


@incident_bp.route("/incidents/<int:incident_id>", methods=["GET"])
def get_incident_by_id(incident_id):

    if incident_id < 0 or incident_id >= len(incidents):
        return jsonify({"error": "Incident not found"}), 404

    return jsonify(incidents[incident_id]), 200


@incident_bp.route("/incidents/<int:incident_id>", methods=["PUT"])
def update_incident(incident_id):

    if incident_id < 0 or incident_id >= len(incidents):
        return jsonify({"error": "Incident not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    data["incident_id"] = incident_id
    incidents[incident_id] = data

    return jsonify({"message": "Incident updated successfully", "data": data}), 200


@incident_bp.route("/incidents/<int:incident_id>", methods=["DELETE"])
def delete_incident(incident_id):

    if incident_id < 0 or incident_id >= len(incidents):
        return jsonify({"error": "Incident not found"}), 404

    deleted = incidents.pop(incident_id)

    return jsonify({"message": "Incident deleted successfully", "data": deleted}), 200
