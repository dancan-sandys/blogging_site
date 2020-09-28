from flask import render_template,redirect, url_for,flash
from .forms import Blog, NewComment, Subscribe
from . import blogs
from ..models import Blogs,Comment, Subscriber
from .. import db
from ..request import load_quote
from flask_login import login_required
from ..email import mail
from ..subscriber import get_subscribers



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

        subscribers = get_subscribers()

        blog_id = blog_id
        title = form.title.data
        body = form.comment.data

        new_comment = Comment(blog_id = blog_id,title =title,body =body)

        new_comment.save_comment()

        mail("New Blogs","email/new_blogs",subscribers)

        return redirect(url_for('.postedblogs'))
    
    return render_template('comments/new.html',form = form)

@blogs.route('/subscibe', methods =['GET', 'POST'])
@login_required
def subscribe():
    form = Subscribe()
    if form.validate_on_submit():
        email = form.email.data

        new_subscriber = Subscriber(email = email)

        db.session.add(new_subscriber)
        db.session.commit()

        flash('You have successfully been added to our mailing list')
        return redirect(url_for('.postedblogs'))
    
    return render_template('subscribe.html', form =form)


@blogs.route('/quotes')
@login_required
def quote():
    quote = load_quote()

    return render_template('quotes.html', quote = quote)

    

