from flask import render_template,redirect, url_for
from .forms import Blog
from . import blogs
from ..models import Blogs
from .. import db

@blogs.route('/blogs/publish', methods = ['POST', 'GET'])
def newblog():

    form = Blog()
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        new_blog = Blogs(title = title, body = body)

        new_blog.save_blog()

        return redirect(url_for('.postedblogs'))
        
    return render_template('blogs/new.html', form = form)

@blogs.route('/blogs/posted')
def postedblogs():

    blogs = Blogs.query.all()

    return render_template('blogs/posted.html', blogs = blogs)


