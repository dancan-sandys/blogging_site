from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

#instantiating flask extensions

db = SQLAlchemy()
bootstrap = Bootstrap()


def create_app(config_option):


    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #setting up configurations
    app.config.from_object(config_options[config_option])
    config_options[config_option].init_app(app)

    # Registering the blogs blueprint
    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    #registering the authentification blueprint
    from .Authentification import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #initializing flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    return app