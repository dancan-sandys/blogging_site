from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, SelectField, PasswordField
from wtforms.validators import ValidationError, Email, Required, EqualTo
from ..models import User

class SignUp(FlaskForm):
    username = StringField('Username:', validators=[Required()] )
    email = StringField('Email:', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(),EqualTo('confirm_password', 'Passwords must match')])
    confirm_password = PasswordField('Confirm Password', validators=[Required()])
    sign_up = SubmitField('Sign Up')

    def validate_username(self,inputed_name):
        if User.query.filter_by(username = inputed_name).first():
            raise ValidationError('username already exists')

    def validate_email(self, inputed_email):
        if User.query.filter_by(email = inputed_email):
            raise ValidationError('The email address has already been used')



class SignIn(FlaskForm):
    username = StringField('Username:', validators=[Required()] )
    email = StringField('Email:', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    Remember = BooleanField('Remember me')
    sign_in = SubmitField('Sign In')





