from api import ma
from ..models import discipline_model
from marshmallow import fields
from ..schemas import course_schema, teacher_schema

#class defined to validate the fields of API
class DisciplineSchema(ma.SQLAlchemyAutoSchema):
    teachers = ma.Nested(teacher_schema.TeacherSchema, many=True)
    class Meta:
        model = discipline_model.Discipline
        load_instance = True
        fields = ("id_discipline", "name_discipline", "desc_discipline", "courses", "teachers")

    #all fiels indicates below should be requerid
    name_discipline = fields.String(required=True)
    desc_discipline = fields.String(required=True)
    courses = fields.List(fields.Nested(course_schema.CourseSchema, only=('id_course', 'name_course')))

