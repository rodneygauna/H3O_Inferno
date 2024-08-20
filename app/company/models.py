"""
Company > models.py
This file contains the database models for the company (third-party developers
and provider practices) in the application.
"""
# Imports
from datetime import datetime
from app import db


# Model - Company
class Company(db.Model):
    """Company model"""

    __tablename__ = "companies"

    # IDs
    id = db.Column(db.Integer, primary_key=True)
    # Company Information
    company = db.Column(db.String(255), nullable=False)
    company_website = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(255), nullable=False)
    # Status
    is_active = db.Column(db.Boolean, default=True)
    # Timestamps
    created_date = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    updated_date = db.Column(db.DateTime)
    # Updatestamps
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"))
    updated_by = db.Column(db.Integer, db.ForeignKey("users.id"))
