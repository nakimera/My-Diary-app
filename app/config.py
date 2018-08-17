import os

class Config:
    SECRET_KEY = "TcQsWISFjRG4243XobHPIaDxMioisOba"
    DEBUG = False
    TESTING = False 
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DATABASE_URL = os.environ.get("DATABASE_URL")

class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = os.environ.get("TEST_DATABASE_URL")

class ProductionConfig(Config):
    DEBUG = False
    DATABASE_URL = os.environ.get("DATABASE_URL")
    
app_config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}