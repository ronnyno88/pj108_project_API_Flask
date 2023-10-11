from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify, request
from .services.user_service import list_user_api_key


def adm_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims["roles"] != "adm":
            return make_response(jsonify("acess dennited"), 403)
        else:
            return function(*args, **kwargs)

    return wrapper

def api_key_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        api_key = request.args.get("api_key")
        if api_key and list_user_api_key(api_key):
            return function(*args, **kwargs)
        else:
            return make_response(jsonify("access dennited"), 401)
    return wrapper