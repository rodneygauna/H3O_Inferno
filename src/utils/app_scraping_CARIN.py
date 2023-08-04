"""
Utils > app_scraping_CARIN
This file contains the functions to scrape the CARIN My Health Application
website.

URL: https://myhealthapplication.com/health-apps/gallery
"""

# Imports
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from src import db
from src.models import HealthApp
from flask import current_app


def scrape_carin_health_apps_and_store():
    """
    This function scrapes the CARIN My Health Application website
    and stores or updates the information for each app in the database.
    """

    url = "https://myhealthapplication.com/health-apps/gallery"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    app_list_CARIN = []

    for app in soup.find_all("div", class_="app-info"):
        link = app.find("a")["href"]
        name = app.find("h2").text.strip()
        company = app.find("h5").text.strip()
        description = app.find("p").text.strip()
        app_list_CARIN.append(
            {
                "link": f"https://myhealthapplication.com{link}",
                "name": name,
                "company": company,
                "description": description,
            }
        )

    try:
        with current_app.app_context():
            for app_info in app_list_CARIN:
                existing_app = HealthApp.query.filter_by(
                    name=app_info["name"]).first()
                if existing_app:
                    if (existing_app.name != app_info["name"] or
                        existing_app.company != app_info["company"] or
                            existing_app.description != app_info["description"] or
                            existing_app.link != app_info["link"]):
                        existing_app.name = app_info["name"]
                        existing_app.company = app_info["company"]
                        existing_app.description = app_info["description"]
                        existing_app.updated_date = datetime.utcnow()
                else:
                    new_app = HealthApp(
                        source="CARIN",
                        name=app_info["name"],
                        company=app_info["company"],
                        description=app_info["description"],
                        link=app_info["link"],
                        created_date=datetime.utcnow(),
                    )
                    db.session.add(new_app)

            db.session.commit()

        print("Scraped CARIN data saved to the database.")

    except Exception as e:
        print(f"Error saving CARIN data to the database: {e}")
