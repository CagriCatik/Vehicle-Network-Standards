from flask import Flask
from app.config import configurations
from app.routes import register_blueprints
from app.utils.errors import register_error_handlers
from app.utils.logger import setup_logger
from app.services.real_time_simulator import RealTimeSimulator
from app.protocols.can_bus_simulator import CANBusSimulator

def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(configurations[env])
    
    # Setup Logger
    logger = setup_logger()
    app.logger = logger
    
    # Register Blueprints
    register_blueprints(app)
    
    # Register Error Handlers
    register_error_handlers(app, logger)
    
    # Initialize Real-Time Simulator
    simulator = RealTimeSimulator(components=app.blueprints['components'].components)
    simulator.start()
    
    # Initialize CAN Bus Simulator
    can_simulator = CANBusSimulator(components=app.blueprints['components'].components)
    can_simulator.start()
    
    # Ensure simulators stop when the app context is torn down
    @app.teardown_appcontext
    def shutdown_simulators(exception=None):
        simulator.stop()
        can_simulator.stop()
    
    return app



def create_app(env='development'):
    app = Flask(__name__)
    app.config.from_object(configurations[env])
    
    # Setup Logger
    logger = setup_logger()
    app.logger = logger
    
    # Register Blueprints
    register_blueprints(app)
    
    # Register Error Handlers
    register_error_handlers(app, logger)
    
    # Initialize Real-Time Simulator
    simulator = RealTimeSimulator(components=app.blueprints['components'].components)
    simulator.start()
    
    # Ensure simulator stops when the app context is torn down
    @app.teardown_appcontext
    def shutdown_simulator(exception=None):
        simulator.stop()
    
    return app
