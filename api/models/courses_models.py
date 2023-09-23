from api import *

from api import db
# modeling the class used in methods of API
# this model will be created in database
class Course(db.Model):
    __tablename__ = "course"
    id_course = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_course = db.Column(db.String(50), nullable=False)
    desc_course = db.Column(db.String(100), nullable=False)
    publish_course = db.Column(db.Date, nullable=False)

