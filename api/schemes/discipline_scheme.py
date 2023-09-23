from api import ma
from ..models import discipline_model
from marshmallow import fields

#class defined to validate the fields of API
class DisciplineScheme(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = discipline_model.DisciplineModel
        load_instance = True
        fields = ("id_discipline", "name_discipline", "desc_discipline")

    #all fiels indicates below should be requerid
    name_discipline = fields.String(required=True)
    desc_discipline = fields.String(required=True)
