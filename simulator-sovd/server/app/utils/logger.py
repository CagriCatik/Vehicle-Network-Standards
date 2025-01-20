import logging
from logging.handlers import RotatingFileHandler
import os

def setup_logger():
    logger = logging.getLogger('sovd_server')
    logger.setLevel(logging.DEBUG)  # Set to DEBUG for comprehensive logging
    
    # Ensure logs directory exists
    if not os.path.exists('logs'):
        os.makedirs('logs')
    
    # Create handlers
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    file_handler = RotatingFileHandler('logs/sovd_server.log', maxBytes=5*1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatter and add to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    
    return logger
