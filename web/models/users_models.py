"""
User models for the application.
"""
# Imports
from datetime import datetime
from flask import redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from login_config import login_manager
from app import db


# Login Manager - User Loader
@login_manager.user_loader
def load_user(user_id):
    """Loads the user from the database"""
    return User.query.get(int(user_id))


# Login Manager - Unauthorized Handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirects unauthorized users to the login page"""
    return redirect(url_for("users.login"))


# Model - User
class User(db.Model, UserMixin):
    """User model"""

    __tablename__ = "users"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    # Login Information
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.Text, nullable=False)
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.now())
    updated_date = db.Column(db.DateTime)
    # User Type
    user_type = db.Column(db.String(100), nullable=False)
    # Role
    role = db.Column(db.String(100), default="user")
    # Status
    status = db.Column(db.String(10), default="ACTIVE")

    def check_password(self, password):
        """Checks if the password is correct"""
        return check_password_hash(self.password_hash, password)
