from flask import Flask
from app.config import configuration

def create_app(environment):
    app = Flask(__name__)
    app.config.from_object(configuration[environment])

    from app.api.v1.auth.views import mod as auth

    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    
    return app
