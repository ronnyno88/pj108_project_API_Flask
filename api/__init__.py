from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

import config

# creating the app flask
app = Flask(__name__)
# defining live reload of app, recovery the module config
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["DEBUG"] = config.DEBUG
app.config["SECRET_KEY"] = "flask_api"

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

# creating the API restful with parameter app of app flask
api = Api(app)

# implemetation of web token
jwt = JWTManager(app)

# importing the modules
from .views import course_view, discipline_view, teacher_view, user_view, refresh_token_view
from .models import course_model, discipline_model, teacher_model, user_model
