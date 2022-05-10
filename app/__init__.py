from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

db = SQLAlchemy()

def create_app (environment):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_options[environment])
    db.init_app(app)
    from .main import auth
    app.register_blueprint(auth)

    return app
