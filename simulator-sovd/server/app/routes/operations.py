from flask import Blueprint, request, jsonify
from app.models import Component
import logging
from app.utils.security import token_required

operations_bp = Blueprint('operations', __name__)
logger = logging.getLogger('sovd_server')

@operations_bp.route('/components/<component_id>/operations', methods=['POST'])
@token_required
def execute_operation(current_user, component_id):
    """Execute an operation on a specific component."""
    component = components.get(component_id)
    if not component:
        logger.warning(f"Component '{component_id}' not found for operation.")
        return jsonify({"error": "Component not found"}), 404
    
    operation = request.json.get("operation")
    if not operation:
        logger.error("No operation specified in request.")
        return jsonify({"error": "No operation specified"}), 400
    
    logger.info(f"User '{current_user}' is executing operation '{operation}' on component '{component_id}'.")
    
    if component.locked and component.lock_id != current_user:
        logger.warning(f"Component '{component_id}' is locked by another user.")
        return jsonify({"error": "Component is locked by another user"}), 403
    
    if operation == "reset":
        component.reset_faults()
        logger.info(f"Faults reset for component '{component_id}' by user '{current_user}'.")
        return jsonify({"message": f"{component.name} reset successfully"}), 200
    elif operation == "lock":
        success = component.lock_component(requester_id=current_user)
        if success:
            logger.info(f"Component '{component_id}' locked by user '{current_user}'.")
            return jsonify({"message": f"{component.name} locked successfully"}), 200
        else:
            logger.warning(f"Component '{component_id}' is already locked.")
            return jsonify({"error": "Component is already locked"}), 403
    elif operation == "unlock":
        success = component.unlock_component(requester_id=current_user)
        if success:
            logger.info(f"Component '{component_id}' unlocked by user '{current_user}'.")
            return jsonify({"message": f"{component.name} unlocked successfully"}), 200
        else:
            logger.warning(f"User '{current_user}' attempted to unlock component '{component_id}' not locked by them.")
            return jsonify({"error": "Cannot unlock component not locked by you"}), 403
    else:
        logger.error(f"Unsupported operation '{operation}' requested by user '{current_user}'.")
        return jsonify({"error": "Unsupported operation"}), 400

@operations_bp.route('/components/<component_id>/faults', methods=['DELETE'])
@token_required
def clear_faults(current_user, component_id):
    """Clear specific fault codes for a component."""
    component = components.get(component_id)
    if not component:
        logger.warning(f"Component '{component_id}' not found for clearing faults.")
        return jsonify({"error": "Component not found"}), 404
    
    fault_code = request.args.get('code')
    if not fault_code:
        logger.error("No fault code specified for clearing.")
        return jsonify({"error": "No fault code specified"}), 400
    
    if component.locked and component.lock_id != current_user:
        logger.warning(f"Component '{component_id}' is locked by another user.")
        return jsonify({"error": "Component is locked by another user"}), 403
    
    success = component.clear_fault_code(fault_code)
    if success:
        logger.info(f"Fault code '{fault_code}' cleared for component '{component_id}' by user '{current_user}'.")
        return jsonify({"message": f"Fault code {fault_code} cleared"}), 200
    else:
        logger.warning(f"Fault code '{fault_code}' not found in component '{component_id}'.")
        return jsonify({"error": f"Fault code {fault_code} not found"}), 404


from app.utils.security import token_required, roles_required

@operations_bp.route('/components/<component_id>/operations', methods=['POST'])
@token_required
@roles_required(['admin', 'tester'])  # Only admin and tester can perform operations
def execute_operation(current_user, component_id):
    # Existing operation code
    pass
