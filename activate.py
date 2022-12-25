from flask import Flask
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from apps.app import create_app, db
from apps.model import User, Role

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)


def shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


if __name__ == '__main__':
    manager.add_command("shell", Shell(make_context=shell_context))
    manager.add_command("db", MigrateCommand)
    manager.run()
