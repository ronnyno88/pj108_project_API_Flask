from flask_restful import Resource
from api import api


class CourseList(Resource):
    def get(self):
        return 'Hello World'


api.add_resource(CourseList, '/coursers')
