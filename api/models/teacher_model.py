from api import db


# modeling the class used in methods of API
# this model contains the base for create the database
class Teacher(db.Model):
    # mappeding the name of table
    __tablename__ = "teacher"
    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_teacher = db.Column(db.String(50), nullable=False)
    age_teacher = db.Column(db.Integer, nullable=False)

    disciplines = db.relationship('Discipline', secondary='teacher_discipline', back_populates='teachers')
