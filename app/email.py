from flask_mail import Message
from flask import render_template
from . import mail

def mail(Subject, template, to,**kwargs ):
    sender = dancan.oruko99@gmail.com

    email = Message(Subject,sender = sender, recipients=[to])
    email.body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.txt', **kwargs)
    mail.send(email)