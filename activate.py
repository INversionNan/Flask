from flask import Flask
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from apps.app import create_app, db
from apps.model import User, Role

app = create_app("development")
manager = Manager(app)
migrate = Migrate(app, db)

@manager.command
def tests():
    """
    Execute test cases for the Flask project
    """
    import unittest
    # 发现所有的测试用例(TestCase)绑定成一个测试集合(TestSuite), TestLoader
    tests = unittest.TestLoader().discover('tests')
    # verbosity是测试结果的信息复杂度，有0、1、2 三个值
    unittest.TextTestRunner(verbosity=2).run(tests)

def shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


if __name__ == '__main__':
    manager.add_command("shell", Shell(make_context=shell_context))
    manager.add_command("db", MigrateCommand)
    manager.run()
