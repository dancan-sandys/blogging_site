from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,TextAreaField,SubmitField
from wtforms.validators import Required

class Blog(FlaskForm):
    title = db.StringField('What is the Blog title', validators = [Required()])
    body =TextAreaField('Write Down Your Blog', validators=[Required()])
    submit = SubmitField('Submit')
