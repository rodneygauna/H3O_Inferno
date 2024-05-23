"""
Utils > app_match.py
This function is used to determine if the connection request
matches any Health Apps in the database.

It will return a list of Health Apps that match the request based on
the company name and the app name along with a score of how well the
request matches the app.
"""

# Imports
from sqlalchemy import func
from web.models import HealthApp


# Function - Probability Matching
def calculate_affiliate_match_probability(connection_request):
    """
    Calculate the probability that the connection request matches.
    The probability is calculated by comparing the company name and
    the app name to the Health Apps in the database.

    The probability is calculated by dividing the number of matches
    by the total number of possible matches.
    """

    # Get the company and app name from the connection request
    company = connection_request.company.lower()  # Convert to lowercase
    app_name = connection_request.app_name.lower()  # Convert to lowercase

    # Query HealthApp records that match the company and app name
    matching_apps = HealthApp.query.filter(
        (func.lower(HealthApp.company) == company) |
        (func.lower(HealthApp.name) == app_name)
    ).all()

    carin_company_match = any(
        health_app.source == 'CARIN' for health_app in matching_apps)
    medicare_company_match = any(
        health_app.source == 'Medicare Blue Button'
        for health_app in matching_apps)
    carin_app_match = any(health_app.source ==
                          'CARIN' for health_app in matching_apps)
    medicare_app_match = any(
        health_app.source == 'Medicare Blue Button'
        for health_app in matching_apps)

    # Calculate the match probability
    total_matches = (carin_company_match + medicare_company_match +
                     carin_app_match + medicare_app_match)
    total_sources = 4  # Total possible sources to match

    match_probability = (total_matches / total_sources) * 100

    match_info = {
        "carin_company_match": carin_company_match,
        "medicare_company_match": medicare_company_match,
        "carin_app_match": carin_app_match,
        "medicare_app_match": medicare_app_match,
        "match_probability": match_probability
    }

    return match_info
