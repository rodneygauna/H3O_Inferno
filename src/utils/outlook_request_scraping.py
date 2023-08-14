"""
Utils > outlook_request_scraping.py
Scapes the Outlook web-based email client for
email connection submission requests.

URL: https://outlook.office.com/mail/inbox
"""

# Imports
import os
from time import time
from datetime import datetime
from dotenv import load_dotenv
from src import db
from src.models import ConnectionRequest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
from flask_login import current_user


# Function to scrape the Outlook web-based email client
def scrape_outlook_email_connection_requests_and_store():
    """
    Scrapes the Outlook web-based email client for
    email connection submission requests and stores them to the
    ConnectionRequest table in the database.
    """

    # Load environment variables
    load_dotenv()
    OUTLOOK_EMAIL = os.getenv("H3O_OUTLOOK_EMAIL")
    OUTLOOK_PASSWORD = os.getenv("H3O_OUTLOOK_PASSWORD")

    url = "https://outlook.office.com/mail/inbox"

    # Set up Selenium Chrome driver
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chrome_options, service=chrome_service)

    # Get the page
    driver.get(url)
    time.sleep(5)

    # Try logging into Outlook, else print error message
    try:
        driver.find_element_by_id("i0116").send_keys(OUTLOOK_EMAIL)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(5)
        driver.find_element_by_id("i0118").send_keys(OUTLOOK_PASSWORD)
        driver.find_element_by_id("idSIButton9").click()
        time.sleep(5)
        # Click "Yes" to stay signed in
        driver.find_element_by_id("idSIButton9").click()
    except Exception as e:
        print(e)

    # Wait for the page to load
    time.sleep(20)

    # Get the page source
    page_source = driver.page_source

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, "html.parser")
    print(soup)

    """ # Find table elements
    try:
        table_rows = soup.find_all("tr")
        return table_rows
    except Exception as e:
        print(e) """
