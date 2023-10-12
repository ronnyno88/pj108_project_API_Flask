from api import ma
from ..models import course_model
from marshmallow import fields

#class defined to validate the fields of API
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_model.Course
        load_instance = True
        fields = ("id_course", "name", "workload", "discipline")

    name = fields.String(required=True)
    workload = fields.Float(required=True)
    discipline = fields.String(required=True)
