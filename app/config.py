db_user = 'postgres'
user_password = 'postgres'
db_name = 'mydiary'

class Config:
    SECRET_KEY = "TcQsWISFjRG4243XobHPIaDxMioisOba"
    DEBUG = False
    TESTING = False 
    DEVELOPMENT = False

class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DATABASE_URL = 'postgresql://'+ db_user +': '+ user_password + '@localhost/'+ db_name +''

class TestingConfig(Config):
    TESTING = True
    DATABASE_URL = ''

class ProductionConfig(Config):
    DEBUG = False
    
app_config = {
    "development" : DevelopmentConfig,
    "testing" : TestingConfig,
    "production" : ProductionConfig
}