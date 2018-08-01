from flask import Blueprint, make_response, request
from werkzeug.security import generate_password_hash
import psycopg2
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)

@mod.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = data.get("username", None)
    email_address = data.get("email_address", None)
    password = generate_password_hash(data.get("password"), method='sha256')
    user = User(username, password, email_address)

    if user.username == "":
        return make_response("Please provide a username", 200)
        
    else:
        user.create_user()
        return make_response('User successfully signed up', 201)

@mod.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)
    user = User(username, password)
    user.login_user()
    return make_response('You are successfully logged in', 200)