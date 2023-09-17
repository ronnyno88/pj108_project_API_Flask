from flask_restful import Resource
from api import api
from flask import request, jsonify, make_response
from ..entitys import courses
from ..schemes import courses_schemes
from ..services import courses_services

class CourseList(Resource):
    def get(self):
        return 'Hello World'
    def post(self):
        csm  = courses_schemes.CourseScheme
        validate = csm.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 404)
        else:
            name_course = request.json("name_course")
            desc_course = request.json("desc_course")
            publish_course = request.json("publish_course")

            new_course = courses.Courses(name_course=name_course, desc_course=desc_course, publish_course=publish_course)
            csv_result = courses_services.create_course(new_course)

            return make_response(csm.jsonify(csv_result), 201)


api.add_resource(CourseList, '/coursers')
