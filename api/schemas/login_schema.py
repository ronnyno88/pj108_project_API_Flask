from api import ma
from ..models import teacher_model
from marshmallow import fields
from ..schemas import discipline_schema
class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id", "login", "email", "password")

    login = fields.String(required=False)
    email = fields.String(required=True)
    password = fields.String(required=True)
