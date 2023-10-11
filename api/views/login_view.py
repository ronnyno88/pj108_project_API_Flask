from flask_restful import Resource
from api import api, jwt
from flask import request, jsonify, make_response
from ..schemas import login_schema
from ..services import user_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

# classes that response e request datas with methods HTTP
class LoginList(Resource):
    @jwt.additional_claims_loader#verificação de papeis(clains) do usuário(is_adm)
    def add_clains_to_access_token(identity):#verifica clains do usuario
        user_token = user_service.list_user_id(identity)
        if user_token.is_adm:
            roles = "adm"
        else:
            roles = "user"
        return {"roles":roles}
    def post(self):
        login_sch = login_schema.LoginSchema()
        validate = login_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            email = request.json["email"]
            password = request.json["password"]
            db_user = user_service.list_user(email)

            if db_user and db_user.disencript(password):
                access_token = create_access_token(
                    identity=db_user.id,
                    expires_delta=timedelta(seconds=100)
                )
                refresh_token = create_refresh_token(
                    identity=db_user.id
                )
                return make_response(jsonify({
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                    "message": "Sucessful!"
                }), 200)
            return make_response(jsonify({
                "message": "Fault, Invalids datas!"
            }), 401)


api.add_resource(LoginList, '/login')
