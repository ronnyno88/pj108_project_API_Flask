from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import course
from ..schemes import course_scheme
from ..services import course_service, discipline_service

#classes that response e request datas with methods HTTP
class CourseNoParameter(Resource):
    def get(self):
        courses = course_service.list_courses()
        course_sch = course_scheme.CourseScheme(many=True)
        return make_response(course_sch.jsonify(courses), 200)

    def post(self):
        course_sch = course_scheme.CourseScheme()
        validate = course_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name_course = request.json["name_course"]
            desc_course = request.json["desc_course"]
            publish_course = request.json["publish_course"]
            discipline = request.json["discipline"]
            discipline_course = discipline_service.list_discipline(discipline)

            if discipline_course is None:
                return make_response(jsonify("discipline not found"), 404)

            new_course = course.Course(name_course=name_course, desc_course=desc_course, publish_course=publish_course, discipline=discipline_course)
            csv_result = course_service.create_course(new_course)
            return make_response(course_sch.jsonify(csv_result), 201)


class CourseWithParameter(Resource):
    def get(self, id_course):
        new_course = course_service.list_course(id_course)
        if new_course is None:
            return make_response(jsonify("Not found"), 404)
        course_sch = course_scheme.CourseScheme()
        return make_response(course_sch.jsonify(new_course), 200)

    def put(self, id_course):
        db_course = course_service.list_course(id_course)
        if db_course is None:
            return make_response(jsonify("Not found"), 404)
        course_sch = course_scheme.CourseScheme()
        validate = course_sch.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_course = request.json["name_course"]
            desc_course = request.json["desc_course"]
            publish_course = request.json["publish_course"]

            discipline = request.json["discipline"]
            discipline_course = discipline_service.list_discipline(discipline)

            if discipline_course is None:
                return make_response(jsonify("discipline not found"), 404)

            new_course = course.Course(name_course=name_course, desc_course=desc_course, publish_course=publish_course,
                                       discipline=discipline_course)
            course_service.update_course(course, new_course)
            csv_result = course_service.list_course(id_course)
            return make_response(course_sch.jsonify(csv_result), 200)

    def delete(self, id_course):
        db_course = course_service.list_course(id_course)
        if db_course is None:
            return make_response(jsonify("Not found"), 404)
        course_service.delete_course(db_course)
        return make_response(jsonify("Deleted Successful"), 200)


api.add_resource(CourseNoParameter, '/courses')
api.add_resource(CourseWithParameter, '/course/<int:id_course>')
