"""
Request database models for the application.
"""
# Imports
from datetime import datetime
from app import db


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
