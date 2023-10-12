from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import discipline
from ..schemas import discipline_schema
from ..services import discipline_service
from ..paginate import paginate
from ..models.discipline_model import Discipline
from flask_jwt_extended import jwt_required
class Disciplines(Resource):
    @jwt_required()
    def get(self):
        discipline_sch = discipline_schema.DisciplineSchema(many=True)
        return paginate(Discipline, discipline_sch)

    @jwt_required()
    def post(self):
        discipline_sch = discipline_schema.DisciplineSchema()
        validate = discipline_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            description = request.json["description"]
            teachers = request.json["teachers"]

            new_discipline = discipline.Discipline(description=description, teachers=teachers)
            csv_result = discipline_service.create_discipline(new_discipline)
            result = discipline_sch.jsonify(csv_result)
            return make_response(result, 201)


class DisciplineResource(Resource):
    @jwt_required()
    def get(self, id_discipline):
        new_discipline = discipline_service.list_discipline(id_discipline)
        if new_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_sch = discipline_schema.DisciplineSchema()
        return make_response(discipline_sch.jsonify(new_discipline), 200)
    @jwt_required()
    def put(self, id_discipline):
        db_discipline = discipline_service.list_discipline(id_discipline)
        if db_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_sch = discipline_schema.DisciplineSchema()
        validate = discipline_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            description = request.json["description"]
            teachers = request.json["teachers"]

            new_discipline = discipline.Discipline(description=description, teachers=teachers)
            discipline_service.update_discipline(db_discipline, new_discipline)
            csv_result = discipline_service.list_discipline(id_discipline)
            result = discipline_sch.jsonify(csv_result)
            return make_response(result, 201)
    @jwt_required()
    def delete(self, id_discipline):
        db_discipline = discipline_service.list_discipline(id_discipline)
        if db_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_service.delete_discipline(db_discipline)
        return make_response(jsonify("Deleted Successful"), 200)


api.add_resource(Disciplines, '/disciplines')
api.add_resource(DisciplineResource, '/discipline/<int:id_discipline>')
