"""
CLI Commands for the app
"""


# Imports
import random
from faker import Faker
from flask import Blueprint
from werkzeug.security import generate_password_hash
from web import db
from web.models import (
    User,
    HealthPlan,
    ConnectionRequest,
    RequestJira,
    ConnectionRequestChangeLog,
)
from web.dictionaries.working_status import WORKING_STATUS
from web.dictionaries.demo_health_apps import DEMO_HEALTH_APP_NAMES

# Faker instance
faker = Faker()


# Blueprint initialization
commands_bp = Blueprint("commands", __name__)


# Flask CLI Commands
@commands_bp.cli.command("db_create")
def db_create():
    """Creates the database using SQLAlchemy"""
    db.create_all()
    print("Database created!")


@commands_bp.cli.command("db_drop")
def db_drop():
    """Drops the database using SQLAlchemy"""
    db.drop_all()
    print("Database dropped!")


@commands_bp.cli.command("db_seed")
def db_seed():
    """Seeds the database"""

    # Variable for the maximum range
    max_range = 10
    # Data to seed the database with
    data = []

    # Create users
    for i in range(1, max_range+1):
        random_email = (
            f"{faker.first_name()}{faker.last_name()}@healthtrio.com"
        )
        data.append(
            User(
                email=random_email,
                password_hash=generate_password_hash("password"),
                role=random.choice(["admin", "user"]),
            )
        )

    # Create health plans
    for i in range(1, max_range+1):
        data.append(
            HealthPlan(
                name=faker.company(),
                hp_id=i,
            )
        )

    # Create connection requests
    for i in range(1, max_range+1):
        data.append(
            ConnectionRequest(
                firstname=faker.first_name(),
                lastname=faker.last_name(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                company=faker.company(),
                company_website=faker.url(),
                app_name=random.choice([item[0]
                                       for item in DEMO_HEALTH_APP_NAMES]),
                app_link=faker.url(),
                app_type_web=random.choice([True, False]),
                app_type_mobile=random.choice([True, False]),
                app_type_native=random.choice([True, False]),
                app_type_other=random.choice([True, False]),
                app_description=faker.text(),
                carin_link=random.choice([faker.url(), None]),
                medicare_link=random.choice([faker.url(), None]),
                caqh_link=random.choice([faker.url(), None]),
                fhir_patient_access_api=random.choice([True, False]),
                fhir_provider_directory_api=random.choice([True, False]),
                fhir_drug_formulary_api=random.choice([True, False]),
                health_plan_id=random.randint(1, max_range),
                created_date=faker.date_between(
                    start_date="-1y", end_date="today"),
                working_status=random.choice(
                    [item[0] for item in WORKING_STATUS]),
            )
        )

    # Create Connection Request Change Logs
    for i in range(1, max_range+1):
        data.append(
            ConnectionRequestChangeLog(
                connectionrequest_id=random.randint(1, max_range),
                previous_working_status=random.choice(
                    [item[0] for item in WORKING_STATUS]),
                changed_working_status=random.choice(
                    [item[0] for item in WORKING_STATUS]),
                changed_date=faker.date_between(
                    start_date="-1m", end_date="today"),
                changed_by=random.randint(1, max_range),
            )
        )

    # Create Jira Tickets
    for i in range(1, max_range+1):
        data.append(
            RequestJira(
                connectionrequest_id=i,
                jira_cc_id=random.randint(1, 999999),
                jira_cc_url=faker.url(),
                jira_csm1_id=random.randint(1, 999999),
                jira_csm1_url=faker.url(),
            )
        )

    # Add the data to the database
    for entry in data:
        db.session.add(entry)
    db.session.commit()
    print("Database seeded!")
