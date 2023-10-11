from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask import make_response, jsonify


def adm_required(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        clains = get_jwt()
        if clains["roles"] != "adm":
            return make_response(jsonify(message="acess dennited"), 403)
        else:
            return function(*args, **kwargs)

    return wrapper
