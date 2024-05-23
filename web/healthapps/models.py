"""
Database models for the application.
"""
# Imports
from datetime import datetime
from app import db


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
