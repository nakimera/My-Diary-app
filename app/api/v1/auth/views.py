from flask import Blueprint, make_response, request
from werkzeug.security import generate_password_hash
import psycopg2
from app.api.v1.auth.models import User

mod = Blueprint('auth', __name__)

@mod.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = str(data.get("username", "")).strip()
    email_address = str(data.get("email_address", None)).strip()
    password = str(data.get("password", None)).strip()

    if not username:
        return make_response("Please provide a username", 400)
    
    if not email_address:
        return make_response("Please provide a email address", 400)

    if not password:
        return make_response("Please provide a password", 400)

    # if db_user:
    #     return make_response("User already exists. Please log in")

    password_hash = generate_password_hash(data.get("password"), method='sha256')
    user = User(username, password_hash, email_address)
    user.create_user()
    return make_response('User successfully signed up', 201)

@mod.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username = data.get("username", None)
    password = data.get("password", None)
    user = User(username, password)

    if not username:
        return make_response("Please provide a username", 400)
    
    if not password:
        return make_response("Please provide a password", 400)

    user.login_user()
    return make_response('You are successfully logged in', 200)