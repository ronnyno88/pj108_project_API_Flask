from ..models import user_model
from api import db


#methods for manipulate DB
def create_user(user):
    user_db = user_model.User(login=user.login, email=user.email, password=user.password)
    user_db.encript()
    db.session.add(user_db)
    db.session.commit()
    return user_db

def list_user(email):
    return user_model.User.query.filter_by(email=email).first()
