"""
Requests > Forms
"""

# Imports
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    BooleanField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
)


# Form - Connection Request
class ConnectionRequestForm(FlaskForm):
    """Form - Connection Request"""

    # Requester Information
    firstname = StringField('First Name*', validators=[DataRequired()],
                            render_kw={"class": "u-full-width"})
    lastname = StringField('Last Name*', validators=[DataRequired()],
                           render_kw={"class": "u-full-width"})
    email = StringField('Email*', validators=[DataRequired()],
                        render_kw={"class": "u-full-width"})
    phone_number = StringField('Phone Number*', validators=[DataRequired()],
                               render_kw={"class": "u-full-width"})
    company = StringField('Company*', validators=[DataRequired()],
                          render_kw={"class": "u-full-width"})
    company_website = StringField(
        'Company Website*', validators=[DataRequired()],
        render_kw={"class": "u-full-width"})
    # Application Information
    app_name = StringField('Application Name*', validators=[DataRequired()],
                           render_kw={"class": "u-full-width"})
    app_link = StringField('Application Link*', validators=[DataRequired()],
                           render_kw={"class": "u-full-width"})
    app_type_web = BooleanField('Web App', render_kw={"class": "u-full-width"})
    app_type_mobile = BooleanField('Mobile App',
                                   render_kw={"class": "u-full-width"})
    app_type_native = BooleanField('Native App',
                                   render_kw={"class": "u-full-width"})
    app_type_other = BooleanField('Other',
                                  render_kw={"class": "u-full-width"})
    app_description = TextAreaField(
        'Application Description*', validators=[DataRequired()],
        render_kw={"class": "u-full-width"})
    carin_link = StringField('CARIN BB Link',
                             render_kw={"class": "u-full-width"})
    medicare_link = StringField('Medicare Link',
                                render_kw={"class": "u-full-width"})
    caqh_link = StringField('CAQH Link',
                            render_kw={"class": "u-full-width"})
    # Requesting Information
    fhir_patient_access_api = BooleanField(
        'Patient Access API',
        render_kw={"class": "u-full-width"})
    fhir_provider_directory_api = BooleanField(
        'Provider Directory API',
        render_kw={"class": "u-full-width"})
    fhir_drug_formulary_api = BooleanField(
        'Drug Formulary API',
        render_kw={"class": "u-full-width"})
    # Health Plan Information
    health_plan_name = StringField(
        'Health Plan Name*', validators=[DataRequired()],
        render_kw={"class": "u-full-width"})
    # Submit
    submit = SubmitField('Submit')
