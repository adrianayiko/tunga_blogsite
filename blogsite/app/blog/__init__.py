from flask import Blueprint

blog = Blueprint('blog', __name__,template_folder="templates")

from . import views
