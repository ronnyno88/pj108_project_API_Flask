from api import db
from .teacher_model import Teacher
# modeling the class used in methods of API
# this model contains the base for create the database

teacher_discipline = db.Table('teacher_discipline',
    db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id_teacher'), primary_key=True, nullable=False),
    db.Column('discipline_id', db.Integer, db.ForeignKey('discipline.id_discipline'), primary_key=True, nullable=False)
)

class Discipline(db.Model):
    #mappeding the name of table
    __tablename__ = "discipline"
    id_discipline = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)

    #describe type of relation beetheen tables
    teachers = db.relationship(Teacher, secondary='teacher_discipline', back_populates='disciplines')
