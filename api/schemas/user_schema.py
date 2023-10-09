from api import ma
from ..models import teacher_model
from marshmallow import fields
from ..schemas import discipline_schema
#class defined to validate the fields of API
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_model.Teacher
        load_instance = True
        fields = ("id", "login", "email", "password", "is_adm")

    #all fiels indicates below should be requerid
    login = fields.String(required=True)
    email = fields.String(required=True)
    password = fields.String(required=True)
    is_adm = fields.String(required=True)
