from flask_restful import Resource
from api import api

class CurseList(Resource):
    def get(self):
        return 'Hello World'

api.add_resource(CurseList, '/cursers')