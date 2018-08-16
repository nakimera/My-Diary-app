from flask import request, jsonify
from functools import wraps
import jwt
from app.api.v1.auth.models import User
from app.config import Config

def token_required(func):
    """
    Method that restricts access to entries routes
    """

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
            data = jwt.decode(token, Config.SECRET_KEY)
            user_id = data['sub']

        except jwt.ExpiredSignatureError:
            return jsonify({
                'message' : 'Signature expired. Please log in again.'
            }), 403

        except jwt.InvalidTokenError:
            return jsonify({
                "message" : "Invalid token. Please try again."
            }), 403            

        except Exception:
            return jsonify({
                "message" : "Token is invalid"
            }), 403
        
        return func(user_id, *args, **kwargs)
    return decorated