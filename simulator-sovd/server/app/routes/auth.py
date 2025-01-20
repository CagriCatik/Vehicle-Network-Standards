from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
import logging

auth_bp = Blueprint('auth', __name__)
logger = logging.getLogger('sovd_server')

# In-memory user storage for demonstration; replace with database in production
users = {
    "admin": generate_password_hash("adminpass"),
    "tester": generate_password_hash("testerpass")
}

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        logger.warning("Authentication attempt with missing credentials.")
        return jsonify({"error": "Username and password required"}), 400
    
    user_password_hash = users.get(username)
    if user_password_hash and check_password_hash(user_password_hash, password):
        access_token = create_access_token(identity=username)
        logger.info(f"User '{username}' authenticated successfully.")
        return jsonify(access_token=access_token), 200
    else:
        logger.warning(f"Authentication failed for user '{username}'.")
        return jsonify({"error": "Invalid credentials"}), 401


from flask_jwt_extended import create_access_token

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        logger.warning("Authentication attempt with missing credentials.")
        return jsonify({"error": "Username and password required"}), 400
    
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
        logger.info(f"User '{username}' authenticated successfully.")
        return jsonify(access_token=access_token), 200
    else:
        logger.warning(f"Authentication failed for user '{username}'.")
        return jsonify({"error": "Invalid credentials"}), 401
