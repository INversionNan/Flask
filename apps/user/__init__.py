from flask import Blueprint

user = Blueprint("user", __name__)
blog = Blueprint("blog", __name__, url_prefix="/blog")
blogindex = Blueprint("blogindex", __name__)

from . import base, blog, index
