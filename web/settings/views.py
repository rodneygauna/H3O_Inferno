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
    flash,
)
from flask_login import login_required
from web.settings.forms import (
    ChangeRoleForm, ChangeStatusForm, HealthPlanForm,
)
from web.decorators.decorators import admin_required
from sqlalchemy import or_
from web import db
from web.models import User, HealthPlan


# Blueprint Configuration
settings_bp = Blueprint('settings', __name__)


# Route - Settings Landing Page
@settings_bp.route('/settings', methods=['GET', 'POST'])
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


# Settings - Manage Health Plans
@settings_bp.route('/settings/manage-health-plans',
                   methods=['GET', 'POST'])
@login_required
def manage_health_plans():
    """Manage health plans page"""

    health_plans = HealthPlan.query.all()

    return render_template('settings/manage-health-plans.html',
                           title='Manage Health Plans',
                           health_plans=health_plans)


# Settings - Manage Health Plans > Add Health Plan
@settings_bp.route('/settings/manage-health-plans/add-health-plan',
                   methods=['GET', 'POST'])
@login_required
def add_health_plan():
    """Add health plan page"""

    form = HealthPlanForm()

    if form.validate_on_submit():
        # Check if health plan already exists via name or health plan ID
        health_plan = HealthPlan.query.filter(
            or_(HealthPlan.name == form.name.data,
                HealthPlan.hp_id == form.hp_id.data)).first()
        if health_plan:
            flash('Health plan already exists.', 'danger')

        # Add to the database
        health_plan = HealthPlan(
            name=form.name.data,
            hp_id=form.hp_id.data,
            status=form.status.data,)
        db.session.add(health_plan)
        db.session.commit()

        flash('Health Plan added successfully.', 'success')
        return redirect(url_for('settings.manage_health_plans'))

    return render_template('settings/add-edit-health-plan.html',
                           title='Add Health Plan',
                           form=form)


# Settings - Manage Health Plans > Edit Health Plan
@settings_bp.route(
    '/settings/manage-health-plans/edit-health-plan/<int:health_plan_id>',
    methods=['GET', 'POST'])
@login_required
def edit_health_plan(health_plan_id):
    """Edit health plan page"""

    health_plan = HealthPlan.query.get_or_404(health_plan_id)

    form = HealthPlanForm()

    if request.method == 'GET':
        form.name.data = health_plan.name
        form.hp_id.data = health_plan.hp_id
        form.status.data = health_plan.status

    if form.validate_on_submit():
        # Update the database
        health_plan.name = form.name.data
        health_plan.hp_id = form.hp_id.data
        health_plan.status = form.status.data
        db.session.commit()

        flash('Health Plan updated successfully.', 'success')
        return redirect(url_for('settings.manage_health_plans'))

    return render_template('settings/add-edit-health-plan.html',
                           title='Edit Health Plan',
                           form=form,
                           health_plan=health_plan)
