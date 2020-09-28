from flask import Flask
from app import create_app
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import Comment, Blogs,User, Quotes
from app import db



app = create_app('production')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server', Server)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app= app, db =db, Comment = Comment, Blogs =Blogs, User = User, Quotes =Quotes)

if __name__ == '__main__':
    manager.run()