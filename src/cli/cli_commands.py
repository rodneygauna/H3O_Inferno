"""
CLI Commands for the app
"""


# Imports
import random
from faker import Faker
from flask import Blueprint
from werkzeug.security import generate_password_hash
from src import db
from src.models import (
    User,
    ConnectionRequest,
    RequestJira,
)
from src.dictionaries.working_status import WORKING_STATUS

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
    max_range = 10+1
    # Data to seed the database with
    data = []

    # Create users
    for i in range(1, max_range):
        random_email = (
            f"{faker.first_name()}{faker.last_name()}@healthtrio.com"
        )
        data.append(
            User(
                email=random_email,
                password_hash=generate_password_hash("password"),
            )
        )

    # Create connection requests
    for i in range(1, max_range):
        data.append(
            ConnectionRequest(
                firstname=faker.first_name(),
                lastname=faker.last_name(),
                email=faker.email(),
                phone_number=faker.phone_number(),
                company=faker.company(),
                company_website=faker.url(),
                app_name=faker.company(),
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
                health_plan_name=faker.company(),
                created_date=faker.date_between(
                    start_date="-1y", end_date="today"),
                working_status=random.choice(
                    [item[0] for item in WORKING_STATUS]),
            )
        )

    # Create Jira Tickets
    for i in range(1, max_range):
        data.append(
            RequestJira(
                connectionrequest_id=random.randint(1, max_range),
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
