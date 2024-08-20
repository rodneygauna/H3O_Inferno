"""Requests > Views"""
# Imports
import pdfkit
from datetime import datetime
from flask import (
    Blueprint, render_template, request, flash, redirect, url_for, jsonify,
    make_response,
)
from flask_login import login_required, current_user
from .forms import (
    ConnectionRequestForm, RequestWorkingStatusForm, JiraTicketsForm,
)
from app import db
from settings.settings_models import HealthPlan
from models.request_models import (
    ConnectionRequest, RequestJira, ConnectionRequestChangeLog
)
from request.sql_queries import (
    get_all_connection_requests, get_all_connection_requests_count,
    get_connection_request,
)
from utils.app_match import calculate_affiliate_match_probability


# Blueprint Configuration
requests_bp = Blueprint("requests", __name__)


# Route - Connection Request
@requests_bp.route("/connection_request", methods=["GET", "POST"])
def connection_request():
    """Form for connection request. This is an unauthenticated route."""

    form = ConnectionRequestForm()

    # Populate the Health Plan ID dropdown
    form.health_plan_id.choices = [
        (health_plan.id, f"{health_plan.name} ({health_plan.hp_id})")
        for health_plan in db.session.query(
            HealthPlan.id, HealthPlan.name, HealthPlan.hp_id,
        ).filter(
            HealthPlan.status == "ACTIVE"
        ).order_by(
            HealthPlan.name.asc()
        ).all()]

    if form.validate_on_submit():
        new_request = ConnectionRequest(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            email=form.email.data,
            phone_number=form.phone_number.data,
            company=form.company.data,
            company_website=form.company_website.data,
            app_name=form.app_name.data,
            app_link=form.app_link.data,
            app_type_web=form.app_type_web.data,
            app_type_mobile=form.app_type_mobile.data,
            app_type_native=form.app_type_native.data,
            app_type_other=form.app_type_other.data,
            app_description=form.app_description.data,
            carin_link=form.carin_link.data,
            medicare_link=form.medicare_link.data,
            caqh_link=form.caqh_link.data,
            fhir_patient_access_api=form.fhir_patient_access_api.data,
            fhir_provider_directory_api=form.fhir_provider_directory_api.data,
            fhir_drug_formulary_api=form.fhir_drug_formulary_api.data,
            health_plan_id=form.health_plan_id.data,
        )
        db.session.add(new_request)
        db.session.commit()
        flash("Your request has been submitted. We will be in touch soon.",
              "success")
        return redirect(url_for("core.index"))

    return render_template("requests/connection_request.html",
                           title="Connection Request",
                           form=form)


# Route - View All Requests
@requests_bp.route("/view_requests", methods=["GET", "POST"])
@login_required
def view_requests():
    """View all requests. This is an authenticated route."""

    requests = get_all_connection_requests()
    count = get_all_connection_requests_count()

    return render_template("requests/view_requests.html",
                           title="View Requests",
                           requests=requests,
                           count=count)


# Route - View Request
@requests_bp.route("/view_request/<int:request_id>")
@login_required
def view_request(request_id):
    """View a request. This is an authenticated route."""

    connection_request = get_connection_request(request_id)

    return render_template("requests/view_request.html",
                           title="View Request",
                           connection_request=connection_request)


