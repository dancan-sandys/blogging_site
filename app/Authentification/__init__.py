from flask_blueprint import Blueprint
auth = Blueprint('auth',__name__)
from .  import views, forms