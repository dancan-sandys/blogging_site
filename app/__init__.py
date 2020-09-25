from flask import Flask
from config import config_options


def create_app(config_option):


    app = Flask(__name__)

    #setting up configurations
    app.config.from_object(config_options[config_option])
    config_options[config_option].init_app(app)