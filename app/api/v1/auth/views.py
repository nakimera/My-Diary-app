import psycopg2
from flask import Blueprint, jsonify, request
from werkzeug.security import check_password_hash, generate_password_hash

import jwt
from app.api.v1.auth.models import User
from validate_email import validate_email

mod = Blueprint('auth', __name__)


@mod.route('/signup', methods=['POST'])

def signup():
    """ 
    Method that registers a user
    """

    data = request.get_json(force=True)
    username = str(data.get("username")).strip()
    email_address = str(data.get("email_address")).strip()
    password = str(data.get("password")).strip()

    validate_email(email_address)

    if not username:
        return jsonify({"message": "Please provide a username"}), 400
    
    if not email_address:
        return jsonify({"message": "Please provide an email address"}), 400

    if not validate_email(email_address):
        return jsonify({"message": "Please provide a valid email address"}), 400

    if not password:
        return jsonify({"message": "Please provide a password"}), 400

    
    password_hash = generate_password_hash(data.get("password"), method='sha256')
    user = User(username, email_address, password_hash)
    user_exists = user.fetch_user(email_address)

    if user_exists:
        return jsonify({"message": "User already exists. Please log in"}), 409

    user.create_user()
    return jsonify({"message": "User successfully signed up"}), 201

@mod.route('/login', methods=['POST'])
def login():
    """ 
    Method that logs in a user
    """
    data = request.get_json(force=True)
    username = str(data.get("username")).strip()
    email_address = str(data.get("email_address")).strip()
    password = str(data.get("password")).strip()

    if not username:
        return jsonify({"message": "Please provide a username"}), 400
        
    if not password:
        return jsonify({"message": "Please provide a password"}), 400
    
    if not email_address:
        return jsonify({"message": "Please provide an email address"}), 400

    user = User(username, email_address, password)
    current_user = user.fetch_user(email_address)

    compare_password = check_password_hash(current_user[3], password)

    if compare_password == True and user.username == current_user[1]:
        logged_in_user = current_user
        user_id = logged_in_user[0]
        token = user.encode_auth_token(user_id)
        return jsonify({
                            "message": "You have successfully logged in",
                            "token": token.decode('UTF-8')
                        }), 200
    
    return jsonify({"message" : "User does not exist. Please try again"}), 404
