from os import terminal_size

from ..entitys import teacher
from ..models import discipline_model, teacher_model
from .teacher_service import list_teacher
from api import db
def create_discipline(discipline):
    discipline_db = discipline_model.Discipline(description=discipline.description)
    for i in discipline.teachers:
        teacher = list_teacher(i)
        discipline_db.teachers.append(teacher)
    db.session.add(discipline_db)
    db.session.commit()
    return discipline_db

def list_disciplines():
    disciplines = discipline_model.Discipline.query.all()
    return disciplines

def list_discipline(id_discipline):
    discipline = (discipline_model.Discipline.query.filter_by(id_discipline=id_discipline).first())
    return discipline

def update_discipline(previous_discipline, new_discipline):
    previous_discipline.name_discipline = new_discipline.name_discipline
    previous_discipline.description = new_discipline.description
    for i in new_discipline.teachers:
        teacher = list_teacher(i)
        previous_discipline.teachers.append(teacher)
    db.session.commit()

def delete_discipline(discipline):
    db.session.delete(discipline)
    db.session.commit()