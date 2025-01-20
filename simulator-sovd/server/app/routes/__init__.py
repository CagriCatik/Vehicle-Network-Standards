from .components import components_bp
from .operations import operations_bp
from .auth import auth_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(components_bp)
    app.register_blueprint(operations_bp)
