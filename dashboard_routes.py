from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.task import Task
from analytics.analytics import generate_task_analytics

dashboard_bp = Blueprint('dashboard', __name__)


@dashboard_bp.route('/dashboard')
@login_required
def dashboard():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    analytics = generate_task_analytics(tasks)

    return render_template(
        'dashboard.html',
        tasks=tasks,
        analytics=analytics
    )
