from api import *

from api import db
# modeling the class used in methods of API
# this model will be created in database
class DisciplineModel(db.Model):
    __tablename__ = "discipline"
    id_discipline = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_discipline = db.Column(db.String(50), nullable=False)
    desc_discipline = db.Column(db.String(100), nullable=False)