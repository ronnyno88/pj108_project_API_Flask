from api import db

# modeling the class used in methods of API
# this model contains the base for create the database

class Discipline(db.Model):
    #mappeding the name of table
    __tablename__ = "discipline"
    id_discipline = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name_discipline = db.Column(db.String(50), nullable=False)
    desc_discipline = db.Column(db.String(100), nullable=False)

    #describe type of relation beetheen tables
    courses = db.relationship("Course", back_populates='discipline')
