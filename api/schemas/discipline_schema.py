from api import ma
from ..models import discipline_model
from marshmallow import fields
from ..schemas import course_schema, teacher_schema
class DisciplineSchema(ma.SQLAlchemyAutoSchema):
    teachers = ma.Nested(teacher_schema.TeacherSchema, many=True)
    class Meta:
        model = discipline_model.Discipline
        load_instance = True
        fields = ("id_discipline", "description", "courses", "teachers")

    description = fields.String(required=True)
    courses = fields.List(fields.Nested(course_schema.CourseSchema, only=('id_course', 'name')))
    teachers = fields.List(fields.Nested(teacher_schema.TeacherSchema, only=('id_teacher', 'name')))

