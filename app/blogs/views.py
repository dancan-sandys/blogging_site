from flask import render_template,redirect, url_for
from .forms import Blog
from . import blogs
from ..models import Blogs


@blogs.route('/blogs/publish')
def newblog():

    form = Blog
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data

        new_blog = Blogs(title = title, body = body)



