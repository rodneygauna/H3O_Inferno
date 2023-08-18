"""
Reports > sql_queries.py
SQL queries for generating reports.
"""

# Imports
from src import db
from src.models import (
    User, HealthApp, ConnectionRequest
)


# Connection Requests - All
def get_report_connect_requests_all(start_date, end_date):
    """Returns all connection requests report data"""

    # Aliases
    CreatingUser = db.aliased(User, name="CreatingUser")
    UpdatingUser = db.aliased(User, name="UpdatingUser")
    # Query
    query = db.session.query(
        ConnectionRequest.id,
        ConnectionRequest.health_plan_name,
        ConnectionRequest.firstname,
        ConnectionRequest.lastname,
        ConnectionRequest.email,
        ConnectionRequest.phone_number,
        ConnectionRequest.company,
        ConnectionRequest.company_website,
        ConnectionRequest.app_name,
        ConnectionRequest.app_link,
        ConnectionRequest.app_type_web,
        ConnectionRequest.app_type_mobile,
        ConnectionRequest.app_type_native,
        ConnectionRequest.app_type_other,
        ConnectionRequest.app_description,
        ConnectionRequest.carin_link,
        ConnectionRequest.medicare_link,
        ConnectionRequest.caqh_link,
        ConnectionRequest.fhir_patient_access_api,
        ConnectionRequest.fhir_provider_directory_api,
        ConnectionRequest.fhir_drug_formulary_api,
        ConnectionRequest.working_status,
        ConnectionRequest.created_date,
        CreatingUser.email.label("created_by"),
        ConnectionRequest.updated_date,
        UpdatingUser.email.label("updated_by"),
    ).outerjoin(
        CreatingUser, ConnectionRequest.created_by == CreatingUser.id
    ).outerjoin(
        UpdatingUser, ConnectionRequest.updated_by == UpdatingUser.id
    ).filter(
        ConnectionRequest.created_date >= start_date
    ).filter(
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query
