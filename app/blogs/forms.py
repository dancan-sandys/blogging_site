from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,TextAreaField,SubmitField
from wtforms.validators import Required

class Blog(FlaskForm):
    title = StringField('What is the Blog title', validators = [Required()])
    body =TextAreaField('Write Down Your Blog', validators=[Required()])
    submit = SubmitField('Submit')
class NewComment(FlaskForm):

    title = StringField('Enter the title of the comment')
    comment = TextAreaField('Write Down your comments bellow')
    submit = SubmitField('comment')