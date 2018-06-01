from flask import Blueprint

user = Blueprint('user',__name__)

from module.user import views