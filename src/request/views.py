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

    requests = ConnectionRequest.query.order_by(
        ConnectionRequest.created_date.desc()).all()

    return render_template("requests/view_requests.html",
                           title="View Requests",
                           requests=requests)


# Route - View Request
@requests_bp.route("/view_request/<int:request_id>")
@login_required
def view_request(request_id):
    """View a request. This is an authenticated route."""

    connection_request = ConnectionRequest.query.get_or_404(request_id)

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
        return redirect(url_for("requests.view_request", request_id=request_id))

    return render_template("requests/connection_request.html",
                           title="Edit Request",
                           form=form,
                           connection_request=connection_request)
