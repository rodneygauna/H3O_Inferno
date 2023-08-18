"""
Reports > sql_queries.py
SQL queries for generating reports.
"""

# Imports
from sqlalchemy import or_
from src import db
from src.models import (
    User, HealthApp, ConnectionRequest,
    ConnectionRequestChangeLog,
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
        ConnectionRequest.created_date >= start_date,
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query


# Connection Request - Active
def get_report_connect_requests_active(start_date, end_date):
    """
    Returns connection requests report data that have a working status of:
        - New
        - In Review by PM
        - In Review by Health Plan
        - Request Approved by Health Plan
        - Connection Request Created
        - Connection In Progress with Development Team
    """

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
        or_(
            ConnectionRequest.working_status == "New",
            ConnectionRequest.working_status == "In Review by PM",
            ConnectionRequest.working_status == "In Review by Health Plan",
            ConnectionRequest.working_status == "Request Approved by Health Plan",
            ConnectionRequest.working_status == "Connection Request Created",
            ConnectionRequest.working_status == "Connection In Progress with Development Team",
        )
    ).filter(
        ConnectionRequest.created_date >= start_date,
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query


# Connection Request - New
def get_report_connect_requests_new(start_date, end_date):
    """
    Returns connection requests report data that have a working status of "New"
    """

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
        ConnectionRequest.working_status == "New",
        ConnectionRequest.created_date >= start_date,
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query


# Connection Request - Approved
def get_report_connect_requests_approved(start_date, end_date):
    """
    Returns connection requests report data that have a working status of:
        - Request Approved by Health Plan
        - Connection Request Created
        - Connection In Progress with Development Team
        - Connection Completed
    """

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
        or_(
            ConnectionRequest.working_status == "Request Approved by Health Plan",
            ConnectionRequest.working_status == "Connection Request Created",
            ConnectionRequest.working_status == "Connection In Progress with Development Team",
            ConnectionRequest.working_status == "Connection Completed",
        ),
        ConnectionRequest.created_date >= start_date,
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query


# Connection Request - Denied
def get_report_connect_requests_denied(start_date, end_date):
    """
    Returns connection requests report data that have a working status of
    "Request Denied by Health Plan"
    """

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
        ConnectionRequest.working_status == "Request Denied by Health Plan",
        ConnectionRequest.created_date >= start_date,
        ConnectionRequest.created_date <= end_date
    ).all()

    # Return
    return query


# Connection Requests - Change Log
def get_report_connect_requests_change_log(start_date, end_date):
    """Returns the connection requests change log report data"""

    # Query
    query = db.session.query(
        ConnectionRequestChangeLog.connectionrequest_id,
        ConnectionRequest.health_plan_name,
        ConnectionRequest.app_name,
        ConnectionRequestChangeLog.previous_working_status,
        ConnectionRequestChangeLog.changed_working_status,
        ConnectionRequestChangeLog.changed_date,
        User.email,
    ).join(
        User, ConnectionRequestChangeLog.changed_by == User.id
    ).join(
        ConnectionRequest,
        ConnectionRequestChangeLog.connectionrequest_id
        == ConnectionRequest.id
    ).filter(
        ConnectionRequestChangeLog.changed_date >= start_date,
        ConnectionRequestChangeLog.changed_date <= end_date
    ).order_by(
        ConnectionRequestChangeLog.changed_date.desc()
    ).all()

    # Return
    return query


# Health Apps
def get_report_health_apps(start_date, end_date):
    """Returns all health apps report data"""

    # Aliases
    CreatingUser = db.aliased(User, name="CreatingUser")
    UpdatingUser = db.aliased(User, name="UpdatingUser")
    # Query
    query = db.session.query(
        HealthApp.id,
        HealthApp.source,
        HealthApp.name,
        HealthApp.company,
        HealthApp.description,
        HealthApp.link,
        HealthApp.created_date,
        CreatingUser.email.label("created_by"),
        HealthApp.updated_date,
        UpdatingUser.email.label("updated_by"),
    ).outerjoin(
        CreatingUser, HealthApp.created_by == CreatingUser.id
    ).outerjoin(
        UpdatingUser, HealthApp.updated_by == UpdatingUser.id
    ).filter(
        HealthApp.created_date >= start_date,
        HealthApp.created_date <= end_date
    ).all()

    # Return
    return query


# Inferno Users
def get_report_inferno_users(start_date, end_date):
    """Returns all inferno users report data"""

    # Query
    query = db.session.query(
        User.id,
        User.email,
        User.status,
        User.created_date,
    ).filter(
        User.created_date >= start_date,
        User.created_date <= end_date
    ).all()

    # Return
    return query
