from flask import jsonify, request
from flask_cors import CORS, cross_origin
from . import create_app, db
from .models import User

app = create_app()
# CORS(app, resources={r"/users/*": {"origins": ["http://localhost:5173"]}})

CORS(app, origins=[
    "http://localhost:5173",
    "http://localhost:5000",
    "http://localhost",
])

@app.route('/')
def home():
    return 'Hello from Flask!'

# RESET MODELS
@app.route('/resetdb')
def reset_db():
    with app.app_context():
        try:
            db.drop_all()
            db.create_all()
            return 'Reset success!'
        except Exception as e:
            return f"Error: {e}"

# GET ALL USERS
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
    except Exception as e:
        return f"Error: {e}"
    return jsonify([
        {'id': user.id, 'name': user.name, 'email': user.email}
        for user in users
    ])

# GET USER BY ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
    except Exception as e:
        return f"Error: {e}"
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

# CREATE
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
    except Exception as e:
        return f"Error: {e}"
    return jsonify({'message': 'User added successfully'}), 201

# UPDATE
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
    except Exception as e:
        return f"Error: {e}"
    return jsonify({'message': 'User updated successfully'})

# DELETE
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# app.run()