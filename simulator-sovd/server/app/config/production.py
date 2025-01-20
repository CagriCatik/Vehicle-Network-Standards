from .base import BaseConfig

class ProductionConfig(BaseConfig):
    DEBUG = False
    ENV = 'production'
    # Additional production-specific configs
