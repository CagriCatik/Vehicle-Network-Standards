from .base import BaseConfig

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    ENV = 'development'
    # Additional development-specific configs
