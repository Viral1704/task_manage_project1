from flask import Blueprint, jsonify, request

from app.models import db, User, Task

from app.auth import auth, get_user_from_token


tasks_bp = Blueprint('tasks', __name__)


@tasks_bp.route('', methods = ['POST'])
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


@tasks_bp.route('', methods = ['GET'])
def get_tasks():
    user = get_user_from_token()
    if not user:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    tasks = Task.query.filter_by(user_id = user.id).all()

    tasks_list = []
    for task in tasks:
        tasks_list.append({
            'id' : task.id,
            'title' : task.title,
            'description' : task.description,
            'status' : task.status
        })

    return jsonify(tasks_list), 200
    

@tasks_bp.route('/<int:task_id>', methods = ['PUT'])
def update_task(task_id):
    user = get_user_from_token()
    if not user:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message' : 'Task not found'}), 404

    if task.user_id != user.id:
        return jsonify({'message' : 'Forbidden'}), 403
    
    data = request.get_json() or {}

    title =data.get("title")
    if title:
        task.title = title

    description = data.get("description")
    if description is not None:
        task.description = description

    status = data.get("status")
    if status:
        if status not in ['pending', 'in-progress', 'completed']:
            return jsonify({'message' : 'Invalid status value'}), 400
        task.status = status

    db.session.commit()

    return jsonify({
        'id' : task.id,
        'title' : task.title,
        'description' : task.description,
        'status' : task.status
    }), 200


@tasks_bp.route('/<int:task_id>', methods = ['DELETE'])
def delete_task(task_id):
    user = get_user_from_token()
    if not user:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message' : 'Task not found!'}), 404
    
    if task.user_id != user.id:
        return jsonify({'message' : 'Forbidden!'}), 403
    
    db.session.delete(task)

    db.session.commit()

    return "", 204


@tasks_bp.route('/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    user = get_user_from_token()
    if not user:
        return jsonify({'message' : 'Unauthorized'}), 401
    
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'message' : 'Task not found!'}), 404
    
    if task.user_id != user.id:
        return jsonify({'message' : 'Forbidden!'}), 403
    
    return jsonify({
        'id' : task.id,
        'title' : task.title,
        'description' : task.description,
        'status' : task.status
    }), 200