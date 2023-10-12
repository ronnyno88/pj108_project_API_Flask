from api import ma
from ..models import teacher_model
from marshmallow import fields
from ..schemas import discipline_schema
class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id_teacher", "name", "graduate_level")

    name = fields.String(required=True)
    graduate_level = fields.String(required=True)
