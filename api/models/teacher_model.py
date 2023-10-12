from api import db
class Teacher(db.Model):
    __tablename__ = "teacher"
    id_teacher = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    graduate_level = db.Column(db.String(50), nullable=False)

    disciplines = db.relationship('Discipline', secondary='teacher_discipline', back_populates='teachers')
