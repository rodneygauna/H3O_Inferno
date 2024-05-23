"""Health Apps > Views"""
# Imports
from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required
from .models import HealthApp
from utils.app_scraping_CARIN import (
    scrape_carin_health_apps_and_store,
)
from utils.app_scraping_api_MedicareBlueButton import (
    scrape_medicare_api_health_apps,
)


# Blueprint Configuration
healthapps_bp = Blueprint('healthapps', __name__)


# Route - Health Apps
@healthapps_bp.route('/healthapps')
@login_required
def healthapps():
    """Health Apps page"""
    healthapps_list = HealthApp.query.all()
    return render_template('healthapps/healthapps.html',
                           title='Health Apps',
                           healthapps_list=healthapps_list)


# Function - CARIN Scraper
@healthapps_bp.route('/healthapps/scrape_carin', methods=['POST'])
@login_required
def scrape_carin():
    """Scrape and store health apps from CARIN website"""

    try:
        scrape_carin_health_apps_and_store()
        flash('CARIN health apps successfully scraped and stored.',
              'success')
    except Exception as error:
        flash(f'Error scraping CARIN health apps. {error}', 'error')

    return redirect(url_for('healthapps.healthapps'))


# Function - Medicare Blue Button Scraper
@healthapps_bp.route('/healthapps/scrape_medicare', methods=['POST'])
@login_required
def scrape_medicare():
    """Scrape and store health apps from Medicare website"""

    try:
        scrape_medicare_api_health_apps()
        flash(
            'Medicare Blue Button health apps successfully stored.',
            'success'
        )
    except Exception as error:
        flash(
            f'Error scraping Medicare Blue Button health apps. {error}',
            'error'
        )

    return redirect(url_for('healthapps.healthapps'))
