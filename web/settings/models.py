"""
Settings database models for the application.
"""
# Imports
from datetime import datetime
from app import db


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
