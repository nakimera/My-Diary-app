from flask import Blueprint, make_response
from .models import Entry

mod = Blueprint('entry', __name__)