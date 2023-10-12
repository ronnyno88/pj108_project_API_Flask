from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow


import config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = config.DEBUG
app.config["SECRET_KEY"] = "flask_api"

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

api = Api(app)

jwt = JWTManager(app)

from .views import course_view, discipline_view, teacher_view, user_view, refresh_token_view, login_view
from .models import course_model, discipline_model, teacher_model, user_model
