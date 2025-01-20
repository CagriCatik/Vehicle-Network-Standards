from .development import DevelopmentConfig
from .production import ProductionConfig

configurations = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
