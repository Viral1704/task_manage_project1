from flask import Blueprint, request, jsonify

from app.models import db, User



auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message' : 'Email and Password are required!'}), 400
    
    user = User.query.filter_by(email = email).first()

    if user is None or not user.check_password(password):
        return jsonify({'message' : 'Invalid credentials!'}), 401
    
    return jsonify({'message' : 'Login successful!', 'user_id' : user.id}), 200


@auth.route('/register', methods = ['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message' : 'Username, Email and Password are required!'}), 400
    
    user_exists = User.query.filter_by(email = email).first()
    if user_exists:
        return jsonify({'message' : 'Email already registered!'}), 400
    
    new_user = User(username = username, email = email)

    new_user.password = password

    db.session.add(new_user)

    db.session.commit()

    return jsonify({'message' : 'User registered successfully!', 'user_id' : new_user.id}), 201
