from flask import Flask
import os
from app.config import app_config
from app.db import DatabaseConnection

APP_ENV = os.environ.get('APP_ENV', 'development')

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[str(config_name)])

    from app.api.v1.auth.views import mod as auth
    from app.api.v1.entries.views import mod as entry

    app.register_blueprint(auth, url_prefix='/api/v1/auth')
    app.register_blueprint(entry, url_prefix='/api/v1/entries')

    DatabaseConnection(config_name).create_users_table()
    DatabaseConnection(config_name).create_entries_table()
    
    return app
