from ..models import discipline_model
from api import db

#methods for manipulate DB
def create_discipline(discipline):
    discipline_db = discipline_model.DisciplineModel(name_discipline=discipline.name_discipline, desc_discipline=discipline.desc_discipline)
    db.session.add(discipline_db)
    db.session.commit()
    return discipline_db

def list_disciplines():
    disciplines = discipline_model.DisciplineModel.query.all()
    return disciplines

def list_discipline(id_discipline: object) -> object:
    discipline = discipline_model.DisciplineModel.query.filter_by(id_discipline=id_discipline).first()
    return discipline

def update_discipline(previous_discipline, new_discipline):
    previous_discipline.name_discipline = new_discipline.name_discipline
    previous_discipline.desc_discipline = new_discipline.desc_discipline
    db.session.commit()

def delete_discipline(discipline):
    db.session.delete(discipline)
    db.session.commit()