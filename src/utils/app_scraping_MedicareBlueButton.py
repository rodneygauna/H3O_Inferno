"""
Utils > app_scraping_medicareBlueButton
This file contains the functions to scrape the
Medicare Blue Button apps website.

URL: https://www.medicare.gov/manage-your-health/medicares-blue-button-blue-button-20/blue-button-apps
"""

# Imports
import time
from bs4 import BeautifulSoup
from datetime import datetime
from src import db
from src.models import HealthApp
from flask import current_app
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions


def scrape_medicare_blue_button_health_apps_and_store():
    """
    This function scrapes the Medicare Blue Button apps website
    and stores or updates the information for each app in the database.
    """

    url = "https://www.medicare.gov/manage-your-health/medicares-blue-button-blue-button-20/blue-button-apps"

    # Set up Selenium Chrome driver
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

    # Get the page
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)

    # Get the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")

    # Find the desired elements
    ul_element = soup.find("ul", class_="bb-apps__list")

    app_list_medicare_blue_button = []

    if ul_element:
        for li_element in ul_element.find_all("li", class_="bb-apps__item"):
            link = li_element.find("a")["href"]
            name = li_element.find(
                "h4", class_="bb-apps__item-title").text.strip()
            company = li_element.find(
                "h4", class_="bb-apps__item-title").text.strip()
            description = li_element.find(
                "p", class_="bb-apps__item-description"
            ).text.strip()

            # Add the app to the list
            app_list_medicare_blue_button.append(
                {
                    "link": link,
                    "name": name,
                    "company": company,
                    "description": description,
                }
            )

            try:
                with current_app.app_context():
                    for app_info in app_list_medicare_blue_button:
                        existing_app = HealthApp.query.filter_by(
                            name=app_info["name"]
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
                                existing_app.updated_date = datetime.utcnow()
                        else:
                            new_app = HealthApp(
                                source="Medicare Blue Button",
                                name=app_info["name"],
                                company=app_info["company"],
                                description=app_info["description"],
                                link=app_info["link"],
                                created_date=datetime.utcnow(),
                            )
                            db.session.add(new_app)

                    db.session.commit()

                print("Scraped Medicare data saved to the database.")

            except Exception as e:
                print("Error saving Medicare data to the database:", e)
    else:
        return f"No {ul_element} found."

    # Close the driver
    driver.quit()
