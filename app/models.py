from flask import Flask
from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    profile_pic = db.Column(db.String)
    bio = db.Column(db.String)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))

class Comment(db.Model):

    __tablename__ = 'comments'

    id  = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(300))
    body = db.Column(db.String)
    user = db.relationship('User', backref = 'comment', lazy ='dynamic')
    blog_id = db.Column(db.Integer(), db.ForeignKey('blogs.id'))


class Blogs(db.Model):

    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    user = db.relationship('User', backref = 'blog', lazy = 'dynamic')
    Comment = db.relationship('Comment', backref = 'blog', lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def delete_blog(self):
        db.session.delet(self)
        db.session.commit()

class Quotes():

    def __init__(self, quote):
        self.quote = quote