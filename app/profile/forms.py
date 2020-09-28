from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField,StringField,BooleanField
from wtforms.validators import Required

class bio(FlaskForm):

    bio = StringField('Tell us about you', validators=[Required()])
    submit = SubmitField('Update')

