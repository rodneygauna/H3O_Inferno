"""
Requests > Views
"""

# Imports
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
            app_type=form.app_type.data,
            app_description=form.app_description.data,
            carin_link=form.carin_link.data,
            medicare_link=form.medicare_link.data,
            caqh_link=form.caqh_link.data,
            fhir_api=form.fhir_api.data,
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


# Route - View Requests
@requests_bp.route("/view_requests", methods=["GET", "POST"])
@login_required
def view_requests():
    """View all requests. This is an authenticated route."""

    requests = ConnectionRequest.query.order_by(
        ConnectionRequest.created_date.desc()).all()

    return render_template("requests/view_requests.html",
                           title="View Requests",
                           requests=requests)
