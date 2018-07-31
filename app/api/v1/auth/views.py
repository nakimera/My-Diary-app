from flask import Blueprint, make_response
import psycopg2
from .models import User

mod = Blueprint('auth', __name__)

@mod.route('/signup', methods=['POST'])
def signup():
    return make_response('User successfully signed up', 200)

@mod.route('/login', methods=['POST'])
def login():
    return make_response('You are successfully logged in', 200)