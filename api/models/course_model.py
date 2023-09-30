from api import db
from ..models import discipline_model
# modeling the class used in methods of API
# this model will be created in database
class Course(db.Model):
    __tablename__ = "course"
    id_course = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_course = db.Column(db.String(50), nullable=False)
    desc_course = db.Column(db.String(100), nullable=False)
    publish_course = db.Column(db.Date, nullable=False)
    #field that identifies the foreignkey of the disciplines table reference
    discipline_id = db.Column(db.Integer, db.ForeignKey("discipline.id_discipline"))
    #determine the reference for relationship many_to_one(curses-discipline)
    discipline = db.relationship(discipline_model.Discipline, backref=db.backref("courses", lazy="dynamic"))
