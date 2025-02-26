from flask import Blueprint, jsonify, request
from flask_httpauth import HTTPTokenAuth
from app.models import User
from app import db

# Created a Blueprint for authentication routes. 
bp = Blueprint('auth', __name__)

token_auth = HTTPTokenAuth(scheme='Bearer')

@token_auth.verify_token
def verify_token(token):
    return User.query.filter_by(token=token).first()

@token_auth.error_handler
def token_auth_error():
    return jsonify({'error': 'Unauthorized access'}), 401

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = user.get_token()
        db.session.commit()
        return jsonify({'token': token})
    return jsonify({'error': 'Invalid credentials'}), 401