from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from exts import mail, db
from flask_login import LoginManager

# app = Flask(__name__)

from config import config

# mail = Mail()

# db = SQLAlchemy()

bootstrap = Bootstrap()

login_manager = LoginManager()

login_manager.session_protection = 'strong'

login_manager.login_view = 'base.login'


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
    with app.app_context():
        from apps.base import base
        from apps.todolist.course import AddToDoList, ChangeToDoList
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
# if __name__ == '__main__':
#     app.run()
