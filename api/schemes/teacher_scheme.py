from api import ma
from ..models import teacher_model
from marshmallow import fields
from ..schemes import discipline_scheme
#class defined to validate the fields of API
class TeacherScheme(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id_teacher", "name_teacher", "age_teacher")

    #all fiels indicates below should be requerid
    name_teacher = fields.String(required=True)
    age_teacher = fields.Integer(required=True)
