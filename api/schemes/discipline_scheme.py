from api import ma
from ..models import discipline_model
from marshmallow import fields
from ..schemes import course_scheme, teacher_scheme

#class defined to validate the fields of API
class DisciplineScheme(ma.SQLAlchemyAutoSchema):
    teachers = ma.Nested(teacher_scheme.TeacherScheme, many=True)
    class Meta:
        model = discipline_model.Discipline
        load_instance = True
        fields = ("id_discipline", "name_discipline", "desc_discipline", "courses", "teachers")

    #all fiels indicates below should be requerid
    name_discipline = fields.String(required=True)
    desc_discipline = fields.String(required=True)
    courses = fields.List(fields.Nested(course_scheme.CourseScheme, only=('id_course', 'name_course')))

