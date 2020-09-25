from flask_blueprint import Blueprint
blogs = Blueprint('blogs',__name__)
from . import views, forms 