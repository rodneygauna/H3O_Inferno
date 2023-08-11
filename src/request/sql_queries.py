"""
Requests > sql_queries.py
This file contains the SQL queries for the Requests > views.py file.
"""

# Imports
from src import db
from src.models import (
    ConnectionRequest,
    RequestJira,
)


# Query - All Connection Requests
def get_all_connection_requests():
    """Returns all connection requests"""

    requests = (
        db.session.query(
            ConnectionRequest.id,
            ConnectionRequest.app_name,
            ConnectionRequest.fhir_patient_access_api,
            ConnectionRequest.fhir_provider_directory_api,
            ConnectionRequest.fhir_drug_formulary_api,
            ConnectionRequest.health_plan_name,
            ConnectionRequest.created_date,
            ConnectionRequest.working_status,
            RequestJira.jira_cc_id,
            RequestJira.jira_cc_url,
            RequestJira.jira_csm1_id,
            RequestJira.jira_csm1_url,
        )
        .outerjoin(
            RequestJira,
            RequestJira.connectionrequest_id == ConnectionRequest.id,
        )
        .order_by(ConnectionRequest.created_date.desc())
        .all()
    )

    return requests


# Query - Connection Request
def get_connection_request(request_id):
    """Returns a connection request"""

    connection_request = (
        db.session.query(
            ConnectionRequest.id,
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
            ConnectionRequest.health_plan_name,
            ConnectionRequest.created_date,
            ConnectionRequest.working_status,
            RequestJira.jira_cc_id,
            RequestJira.jira_cc_url,
            RequestJira.jira_csm1_id,
            RequestJira.jira_csm1_url,
        )
        .filter(ConnectionRequest.id == request_id)
        .outerjoin(
            RequestJira,
            RequestJira.connectionrequest_id == ConnectionRequest.id,
        )
        .first()
    )

    return connection_request