# Route - Edit Request
@requests_bp.route("/edit_request/<int:request_id>", methods=["GET", "POST"])
@login_required
def edit_request(request_id):
    """Edit a request. This is an authenticated route."""

    form = ConnectionRequestForm()

    connection_request = ConnectionRequest.query.get_or_404(request_id)

    # Populate the Health Plan ID dropdown
    form.health_plan_id.choices = [
        (health_plan.id, f"{health_plan.name} ({health_plan.hp_id})")
        for health_plan in db.session.query(
            HealthPlan.id, HealthPlan.name, HealthPlan.hp_id,
        ).filter(
            HealthPlan.status == "ACTIVE"
        ).order_by(
            HealthPlan.name.asc()
        ).all()]

    # Populate form fields with existing data
    if request.method == "GET":
        form.firstname.data = connection_request.firstname
        form.lastname.data = connection_request.lastname
        form.email.data = connection_request.email
        form.phone_number.data = connection_request.phone_number
        form.company.data = connection_request.company
        form.company_website.data = connection_request.company_website
        form.app_name.data = connection_request.app_name
        form.app_link.data = connection_request.app_link
        form.app_type_web.data = connection_request.app_type_web
        form.app_type_mobile.data = connection_request.app_type_mobile
        form.app_type_native.data = connection_request.app_type_native
        form.app_type_other.data = connection_request.app_type_other
        form.app_description.data = connection_request.app_description
        form.carin_link.data = connection_request.carin_link
        form.medicare_link.data = connection_request.medicare_link
        form.caqh_link.data = connection_request.caqh_link
        form.fhir_patient_access_api.data = \
            connection_request.fhir_patient_access_api
        form.fhir_provider_directory_api.data = \
            connection_request.fhir_provider_directory_api
        form.fhir_drug_formulary_api.data = \
            connection_request.fhir_drug_formulary_api
        form.health_plan_id.data = connection_request.health_plan_id

    if form.validate_on_submit():
        connection_request.firstname = form.firstname.data
        connection_request.lastname = form.lastname.data
        connection_request.email = form.email.data
        connection_request.phone_number = form.phone_number.data
        connection_request.company = form.company.data
        connection_request.company_website = form.company_website.data
        connection_request.app_name = form.app_name.data
        connection_request.app_link = form.app_link.data
        connection_request.app_type_web = form.app_type_web.data
        connection_request.app_type_mobile = form.app_type_mobile.data
        connection_request.app_type_native = form.app_type_native.data
        connection_request.app_type_other = form.app_type_other.data
        connection_request.app_description = form.app_description.data
        connection_request.carin_link = form.carin_link.data
        connection_request.medicare_link = form.medicare_link.data
        connection_request.caqh_link = form.caqh_link.data
        connection_request.fhir_patient_access_api = \
            form.fhir_patient_access_api.data
        connection_request.fhir_provider_directory_api = \
            form.fhir_provider_directory_api.data
        connection_request.fhir_drug_formulary_api = \
            form.fhir_drug_formulary_api.data
        connection_request.health_plan_id = form.health_plan_id.data
        connection_request.updated_date = datetime.utcnow()
        connection_request.updated_by = current_user.id
        db.session.commit()
        flash("Connection request has been updated.", "success")
        return redirect(url_for("requests.view_request",
                                request_id=request_id))

    return render_template("requests/connection_request.html",
                           title="Edit Request",
                           form=form,
                           connection_request=connection_request)


# Route - Status Updates
@requests_bp.route("/status_updates/<int:request_id>", methods=["GET", "POST"])
@login_required
def status_updates(request_id):
    """Allows the HealthTrio user to update the status of a request."""

    form = RequestWorkingStatusForm()

    connection_request = ConnectionRequest.query.get_or_404(request_id)

    # Populate form fields with existing data
    if request.method == "GET":
        form.working_status.data = connection_request.working_status

    # Update the status of the request
    if form.validate_on_submit():
        # Create a new change log record
        new_change_log = ConnectionRequestChangeLog(
            connectionrequest_id=request_id,
            previous_working_status=connection_request.working_status,
            changed_working_status=form.working_status.data,
            changed_date=datetime.utcnow(),
            changed_by=current_user.id,
        )
        db.session.add(new_change_log)
        db.session.commit()

        # Update the status of the request
        connection_request.working_status = form.working_status.data
        connection_request.updated_date = datetime.utcnow()
        connection_request.updated_by = current_user.id
        db.session.commit()

        flash("Status has been updated.", "success")
        return redirect(url_for("requests.view_request",
                                request_id=request_id))

    return render_template("requests/status_updates.html",
                           title="Status Updates",
                           form=form,
                           connection_request=connection_request)


# Route - Jira Ticket Updates
@requests_bp.route("/jira_ticket_updates/<int:request_id>",
                   methods=["GET", "POST"])
