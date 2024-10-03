from flask import Blueprint

auth = Blueprint('auth', __name__)

#import view at end to avoid circular imports 
from . import views
