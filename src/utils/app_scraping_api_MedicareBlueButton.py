"""
Utils > app_scraping_api_medicareBlueButton
This file contains the function to scrape the Medicare Blue Button API.

URL: https://api.bluebutton.cms.gov/.well-known/applications?page_size=1000&page=1
"""

# Imports
import time
from datetime import datetime
import requests
from flask import current_app
from flask_login import current_user
from src import db
from src.models import HealthApp


def scrape_medicare_api_health_apps():
    """
    This function will scrape the Medicare Blue Button API and return a list
    of apps.

    URL: https://api.bluebutton.cms.gov/.well-known/applications?page_size=1000&page=1
    """

    # URL to the API
    url = "https://api.bluebutton.cms.gov/.well-known/applications?page_size=1000&page=1"

    # improve the requests.get() call by adding a user agent and a timeout
    response = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/61.0.3163.100 Safari/537.36"
        },
        timeout=10
    )

    # Wait for the page to load
    time.sleep(5)

    # Get the JSON data
    json_data = response.json()

    # Initialize the list of apps
    app_list_medicare_blue_button = []

    # Loop through the JSON data
    for app in json_data["results"]:
        # Initialize variables
        link, name, company, description = None, None, None, None

        # Check if the "link" key is in the dictionary
        if "website_uri" in app:
            link = app["website_uri"]

        # Check if the "name" key is in the dictionary
        if "name" in app:
            name = app["name"]

        # Check if the "developer" key is in the dictionary
        if "name" in app:
            company = app["name"]

        # Check if the "description" key is in the dictionary
        if "description" in app:
            description = app["description"]

        # Add the app to the list
        app_list_medicare_blue_button.append({
            "link": link,
            "name": name,
            "company": company,
            "description": description
        })

    # Save the apps to the database
    with current_app.app_context():
        for app_info in app_list_medicare_blue_button:
            existing_app = HealthApp.query.filter_by(
                name=app_info["name"], source="Medicare Blue Button"
            ).first()
            if existing_app:
                if (
                    existing_app.name != app_info["name"]
                    or existing_app.company != app_info["company"]
                    or existing_app.description != app_info["description"]
                    or existing_app.link != app_info["link"]
                ):
                    existing_app.name = app_info["name"]
                    existing_app.company = app_info["company"]
                    existing_app.description = app_info["description"]
                    existing_app.link = app_info["link"]
                    existing_app.updated_date = datetime.utcnow()
                    existing_app.updated_by = current_user.id
            else:
                new_app = HealthApp(
                    name=app_info["name"],
                    company=app_info["company"],
                    description=app_info["description"],
                    link=app_info["link"],
                    source="Medicare Blue Button",
                    created_date=datetime.utcnow(),
                    created_by=current_user.id,
                )
                db.session.add(new_app)
        db.session.commit()
    print("Scraped Medicare API and saved to the database.")
