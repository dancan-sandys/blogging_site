from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_mail import Mail

#instantiating flask extensions

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'
mail = Mail()


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

    #registering the profile blueprint
    from .profile import profile as profile_blueprint
    app.register_blueprint(profile_blueprint)

    #initializing flask extensions
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    return app