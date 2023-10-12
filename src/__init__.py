"""
Initialization and configuration for the application.
"""


# Imports
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail


# Read .env file
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


# Flask initialization
app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY

# Database Path
database_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                             'data', 'database.db')

# Ensure the 'data' directory exists; if not, create it
os.makedirs(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data'),
            exist_ok=True)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + database_path


# Database initialization
db = SQLAlchemy(app)


# Migrations initialization
Migrate(app, db)


# Function to create the database if it doesn't exist
def create_database_if_not_exists():
    """Create the database if it doesn't exist."""

    try:
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        engine.connect()
    except OperationalError:
        db.create_all()


# Login manager initialization
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "users.login"


# Mail configuration and initialization
mail = Mail()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rodneygauna@gmail.com'
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
mail.init_app(app)


# Flask Blueprints - Imports
from src.cli.cli_commands import commands_bp
from src.core.views import core_bp
from src.users.views import users_bp
from src.healthapps.views import healthapps_bp
from src.request.views import requests_bp
from src.reports.views import reports_bp
from src.settings.views import settings_bp

# Flask Blueprints - Register
app.register_blueprint(commands_bp)
app.register_blueprint(core_bp)
app.register_blueprint(users_bp)
app.register_blueprint(healthapps_bp)
app.register_blueprint(requests_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(settings_bp)
