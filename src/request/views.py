"""
Requests > Views
"""

# Imports
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    login_required,
    current_user,
)
from src.request.forms import (
    ConnectionRequestForm,
    RequestWorkingStatusForm,
)
from src import db
from src.models import (
    ConnectionRequest,
    RequestJira,
    RequestWorkingStatus,
)


# Blueprint Configuration
requests_bp = Blueprint("requests", __name__)


# Route - Connection Request
@requests_bp.route("/connection_request", methods=["GET", "POST"])
def connection_request():
    """Form for connection request. This is an unauthenticated route."""

    form = ConnectionRequestForm()

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
            health_plan_name=form.health_plan_name.data,
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

    requests = (
        db.session.query(
            ConnectionRequest.id,
            ConnectionRequest.app_name,
            ConnectionRequest.fhir_patient_access_api,
            ConnectionRequest.fhir_provider_directory_api,
            ConnectionRequest.fhir_drug_formulary_api,
            ConnectionRequest.health_plan_name,
            ConnectionRequest.created_date,
            RequestWorkingStatus.working_status,
        )
        .join(
            RequestWorkingStatus,
            RequestWorkingStatus.connectionrequest_id == ConnectionRequest.id,
        )
        .order_by(ConnectionRequest.created_date.desc())
        .all()
    )

    return render_template("requests/view_requests.html",
                           title="View Requests",
                           requests=requests)


# Route - View Request
@requests_bp.route("/view_request/<int:request_id>")
@login_required
def view_request(request_id):
    """View a request. This is an authenticated route."""

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
            RequestWorkingStatus.working_status,
        )
        .filter(ConnectionRequest.id == request_id)
        .join(
            RequestWorkingStatus,
            RequestWorkingStatus.connectionrequest_id == ConnectionRequest.id,
        )
        .first()
    )

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
        form.health_plan_name.data = connection_request.health_plan_name

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
        connection_request.health_plan_name = form.health_plan_name.data
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
    connection_status = RequestWorkingStatus.query.filter_by(
        connectionrequest_id=request_id).first()

    # If this is the first time adding a status update, create a new record
    if connection_status is None:
        connection_status = RequestWorkingStatus(
            connectionrequest_id=request_id,
            working_status=form.working_status.data,
            notes=form.notes.data,
            created_date=datetime.utcnow(),
            created_by=current_user.id,
        )
        db.session.add(connection_status)
        db.session.commit()
        flash("Status has been updated.", "success")
        return redirect(url_for("requests.view_request",
                                request_id=request_id))

    # If there is an existing status update, update the record
    if connection_status is not None:
        # Populate form fields with existing data
        if request.method == "GET":
            form.working_status.data = connection_status.working_status
            form.notes.data = connection_status.notes

        # Update the status of the request
        if form.validate_on_submit():
            connection_status.working_status = form.working_status.data
            connection_status.notes = form.notes.data
            connection_status.updated_date = datetime.utcnow()
            connection_status.updated_by = current_user.id
            db.session.commit()
            flash("Status has been updated.", "success")
            return redirect(url_for("requests.view_request",
                                    request_id=request_id))

    return render_template("requests/status_updates.html",
                           title="Status Updates",
                           form=form,
                           connection_request=connection_request)
