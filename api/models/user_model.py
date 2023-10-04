from api import db
from passlib.hash import pbkdf2_sha256

# modeling the class used in methods of API
# this model contains the base for create the database
class User(db.Model):
    # mappeding the name of table
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    login = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def encript(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def disencript(self, password):
        return pbkdf2_sha256.verify(password, self.password)