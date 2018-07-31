from flask import Blueprint, make_response, request
import psycopg2
from .models import User

mod = Blueprint('auth', __name__)

@mod.route('/signup', methods=['POST'])
def signup():
    data = request.get_json(force=True)
    username = data.get("username", None)
    email_address = data.get("email_address", None)
    password = data.get("password", None)
    user = User(username, email_address, password)

    user.add_user()


    return make_response('User successfully signed up', 200)

@mod.route('/login', methods=['POST'])
def login():
    return make_response('You are successfully logged in', 200)