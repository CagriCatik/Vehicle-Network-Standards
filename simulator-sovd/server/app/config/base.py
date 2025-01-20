import os

class BaseConfig:
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'super-secret-key')
    # Database configuration can be added here
