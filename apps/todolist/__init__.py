from flask import Blueprint

# todolist = Blueprint("apps", __name__, url_prefix="/todolist")
todolist = Blueprint("todolist", __name__)

from . import base
