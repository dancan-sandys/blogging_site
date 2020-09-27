from flask import render_template,redirect, url_for
from .forms import Blog, NewComment
from . import blogs
from ..models import Blogs,Comment
from .. import db
from ..request import load_quote
from flask_login import login_required

@blogs.route('/blogs/publish', methods = ['POST', 'GET'])
@login_required
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
@blogs.route('/')
def postedblogs():

    blogs = Blogs.query.all()
    comments = Comment.query.all()

    return render_template('blogs/posted.html', blogs = blogs, comments = comments)

@blogs.route('/blogs/<blog_id>/new/comments', methods = ['GET', 'POST'])
@login_required
def newcomment(blog_id):

    form = NewComment()
    if form.validate_on_submit():

        blog_id = blog_id
        title = form.title.data
        body = form.comment.data

        new_comment = Comment(blog_id = blog_id,title =title,body =body)

        new_comment.save_comment()

        return redirect(url_for('.postedblogs'))
    
    return render_template('comments/new.html',form = form)



@blogs.route('/quotes')
@login_required
def quote():
    quote = load_quote()

    return render_template('quotes.html', quote = quote)

    

