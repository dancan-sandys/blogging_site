from flask import render_template, redirect, url_for
from . import profile


@profile.route('/user/profile/<uname>')
def profile(uname):

    return render_template('profile/profile.html')







