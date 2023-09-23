# defining initials parameter of app
# starting debug
DEBUG = True

# configs used for connecting database
USERNAME = "root"
PASSWORD = "1234"
SERVER = "localhost"
DB = "flask_api"

# configs used for starting e mapping the database (alchemy)
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
