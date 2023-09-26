from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import discipline
from ..schemes import discipline_scheme
from ..services import discipline_service

#classes that response e request datas with methods HTTP
class DisciplineNoParameter(Resource):
    def get(self):
        disciplines = discipline_service.list_disciplines()
        discipline_sch = discipline_scheme.DisciplineScheme(many=True)
        return make_response(discipline_sch.jsonify(disciplines), 200)

    def post(self):
        discipline_sch = discipline_scheme.DisciplineScheme()
        validate = discipline_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_discipline = request.json["name_discipline"]
            desc_discipline = request.json["desc_discipline"]

            new_discipline = discipline.Discipline(name_discipline=name_discipline, desc_discipline=desc_discipline)
            csv_result = discipline_service.create_discipline(new_discipline)
            result = discipline_sch.jsonify(csv_result)
            return make_response(result, 201)


class DisciplineWithParameter(Resource):

    def get(self, id_discipline):
        new_discipline = discipline_service.list_discipline(id_discipline)
        if new_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_sch = discipline_scheme.DisciplineScheme()
        return make_response(discipline_sch.jsonify(new_discipline), 200)

    def put(self, id_discipline):
        db_discipline = discipline_service.list_discipline(id_discipline)
        if db_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_sch = discipline_scheme.DisciplineScheme()
        validate = discipline_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_discipline = request.json["name_discipline"]
            desc_discipline = request.json["desc_discipline"]

            new_discipline = discipline.Discipline(name_discipline=name_discipline, desc_discipline=desc_discipline)
            discipline_service.update_discipline(discipline, new_discipline)
            csv_result = discipline_service.list_discipline(id_discipline)
            result = discipline_sch.jsonify(csv_result)
            return make_response(result, 201)

    def delete(self, id_discipline):
        db_discipline = discipline_service.list_discipline(id_discipline)
        if db_discipline is None:
            return make_response(jsonify("Not found"), 404)
        discipline_service.delete_discipline(db_discipline)
        return make_response(jsonify("Deleted Successful"), 200)


api.add_resource(DisciplineNoParameter, '/disciplines')
api.add_resource(DisciplineWithParameter, '/discipline/<int:id_discipline>')