@login_required
def jira_ticket_updates(request_id):
    """Allows the HealthTrio user to update the Jira ticket of a request."""

    form = JiraTicketsForm()

    connection_request = ConnectionRequest.query.get_or_404(request_id)
    jira_tickets = RequestJira.query.filter_by(
        connectionrequest_id=request_id).first()

    # If this is the first time adding a Jira ticket, create a new record
    if jira_tickets is None:
        if form.validate_on_submit():
            jira_tickets = RequestJira(
                connectionrequest_id=request_id,
                jira_cc_id=form.jira_cc_id.data,
                jira_cc_url=form.jira_cc_url.data,
                jira_csm1_id=form.jira_csm1_id.data,
                jira_csm1_url=form.jira_csm1_url.data,
                created_date=datetime.utcnow(),
                created_by=current_user.id,
            )
            db.session.add(jira_tickets)
            db.session.commit()
            flash("Jira tickets has been updated.", "success")
            return redirect(url_for("requests.view_request",
                                    request_id=request_id))

    # If there is an existing Jira ticket, update the record
    if jira_tickets is not None:
        # Populate form fields with existing data
        if request.method == "GET":
            form.jira_cc_id.data = jira_tickets.jira_cc_id
            form.jira_cc_url.data = jira_tickets.jira_cc_url
            form.jira_csm1_id.data = jira_tickets.jira_csm1_id
            form.jira_csm1_url.data = jira_tickets.jira_csm1_url

        # Update the Jira ticket of the request
        if form.validate_on_submit():
            jira_tickets.jira_cc_id = form.jira_cc_id.data
            jira_tickets.jira_cc_url = form.jira_cc_url.data
            jira_tickets.jira_csm1_id = form.jira_csm1_id.data
            jira_tickets.jira_csm1_url = form.jira_csm1_url.data
            jira_tickets.updated_date = datetime.utcnow()
            jira_tickets.updated_by = current_user.id
            db.session.commit()
            flash("Jira tickets has been updated.", "success")
            return redirect(url_for("requests.view_request",
                                    request_id=request_id))

    return render_template("requests/jira_ticket_updates.html",
                           title="Jira Ticket Updates",
                           form=form,
                           connection_request=connection_request)


# Function - HealthApp Probability Matching
@requests_bp.route("/healthapp_match/<int:request_id>")
@login_required
def healthapp_match(request_id):
    """
    This function matches the Connection Request with the HealthApp
    based on the probability of the match using the
    calculate_affiliate_match_probability function.
    """

    connection_request = ConnectionRequest.query.get_or_404(request_id)

    # Calculate the match probability
    match_info = calculate_affiliate_match_probability(connection_request)

    return jsonify(match_info)


# Function - Request PDF Form Generator
@requests_bp.route("/request_pdf/<int:request_id>")
@login_required
def request_pdf(request_id):
    """Generates a PDF of the Connection Request
    to submit to the Health Plan."""

    # Variables
    connection_request = ConnectionRequest.query.get_or_404(request_id)
    current_year = datetime.utcnow().year
    request_date = connection_request.created_date.strftime("%Y-%m-%d")
    current_date = datetime.utcnow().strftime("%Y-%m-%d")
    app_name = connection_request.app_name
    filename = f"{app_name}_{request_date}_{current_date}.pdf"

    # Match the Connection Request with the HealthApp
    match_info = calculate_affiliate_match_probability(connection_request)
    carin_true = False
    medicare_bb_true = False
    if match_info["carin_app_match"] is True:
        carin_true = True
    if match_info["medicare_app_match"] is True:
        medicare_bb_true = True

    rendered = render_template("requests/request_pdf.html",
                               r=connection_request,
                               current_year=current_year,
                               carin_true=carin_true,
                               medicare_bb_true=medicare_bb_true)
    config = pdfkit.configuration(wkhtmltopdf="/usr/bin/wkhtmltopdf")
    pdf = pdfkit.from_string(rendered, False, configuration=config)
    response = make_response(pdf)
    response.headers["Content-Type"] = "application/pdf"
    response.headers["Content-Disposition"] = f"inline; filename={filename}"
    return response
