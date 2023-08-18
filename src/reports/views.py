"""
Reports > views.py
Routes and functions to generate and view reports.
"""

# Imports
import io
import csv
from datetime import datetime
from flask import Blueprint, request, render_template, make_response
from flask_login import login_required, current_user
from src.reports.forms import GenerateReportForm
from src.reports.sql_queries import (
    get_report_connect_requests_active,
    get_report_connect_requests_new,
    get_report_connect_requests_approved,
    get_report_connect_requests_denied,
    get_report_connect_requests_all,
    get_report_connect_requests_change_log,
    get_report_health_apps,
    get_report_inferno_users,
)


# Blueprint Configuration
reports_bp = Blueprint("reports", __name__)


# Reports
@reports_bp.route("/reports", methods=["GET", "POST"])
@login_required
def generate_report():
    """Route for generating and viewing reports."""

    form = GenerateReportForm()

    # Report Options
    # Make sure to update the following functions:
    # - get_column_labels()
    # - generate_report_data()
    form.report_options.choices = [
        ("Connection Requests - Active", "Connection Requests - Active"),
        ("Connection Requests - New", "Connection Requests - New"),
        ("Connection Requests - Approved", "Connection Requests - Approved"),
        ("Connection Requests - Denied", "Connection Requests - Denied"),
        ("Connection Requests - All", "Connection Requests - All"),
        ("Connection Requests - Change Log",
         "Conenction Requests - Change Log"),
        ("Health Apps", "Health Apps"),
        ("Inferno Users", "Inferno Users"),
    ]

    if request.method == "POST":
        # Get the selected report and date parameters from the form
        selected_report = form.report_options.data
        start_date = form.start_date.data
        end_date = form.end_date.data

        # Generate report data based on the selected report and date parameters
        report_data = generate_report_data(
            selected_report, start_date, end_date)

        # Define custom column labels based on the selected report
        column_labels = get_column_labels(selected_report)
        # Count of the columns for the selected report
        column_count = len(column_labels)

        # Render the report template with the generated data
        return render_template(
            "reports/report.html",
            title="Soulstone - Report",
            user=current_user,
            report_data=report_data,
            selected_report=selected_report,
            start_date=start_date,
            end_date=end_date,
            column_labels=column_labels,
            column_count=column_count,
        )

    return render_template(
        "reports/generate_report.html",
        title="Soulstone - Generate Report",
        form=form,
        user=current_user,
    )


@reports_bp.route("/reports/export-csv", methods=["POST"])
@login_required
def export_csv():
    """Route for exporting report data as CSV."""

    # Current Time
    current_time = datetime.utcnow()

    # Get the selected report and date parameters from the form
    selected_report = request.form.get("selected_report")
    start_date = request.form.get("start_date")
    end_date = request.form.get("end_date")

    # Generate report data based on the selected report and date parameters
    report_data = generate_report_data(selected_report, start_date, end_date)

    # Define custom column labels based on the selected report
    column_labels = get_column_labels(selected_report)

    # Generate a CSV file in memory
    csv_output = generate_csv(report_data, column_labels)

    # Create a response with the CSV file
    response = make_response(csv_output.getvalue())

    # Set the appropriate headers for CSV download
    response.headers[
        "Content-Disposition"
    ] = f"attachment; filename={selected_report}_{current_time}.csv"
    response.headers["Content-type"] = "text/csv"

    return response


def generate_csv(data, column_labels):
    """Generate a CSV file from the provided data and column labels."""
    output = io.StringIO()
    writer = csv.writer(output)

    # Write the header row
    writer.writerow(column_labels)

    # Write the data rows
    for row in data:
        writer.writerow(row)

    return output


def get_column_labels(report):
    """Get custom column labels based on the selected report."""

    # Connection Requests - Column Labels
    if report == "Connection Requests - Active" \
            or report == "Connection Requests - New" \
            or report == "Connection Requests - Approved" \
            or report == "Connection Requests - Denied" \
            or report == "Connection Requests - All":
        return [
            "ID",
            "Health Plan Name",
            "First Name",
            "Last Name",
            "Email",
            "Phone Number",
            "Company",
            "Company Website",
            "App Name",
            "App Link",
            "App Type Web",
            "App Type Mobile",
            "App Type Native",
            "App Type Other",
            "App Description",
            "CARIN Link",
            "Medicare Link",
            "CAQH Link",
            "FHIR Patient Access API",
            "FHIR Provider Directory API",
            "FHIR Drug Formulary API",
            "Working Status",
            "Created Date",
            "Created By",
            "Updated Date",
            "Updated By",
        ]
    # Connection Requests - Change Log - Column Labels
    elif report == "Connection Requests - Change Log":
        return [
            "Connection Request ID",
            "Health Plan Name",
            "App Name",
            "Chagned From Working Status",
            "Changed To Working Status",
            "Changed Date",
            "Changed By",
        ]
    # Health Apps - Column Labels
    elif report == "Health Apps":
        return [
            "ID",
            "Source",
            "Name",
            "Company",
            "Description",
            "Link",
            "Created Date",
            "Created By",
            "Updated Date",
            "Updated By",
        ]
    # Inferno Users - Column Labels
    elif report == "Inferno Users":
        return [
            "ID",
            "Email",
            "Status",
            "Created Date",
        ]
    else:
        # Handle other report options if needed
        return []


def generate_report_data(report, start_date, end_date):
    """
    Generate report data based on the selected report
    and date parameters.
    """

    # Connection Requests - Active
    if report == "Connection Requests - Active":
        return get_report_connect_requests_active(start_date, end_date)
    # Connection Requests - New
    elif report == "Connection Requests - New":
        return get_report_connect_requests_new(start_date, end_date)
    # Connection Requests - Approved
    elif report == "Connection Requests - Approved":
        return get_report_connect_requests_approved(start_date, end_date)
    # Connection Requests - Denied
    elif report == "Connection Requests - Denied":
        return get_report_connect_requests_denied(start_date, end_date)
    # Connection Requests - All
    elif report == "Connection Requests - All":
        return get_report_connect_requests_all(start_date, end_date)
    # Connection Requests - Change Log
    elif report == "Connection Requests - Change Log":
        return get_report_connect_requests_change_log(start_date, end_date)
    # Health Apps
    elif report == "Health Apps":
        return get_report_health_apps(start_date, end_date)
    # Inferno Users
    elif report == "Inferno Users":
        return get_report_inferno_users(start_date, end_date)
    else:
        # Handle other report options if needed
        return []
