"""
Health Apps > Views
"""

# Imports
from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for,
)
from flask_login import (
    login_required,
    current_user,
)
from src import db
from src.models import (
    HealthApp,
)
from src.utils.app_scraping_CARIN import (
    scrape_carin_health_apps_and_store,
)


# Blueprint Configuration
healthapps_bp = Blueprint('healthapps', __name__)


# Route - Health Apps
@healthapps_bp.route('/healthapps')
@login_required
def healthapps():
    """Health Apps page"""
    healthapps = HealthApp.query.all()
    return render_template('healthapps/healthapps.html',
                           title='Health Apps',
                           healthapps=healthapps)


# Function - CARIN Scraper
@healthapps_bp.route('/healthapps/scrape_carin', methods=['POST'])
@login_required
def scrape_carin():
    """Scrape and store health apps from CARIN website"""

    scrape_carin_health_apps_and_store()
    flash('CARIN health apps successfully scraped and stored.', 'success')

    return redirect(url_for('healthapps.healthapps'))
