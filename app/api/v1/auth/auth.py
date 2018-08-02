from flask import request
from functools import wraps
import jwt
from app.api.v1.auth.models import User

def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None

        if "access-token" in request.headers:
            token = request.headers['access-token']
        if not token:
            return jsonify({
                "message" : "Token is missing"
            }), 403
        try:
            data = User.decode_auth_token(token)
        except:
            return jsonify({
                "message" : "Token is invalid"
            }), 403