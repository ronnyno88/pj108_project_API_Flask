from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import user
from ..schemas import user_schema
from ..services import user_service
from flask_jwt_extended import jwt_required

#classes that response e request datas with methods HTTP
class UserList(Resource):
    #@jwt_required()
    def post(self):
        user_sch = user_schema.UserSchema()
        validate = user_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            login = request.json["login"]
            email = request.json["email"]
            password = request.json["password"]
            is_adm = request.json["is_adm"]

            new_user = user.User(login=login, email=email, password=password, is_adm=is_adm)
            csv_result = user_service.create_user(new_user)
            result = user_sch.jsonify(csv_result)
            return make_response(result, 201)

api.add_resource(UserList, '/users')
