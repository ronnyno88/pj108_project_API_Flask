from api import ma
from ..models import course_model
from marshmallow import fields

#class defined to validate the fields of API
class CourseScheme(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_model.CourseModel
        load_instance = True
        fields = ("id_course", "name_course", "desc_course", "publish_course")

    #all fiels indicates below should be requerid
    name_course = fields.String(required=True)
    desc_course = fields.String(required=True)
    publish_course = fields.Date(required=True)

