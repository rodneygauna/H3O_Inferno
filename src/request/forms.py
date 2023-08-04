"""
Requests > Forms
"""

# Imports
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
)


# Form - Connection Request
class ConnectionRequestForm(FlaskForm):
    """Form - Connection Request"""

    # Requester Information
    firstname = StringField('First Name*', validators=[DataRequired()])
    lastname = StringField('Last Name*', validators=[DataRequired()])
    email = StringField('Email*', validators=[DataRequired()])
    phone_number = StringField('Phone Number*', validators=[DataRequired()])
    company = StringField('Company*', validators=[DataRequired()])
    company_website = StringField(
        'Company Website*', validators=[DataRequired()])
    # Application Information
    app_name = StringField('Application Name*', validators=[DataRequired()])
    app_link = StringField('Application Link*', validators=[DataRequired()])
    app_type = StringField('Application Type*', validators=[DataRequired()])
    app_description = StringField(
        'Application Description*', validators=[DataRequired()])
    carin_link = StringField('CARIN BB Link')
    medicare_link = StringField('Medicare Link')
    caqh_link = StringField('CAQH Link')
    # Requesting Information
    fhir_api = StringField('FHIR API*', validators=[DataRequired()])
    # Health Plan Information
    health_plan_name = StringField(
        'Health Plan Name*', validators=[DataRequired()])
    # Submit
    submit = SubmitField('Submit for Review')
