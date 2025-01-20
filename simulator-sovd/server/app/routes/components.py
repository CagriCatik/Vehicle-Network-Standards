from flask import Blueprint, request, jsonify
from app.models import Component, Fault
import logging
from app.utils.security import token_required

components_bp = Blueprint('components', __name__)
logger = logging.getLogger('sovd_server')

# In-memory storage for components
components = {
    "engine": Component(
        id="engine",
        name="Engine ECU",
        faults=[],
        data={"vin": "V123456789", "rpm": 800, "temperature": 90}
    ),
    "door": Component(
        id="door",
        name="Door ECU",
        faults=[Fault(code="1234", description="Door open error", severity="high")],
        data={"status": "closed"}
    ),
    "transmission": Component(
        id="transmission",
        name="Transmission ECU",
        faults=[Fault(code="5678", description="Transmission fluid low", severity="medium")],
        data={"gear": "P", "fluid_level": "Low"}
    )
}

@components_bp.route('/components', methods=['GET'])
@token_required
def list_components(current_user):
    """List all available components."""
    logger.info(f"User '{current_user}' requested list of components.")
    return jsonify({"items": [comp.__dict__ for comp in components.values()]}), 200

@components_bp.route('/components/<component_id>/faults', methods=['GET'])
@token_required
def get_faults(current_user, component_id):
    """Retrieve faults for a specific component with optional filtering."""
    component = components.get(component_id)
    if not component:
        logger.warning(f"Component '{component_id}' not found.")
        return jsonify({"error": "Component not found"}), 404
    
    # Filtering parameters
    severity = request.args.get('severity')
    status = request.args.get('status')  # Future implementation
    
    faults = component.faults
    if severity:
        faults = [fault for fault in faults if fault.severity.lower() == severity.lower()]
    if status:
        faults = [fault for fault in faults if fault.status.lower() == status.lower()]
    
    logger.info(f"User '{current_user}' retrieved faults for component '{component_id}' with filters - Severity: {severity}, Status: {status}")
    return jsonify({"items": [fault.__dict__ for fault in faults]}), 200

@components_bp.route('/components/<component_id>/data', methods=['GET'])
@token_required
def get_data(current_user, component_id):
    """Retrieve data for a specific component based on category."""
    component = components.get(component_id)
    if not component:
        logger.warning(f"Component '{component_id}' not found.")
        return jsonify({"error": "Component not found"}), 404
    
    categories = request.args.get('categories', '')
    category_list = [cat.strip() for cat in categories.split(',') if cat.strip()]
    
    if not category_list:
        logger.error("No categories specified in data request.")
        return jsonify({"error": "No categories specified"}), 400
    
    data_response = {}
    for category in category_list:
        if category == "identData":
            data_response["identData"] = [{"id": key.upper(), "value": value} for key, value in component.data.items() if key.lower() == "vin"]
        elif category == "operationalData":
            data_response["operationalData"] = [{"id": key, "value": value} for key, value in component.data.items() if key.lower() != "vin"]
        else:
            logger.error(f"Invalid category requested: {category}")
            return jsonify({"error": f"Invalid category: {category}"}), 400
    
    logger.info(f"User '{current_user}' retrieved data for component '{component_id}' with categories: {categories}")
    return jsonify(data_response), 200
