from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import teacher
from ..schemas import teacher_schema
from ..services import teacher_service
from ..paginate import paginate
from ..models.teacher_model import Teacher
from flask_jwt_extended import jwt_required

#classes that response e request datas with methods HTTP
class Teachers(Resource):
    @jwt_required()
    def get(self):
        teacher_sch = teacher_schema.TeacherSchema(many=True)
        return paginate(Teacher, teacher_sch)
    @jwt_required()
    def post(self):
        teacher_sch = teacher_schema.TeacherSchema()
        validate = teacher_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_teacher = request.json["name_teacher"]
            age_teacher = request.json["age_teacher"]

            new_teacher = teacher.Teacher(name_teacher=name_teacher, age_teacher=age_teacher)
            csv_result = teacher_service.create_teacher(new_teacher)
            result = teacher_sch.jsonify(csv_result)
            return make_response(result, 201)


class TeacherResouces(Resource):
    @jwt_required()
    def get(self, id_teacher):
        new_teacher = teacher_service.list_teacher(id_teacher)
        if new_teacher is None:
            return make_response(jsonify("Not found"), 404)
        teacher_sch = teacher_schema.TeacherSchema()
        return make_response(teacher_sch.jsonify(new_teacher), 200)
    @jwt_required()
    def put(self, id_teacher):
        db_teacher = teacher_service.list_teacher(id_teacher)
        if db_teacher is None:
            return make_response(jsonify("Not found"), 404)
        teacher_sch = teacher_schema.TeacherSchema()
        validate = teacher_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_teacher = request.json["name_teacher"]
            age_teacher = request.json["age_teacher"]

            new_teacher = teacher.Teacher(name_teacher=name_teacher, age_teacher=age_teacher)
            teacher_service.update_teacher(teacher, new_teacher)
            csv_result = teacher_service.list_teacher(id_teacher)
            result = teacher_sch.jsonify(csv_result)
            return make_response(result, 201)
    @jwt_required()
    def delete(self, id_teacher):
        db_teacher = teacher_service.list_teacher(id_teacher)
        if db_teacher is None:
            return make_response(jsonify("Not found"), 404)
        teacher_service.delete_teacher(db_teacher)
        return make_response(jsonify("Deleted Successful"), 200)


api.add_resource(Teachers, '/teachers')
api.add_resource(TeacherResouces, '/teacher/<int:id_teacher>')
