from api import ma
from ..models import teacher_model
from marshmallow import fields
from ..schemas import discipline_schema
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id", "login", "email", "password", "is_adm", "api_key")

    login = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    is_adm = fields.Boolean(required=True)
    api_key = fields.String(required=False)
