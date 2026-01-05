from flask import Blueprint, jsonify, request

from app.models import db, User, Task

from app.auth import auth, get_user_from_token


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('/tasks', methods = ['POST'])
def create_task():
    user = get_user_from_token()
    if not user:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    data = request.get_json() or {}

    title = data.get("title")
    if not title:
        return jsonify({"message": "Title is required"}), 400

    description = data.get("description")
    
    new_task = Task(
        title = title,
        description = description,
        user_id = user.id
    )

    db.session.add(new_task)

    db.session.commit()

    return jsonify({
        'id' : new_task.id,
        'title' : new_task.title,
        'description' : new_task.description,
        'status' : new_task.status
    }), 201