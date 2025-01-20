import os

class Config:
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    TESTING = True
