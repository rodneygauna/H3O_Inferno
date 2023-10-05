"""
Utils > app_scraping_CARIN
This file contains the functions to scrape the CARIN My Health Application
website.

Current link and site:
  - 10/5/2023: https://myhealthapplication.com/select-an-app-test/

Historical links
  - https://myhealthapplication.com/health-apps/gallery
"""

# Imports
import time
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from flask import current_app
from flask_login import current_user
from src import db
from src.models import HealthApp


def scrape_carin_health_apps_and_store():
    """
    This function scrapes the CARIN My Health Application website
    and stores or updates the information for each app in the database.
    """

    url = "https://myhealthapplication.com/select-an-app-test/"
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
    time.sleep(5)
    soup = BeautifulSoup(response.content, "html.parser")

    app_list_carin = []

    for app in soup.find_all("div", class_="gb-block-layout-column-inner"):
        # Find the "h2" element with the specified class
        h2_element = app.find("h2", class_="wp-block-heading")
        # Find the "p" element with the specified class
        company_element = app.find(
            "p", class_="has-text-color has-medium-font-size")
        description_element = app.find(
            "p",
            style="margin-right:var(--wp--preset--spacing--40);margin-left:0")

        # Initialize variables
        link, name, company, description = None, None, None, None

        # Check if the "h2" element is found
        if h2_element:
            # Find the h2_elements with an "a" element
            link = h2_element.find("a")["href"]
            # Find the "a" element within the "h2" element
            a_element = h2_element.find("a")
            # Check if the "a" element is found
            if a_element:
                # Get the app name from the "a" element
                name = a_element.text.strip()

        # Check if the company_elemnt (p element) is found
        if company_element:
            # Get the text content of the "p" element
            company = company_element.text.strip()

        # Check if the description_element (p element) is found
        if description_element:
            # Get the text content of the "p" element
            description = description_element.text.strip()

        if all((link, name, company, description)):
            app_list_carin.append(
                {
                    "link": link,
                    "name": name,
                    "company": company,
                    "description": description,
                }
            )

    with current_app.app_context():
        for app_info in app_list_carin:
            existing_app = HealthApp.query.filter_by(
                name=app_info["name"], source="CARIN"
            ).first()
            if existing_app:
                if (
                    existing_app.name != app_info["name"]
                    or existing_app.company != app_info["company"]
                    or existing_app.link != app_info["link"]
                    or existing_app.description != app_info["description"]
                ):
                    existing_app.name = app_info["name"]
                    existing_app.company = app_info["company"]
                    existing_app.description = app_info["description"]
                    existing_app.link = app_info["link"]
                    existing_app.updated_date = datetime.utcnow()
                    existing_app.updated_by = current_user.id
            else:
                new_app = HealthApp(
                    source="CARIN",
                    name=app_info["name"],
                    company=app_info["company"],
                    description=app_info["description"],
                    link=app_info["link"],
                    created_date=datetime.utcnow(),
                    created_by=current_user.id,
                )
                db.session.add(new_app)

        db.session.commit()

    print("Scraped CARIN data saved to the database.")
