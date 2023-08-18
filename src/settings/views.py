"""
Settings > views.py
Routes and functions to manage application settings.
"""

# Imports
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
)
from flask_login import login_required
from src.settings.forms import (
    ChangeRoleForm, ChangeStatusForm
)
from src.decorators.decorators import admin_required
from src import db
from src.models import User


# Blueprint Configuration
settings_bp = Blueprint('settings', __name__)


# Route - Settings Landing Page
@settings_bp.route('/settings', methods=['GET', 'POST'])
@admin_required
@login_required
def settings():
    """Settings landing page"""

    return render_template('settings/settings.html',
                           title='Settings')


# Route - Settings > Manage Users
@settings_bp.route('/settings/manage-users',
                   methods=['GET', 'POST'])
@admin_required
@login_required
def manage_users():
    """Manage users page"""

    users = User.query.all()

    return render_template('settings/manage-users.html',
                           title='Manage Users',
                           users=users)


# Route - Settings > Manage Users > Change Role
@settings_bp.route('/settings/manage-users/change-role/<int:user_id>',
                   methods=['GET', 'POST'])
@admin_required
@login_required
def change_role(user_id):
    """Change user role page"""

    user = User.query.get_or_404(user_id)

    form = ChangeRoleForm()

    if request.method == 'GET':
        form.role.data = user.role

    if form.validate_on_submit():
        user.role = form.role.data
        db.session.commit()

        return redirect(url_for('settings.manage_users'))

    return render_template('settings/change-role.html',
                           title='Change Role',
                           form=form,
                           user=user)


# Route - Settings > Manage Users > Change Status
@settings_bp.route('/settings/manage-users/change-status/<int:user_id>',
                   methods=['GET', 'POST'])
@admin_required
@login_required
def change_status(user_id):
    """Change user status page"""

    user = User.query.get_or_404(user_id)

    form = ChangeStatusForm()

    if request.method == 'GET':
        form.status.data = user.status

    if form.validate_on_submit():
        user.status = form.status.data
        db.session.commit()

        return redirect(url_for('settings.manage_users'))

    return render_template('settings/change-status.html',
                           title='Change Status',
                           form=form,
                           user=user)
