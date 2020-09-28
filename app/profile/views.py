from flask import render_template, redirect, url_for, request
from . import profile
from .. import db,photos
from ..models import User
from flask_login import login_required
from ..models import User
from .forms import bio


@profile.route('/user/profile/<uname>', methods= ['GET', 'POST'])
@login_required
def Profile(uname):
    user = User.query.filter_by(username = uname).first()

    return render_template('profile/profile.html' , user = user)

@profile.route('/user/update/profilepic/<uname>', methods = ['GET', 'POST'])
@login_required
def updateprofile(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()

    return redirect(url_for('profile.Profile', uname = uname))

@profile.route('/user/update/bio/<uname>', methods= ['GET', 'POST'])
@login_required
def updatebio(uname):
    user = User.query.filter_by(username = uname).first()
    form =bio()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.commit()

        return redirect(url_for('profile.Profile', uname = user.username))

    return render_template ('profile/bio.html', form =form, user = user)


