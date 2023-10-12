from api import db
from ..models import discipline_model
class Course(db.Model):
    __tablename__ = "courses"
    id_course = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    workload = db.Column(db.Float, nullable=False)

    discipline_id = db.Column(db.Integer, db.ForeignKey("discipline.id_discipline"))
    discipline = db.relationship(discipline_model.Discipline, backref=db.backref("courses", lazy="dynamic"))
