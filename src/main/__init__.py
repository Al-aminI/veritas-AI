from flask import Flask

from flask_bcrypt import Bcrypt
from flask_cors import CORS
from .config import config_by_name
import os


flask_bcrypt = Bcrypt()


def create_app(config_name):
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024 
    app.config['JWT_SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret_key')
    # JWTManager(app)

    CORS(app)
    app.config.from_object(config_by_name[config_name])
    # api.init_app(app)
    # db.init_app(app)
    flask_bcrypt.init_app(app)

    return app