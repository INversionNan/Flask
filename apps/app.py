from flask import Flask, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager

# app = Flask(__name__)

from config import config

mail = Mail()

db = SQLAlchemy()

bootstrap = Bootstrap()

login_manager = LoginManager()

login_manager.session_protection = 'strong'

login_manager.login_view = 'base.login'


# app.register_blueprint();
# app.register_blueprint();
# app.register_blueprint();

# books = [
#     {"id":1,"name":"盛婧雯"},
#     {"id":2,"name":"陈奕俊"},
# ]


# @app.route("/book/<int:book_id>")
# def book_detail(book_id):
#     print(book_id)
#     return "success"


# @app.route('/')  # Set the URL to access, in this case to a root path
# def hello_world():  # put application's code here
#     return 'Hello 盛婧雯!'

def create_app(config_name='development'):
    app = Flask(__name__)
    """
    config = {
       'development': DevelopmentConfig,
       'testing': TestingConfig,
       'production': ProductionConfig,
       'default': DevelopmentConfig
    }
    """

    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    mail.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    # Register the blueprint and associate it with the app
    from apps.base import base
    app.register_blueprint(base)
    from apps.user import user
    app.register_blueprint(user)
    from apps.todolist import todolist
    app.register_blueprint(todolist)

    with app.app_context():
        db.create_all()

    return app
