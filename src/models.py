"""
Database models for the application.
"""

# Imports
from datetime import datetime
from flask import redirect, url_for
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from src import db, login_manager


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
    password_hash = db.Column(db.String(128))
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Role
    role = db.Column(db.String(100), default="user")
    # Status
    status = db.Column(db.String(10), default="ACTIVE")
    # Profile Picture
    profile_image = db.Column(
        db.String(255), nullable=False, default="default_profile.jpg"
    )

    def check_password(self, password):
        """Checks if the password is correct"""
        return check_password_hash(self.password_hash, password)


# Model - HealthTrio Health Plans
class HealthPlan(db.Model):
    """Health Plans Model"""

    __tablename__ = "health_plans"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    # Health Plan Information
    name = db.Column(db.String(255), nullable=False)
    hp_id = db.Column(db.String(255), nullable=False)
    # Status
    status = db.Column(db.String(10), default="ACTIVE")
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Updatestamps
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))


# Model - Health App
class HealthApp(db.Model):
    """Third-party Health App model"""

    __tablename__ = "health_apps"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    # Web Scraping Source
    source = db.Column(db.Text, nullable=False)
    # App Information
    name = db.Column(db.Text, nullable=False)
    company = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Updatestamps
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))


# Model - Connection Request
class ConnectionRequest(db.Model):
    """Connection Request model"""

    __tablename__ = "connection_requests"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    health_plan_id = db.Column(
        db.Integer, db.ForeignKey("health_plans.id"))
    # Requester Information
    firstname = db.Column(db.String(255), nullable=False)
    lastname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    company = db.Column(db.String(255), nullable=False)
    company_website = db.Column(db.String(255), nullable=False)
    # Application Information
    app_name = db.Column(db.String(255), nullable=False)
    app_link = db.Column(db.String(255), nullable=False)
    app_type_web = db.Column(db.Boolean, nullable=False)
    app_type_mobile = db.Column(db.Boolean, nullable=False)
    app_type_native = db.Column(db.Boolean, nullable=False)
    app_type_other = db.Column(db.Boolean, nullable=False)
    app_description = db.Column(db.Text, nullable=False)
    carin_link = db.Column(db.Text)
    medicare_link = db.Column(db.Text)
    caqh_link = db.Column(db.Text)
    # Requesting Information
    fhir_patient_access_api = db.Column(db.Boolean, nullable=False)
    fhir_provider_directory_api = db.Column(db.Boolean, nullable=False)
    fhir_drug_formulary_api = db.Column(db.Boolean, nullable=False)
    # Working Status
    working_status = db.Column(db.String(100), default="New")
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Updatestamps
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))


# Model - Connection Request - Change Log
class ConnectionRequestChangeLog(db.Model):
    """Connection Request Change Log model"""

    __tablename__ = "connection_request_change_logs"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    connectionrequest_id = db.Column(
        db.Integer, db.ForeignKey("connection_requests.id"))
    # Change Log Information
    previous_working_status = db.Column(db.String(100))
    changed_working_status = db.Column(db.String(100))
    # Timestamps
    changed_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    changed_by = db.Column(db.Integer, db.ForeignKey("users.id"))


# Model - Request Jira Ticket
class RequestJira(db.Model):
    """Request Jira relationship model"""

    __tablename__ = "request_jira"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    connectionrequest_id = db.Column(
        db.Integer, db.ForeignKey("connection_requests.id"))
    # Jira Information
    jira_cc_id = db.Column(db.String(255))
    jira_cc_url = db.Column(db.String(255))
    jira_csm1_id = db.Column(db.String(255))
    jira_csm1_url = db.Column(db.String(255))
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Updatestamps
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))
