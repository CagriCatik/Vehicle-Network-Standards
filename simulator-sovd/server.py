from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated ECU Data
components = {
    "engine": {
        "id": "engine",
        "name": "Engine ECU",
        "faults": [],
        "data": {"vin": "V123456789", "rpm": 800, "temperature": 90}
    },
    "door": {
        "id": "door",
        "name": "Door ECU",
        "faults": [{"code": "1234", "description": "Door open error"}],
        "data": {"status": "closed"}
    },
    "transmission": {
        "id": "transmission",
        "name": "Transmission ECU",
        "faults": [{"code": "5678", "description": "Transmission fluid low"}],
        "data": {"gear": "P", "fluid_level": "Low"}
    }
}

@app.route('/components', methods=['GET'])
def list_components():
    """List all available components."""
    return jsonify({"items": list(components.values())}), 200

@app.route('/components/<component_id>/faults', methods=['GET'])
def get_faults(component_id):
    """Retrieve faults for a specific component."""
    component = components.get(component_id)
    if not component:
        return jsonify({"error": "Component not found"}), 404
    return jsonify({"items": component["faults"]}), 200

@app.route('/components/<component_id>/data', methods=['GET'])
def get_data(component_id):
    """Retrieve data for a specific component based on category."""
    component = components.get(component_id)
    if not component:
        return jsonify({"error": "Component not found"}), 404
    
    categories = request.args.get('categories', '')
    category_list = [cat.strip() for cat in categories.split(',') if cat.strip()]
    
    if not category_list:
        return jsonify({"error": "No categories specified"}), 400
    
    data_response = {}
    for category in category_list:
        if category == "identData":
            data_response["identData"] = [{"id": key, "value": value} for key, value in component["data"].items() if key in ["vin"]]
        elif category == "operationalData":
            data_response["operationalData"] = [{"id": key, "value": value} for key, value in component["data"].items() if key not in ["vin"]]
        else:
            return jsonify({"error": f"Invalid category: {category}"}), 400
    
    return jsonify(data_response), 200

@app.route('/components/<component_id>/operations', methods=['POST'])
def execute_operation(component_id):
    """Execute an operation on a specific component."""
    component = components.get(component_id)
    if not component:
        return jsonify({"error": "Component not found"}), 404
    
    operation = request.json.get("operation")
    if not operation:
        return jsonify({"error": "No operation specified"}), 400
    
    # Example operation handling
    if operation == "reset":
        # Reset faults
        component["faults"] = []
        return jsonify({"message": f"{component['name']} reset successfully"}), 200
    elif operation == "lock":
        # Simulate locking the component
        return jsonify({"message": f"{component['name']} locked successfully"}), 200
    elif operation == "unlock":
        # Simulate unlocking the component
        return jsonify({"message": f"{component['name']} unlocked successfully"}), 200
    else:
        return jsonify({"error": "Unsupported operation"}), 400

@app.route('/components/<component_id>/faults', methods=['DELETE'])
def clear_faults(component_id):
    """Clear specific fault codes for a component."""
    component = components.get(component_id)
    if not component:
        return jsonify({"error": "Component not found"}), 404
    
    fault_code = request.args.get('code')
    if not fault_code:
        return jsonify({"error": "No fault code specified"}), 400
    
    initial_faults = len(component["faults"])
    component["faults"] = [fault for fault in component["faults"] if fault["code"] != fault_code]
    if len(component["faults"]) < initial_faults:
        return jsonify({"message": f"Fault code {fault_code} cleared"}), 200
    else:
        return jsonify({"error": f"Fault code {fault_code} not found"}), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
