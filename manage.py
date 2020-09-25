from flask import Flask
from .app import create_app
from flask_script import Manager,Server




app = create_app('development')

manager = Manager()

manager.add_command('server', Server)