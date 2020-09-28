from flask import Flask
from . import db
from flask_login import UserMixin
from . import login_manager


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def save_user(self):
        db.session.delete(self)
        db.session.commit()


    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))



class Comment(db.Model):

    __tablename__ = 'comments'

    id  = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(300))
    body = db.Column(db.String)
    user = db.relationship('User', backref = 'comment', lazy ='dynamic')
    blog_id = db.Column(db.Integer(), db.ForeignKey('blogs.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

class Blogs(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    user = db.relationship('User', backref = 'blog', lazy = 'dynamic')
    Comments = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delet(self)
        db.session.commit()

class Quotes():

    def __init__(self, author , quote):
        self.author = author
        self.quote = quote

class Subscriber(db.Model):
    __tablename__ = 'subscribers'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String)