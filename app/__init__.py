from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

#instantiating flask extensions

db = SQLAlchemy()


def create_app(config_option):


    app = Flask(__name__)

    #setting up configurations
    app.config.from_object(config_options[config_option])
    config_options[config_option].init_app(app)

    #Registering the blogs blueprint
    from .blogs import blogs as blogs_blueprint
    app.register_blueprint(blogs_blueprint)

    #registering the authentification blueprint
    from Authentification import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #initializing flask extensions
    db.init_app(app)