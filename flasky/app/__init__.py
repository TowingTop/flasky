from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)

    app.debug = True
    from .api_v1 import api as api_v1_blueprint
    app.register_blueprint(api_v1_blueprint, url_prefix='/api/v1')

    return app