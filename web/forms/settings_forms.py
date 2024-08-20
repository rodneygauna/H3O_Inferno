"""
Settings > forms.py
This file contains the forms for the Settings Blueprint.
"""

# Imports
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField
from wtforms.validators import DataRequired


# Form - Change User's Role
class ChangeRoleForm(FlaskForm):
    """Change user's role form"""

    role = SelectField('Role', choices=[('admin', 'Admin'),
                                        ('user', 'User')])
    submit = SubmitField('Submit')


# Form - Change User's Status
class ChangeStatusForm(FlaskForm):
    """Change user's status form"""

    status = SelectField('Status', choices=[('ACTIVE', 'Active'),
                                            ('INACTIVE', 'Inactive')])
    submit = SubmitField('Submit')


# Form - Health Plans
class HealthPlanForm(FlaskForm):
    """Health Plans form"""

    name = StringField('Name', validators=[DataRequired()])
    hp_id = StringField('Health Plan ID', validators=[DataRequired()])
    status = SelectField('Status', choices=[('ACTIVE', 'Active'),
                                            ('INACTIVE', 'Inactive')])
    submit = SubmitField('Submit')
