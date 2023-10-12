from ..models import teacher_model
from api import db
def create_teacher(teacher):
    teacher_db = teacher_model.Teacher(name_teacher=teacher.name_teacher, age_teacher=teacher.age_teacher)
    db.session.add(teacher_db)
    db.session.commit()
    return teacher_db

def list_teachers():
    teachers = teacher_model.Teacher.query.all()
    return teachers

def list_teacher(id_teacher):
    teacher = (teacher_model.Teacher.query.filter_by(id_teacher=id_teacher).first())
    return teacher

def update_teacher(previous_teacher, new_teacher):
    previous_teacher.name_teacher = new_teacher.name_teacher
    previous_teacher.age_teacher = new_teacher.age_teacher
    db.session.commit()

def delete_teacher(teacher):
    db.session.delete(teacher)
    db.session.commit()