import os

# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#          'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


class Config:
    """
    所有配置环境的基类, 包含通用配置
    """
    # 尤其是涉及(flask-wtf)登录注册里面提交敏感信息时，一定要加
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Yijun Chen'
    # flask-SQLAlchemy
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PER_PAGE = 5
    C_PAGE = 100
    @staticmethod
    def init_app(app):
        """
        初始化app，当前不用， 后续完善， 用来添加第三方插件的
        :param app:
        :return:
        """
        pass


class DevelopmentConfig(Config):
    Development = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
