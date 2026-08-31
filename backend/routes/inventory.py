from flask import Blueprint, request, jsonify

inventory_bp = Blueprint("inventory", __name__)

# Temporary inventory storage
inventory_data = [
    {"item_name": "Motor", "quantity": 10, "status": "Available"},
    {"item_name": "Motor", "quantity": 10, "status": "Available"},
    {"item_name": "Motor", "quantity": 10, "status": "Available"},
]


# --------------------------------------------------
# GET ALL INVENTORY
# --------------------------------------------------


@inventory_bp.route("/inventory", methods=["GET"])
def get_inventory():
    """
    Get inventory
    ---
    tags:
      - Inventory
    responses:
      200:
        description: Inventory list
    """

    return jsonify(inventory_data), 200


# --------------------------------------------------
# ADD INVENTORY
# --------------------------------------------------


@inventory_bp.route("/inventory", methods=["POST"])
def add_inventory():
    """
    Add inventory
    ---
    tags:
      - Inventory
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            item_name:
              type: string
              example: Motor
            quantity:
              type: integer
              example: 10
            status:
              type: string
              example: Available
    responses:
      201:
        description: Inventory added
    """

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    item_name = data.get("item_name")
    quantity = data.get("quantity")
    status = data.get("status")

    if item_name is None or quantity is None or status is None:
        return jsonify({"error": "item_name, quantity and status are required"}), 400

    inventory_data.append(
        {"item_name": item_name, "quantity": quantity, "status": status}
    )

    return (
        jsonify(
            {"message": "Inventory added successfully", "data": inventory_data[-1]}
        ),
        201,
    )


# --------------------------------------------------
# GET INVENTORY BY ID
# --------------------------------------------------


@inventory_bp.route("/inventory/<int:inventory_id>", methods=["GET"])
def get_inventory_by_id(inventory_id):
    """
    Get inventory by ID
    ---
    tags:
      - Inventory
    parameters:
      - name: inventory_id
        in: path
        required: true
        type: integer
        description: Inventory ID
        example: 0
    responses:
      200:
        description: Inventory record
      404:
        description: Inventory not found
    """

    if inventory_id < 0 or inventory_id >= len(inventory_data):
        return jsonify({"error": "Inventory not found"}), 404

    return jsonify(inventory_data[inventory_id]), 200


# --------------------------------------------------
# UPDATE INVENTORY
# --------------------------------------------------


@inventory_bp.route("/inventory/<int:inventory_id>", methods=["PUT"])
def update_inventory(inventory_id):
    """
    Update inventory
    ---
    tags:
      - Inventory
    parameters:
      - name: inventory_id
        in: path
        required: true
        type: integer
        description: Inventory ID
        example: 0
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            item_name:
              type: string
              example: Motor
            quantity:
              type: integer
              example: 20
            status:
              type: string
              example: Available
    responses:
      200:
        description: Inventory updated
      404:
        description: Inventory not found
    """

    if inventory_id < 0 or inventory_id >= len(inventory_data):
        return jsonify({"error": "Inventory not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON data is required"}), 400

    inventory_data[inventory_id] = {
        "item_name": data.get("item_name"),
        "quantity": data.get("quantity"),
        "status": data.get("status"),
    }

    return (
        jsonify(
            {
                "message": "Inventory updated successfully",
                "data": inventory_data[inventory_id],
            }
        ),
        200,
    )


# --------------------------------------------------
# DELETE INVENTORY
# --------------------------------------------------


@inventory_bp.route("/inventory/<int:inventory_id>", methods=["DELETE"])
def delete_inventory(inventory_id):
    """
    Delete inventory
    ---
    tags:
      - Inventory
    parameters:
      - name: inventory_id
        in: path
        required: true
        type: integer
        description: Inventory ID
        example: 0
    responses:
      200:
        description: Inventory deleted
      404:
        description: Inventory not found
    """

    if inventory_id < 0 or inventory_id >= len(inventory_data):
        return jsonify({"error": "Inventory not found"}), 404

    deleted_item = inventory_data.pop(inventory_id)

    return (
        jsonify({"message": "Inventory deleted successfully", "data": deleted_item}),
        200,
    )
