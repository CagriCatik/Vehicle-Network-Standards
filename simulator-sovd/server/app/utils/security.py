from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, get_jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            verify_jwt_in_request()
            current_user = get_jwt_identity()
        except:
            return jsonify({"error": "Unauthorized"}), 401
        return f(current_user, *args, **kwargs)
    return decorated




def roles_required(required_roles):
    def decorator(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            user_role = claims.get('role', None)
            if user_role not in required_roles:
                return jsonify({"error": "Forbidden: Insufficient privileges"}), 403
            current_user = get_jwt_identity()
            return f(current_user, *args, **kwargs)
        return decorated
    return decorator
