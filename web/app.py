"""
Flask application initialization and configuration.
"""
# Imports
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import BaseConfig


# Flask initialization
app = Flask(__name__)
# Base configuration
app.config.from_object(BaseConfig)
# Database initialization
db = SQLAlchemy(app)


# Importing the models to create the tables
from users.models import *
from healthapps.models import *
from request.models import *
from settings.models import *


# Login manager initialization
from login_config import login_manager
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# Mail configuration and initialization
mail = Mail(app)
mail.init_app(app)


# Flask Blueprints - Imports
from core.views import core_bp
from users.views import users_bp
from healthapps.views import healthapps_bp
from request.views import requests_bp
from reports.views import reports_bp
from settings.views import settings_bp

# Flask Blueprints - Register
app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
app.register_blueprint(healthapps_bp)
app.register_blueprint(requests_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(settings_bp)


# Main function
if __name__ == "__main__":
    app.run()
