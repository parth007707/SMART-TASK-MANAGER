from flask import Blueprint, request, jsonify
from flask_login import login_required, current_user

from database.db import db
from models.task import Task

task_bp = Blueprint('tasks', __name__)


@task_bp.route('/api/tasks', methods=['POST'])
@login_required
def add_task():

    data = request.get_json()

    task = Task(
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status'],
        user_id=current_user.id
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message": "Task added successfully"})


@task_bp.route('/api/tasks', methods=['GET'])
@login_required
def get_tasks():

    tasks = Task.query.filter_by(
        user_id=current_user.id
    ).all()

    task_list = []

    for task in tasks:
        task_list.append({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "priority": task.priority,
            "status": task.status
        })

    return jsonify(task_list)


@task_bp.route('/api/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):

    task = Task.query.get_or_404(id)

    data = request.get_json()

    task.title = data['title']
    task.description = data['description']
    task.priority = data['priority']
    task.status = data['status']

    db.session.commit()

    return jsonify({"message": "Task updated successfully"})


@task_bp.route('/api/tasks/<int:id>', methods=['DELETE'])
@login_required
def delete_task(id):

    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted successfully"})
