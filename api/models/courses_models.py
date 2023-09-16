from api import db

class Course(db.Model):
    __tablename__ = 'curse'
    id_course = db.Column(db.Integer, nullable=False)
    nome_course = db.Column(db.String(50), nullable=False)
    desc_course = db.Column(db.String(100), nullable=False)
    publish_course = db.Column(db.Date, nullable=False)