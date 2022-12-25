import os
import logging
# 获取当前项目的绝对路径;
basedir = os.path.abspath(os.path.dirname(__file__))

# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#          'sqlite:///' + os.path.join(basedir, 'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

# 邮箱配置
# MAIL_USE_TLS：端口号587
# MAIL_USE_SSL：端口号465
# QQ邮箱不支持非加密方式发送邮件
# 发送者邮箱的服务器地址



class Config:
    """
    所有配置环境的基类, 包含通用配置
    """
    LOG_LEVEL = logging.DEBUG
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

    DEBUG = True
    # 邮箱配置
    # MAIL_USE_TLS：端口号587
    # MAIL_USE_SSL：端口号465
    # QQ邮箱不支持非加密方式发送邮件
    # 发送者邮箱的服务器地址
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL
    MAIL_USERNAME = "1052601616@qq.com"
    MAIL_PASSWORD = "zztasmtbvegxbbhb"  # 生成授权码，授权码是开启smtp服务后给出的
    MAIL_DEFAULT_SENDER = "1052601616@qq.com"
    Development = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL
    MAIL_USERNAME = "1052601616@qq.com"
    MAIL_PASSWORD = "zztasmtbvegxbbhb"  # 生成授权码，授权码是开启smtp服务后给出的
    MAIL_DEFAULT_SENDER = "1052601616@qq.com"
    Development = True
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


class ProductionConfig(Config):
    DEBUG = False
    MAIL_SERVER = "smtp.qq.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    # MAIL_USE_SSL
    MAIL_USERNAME = "1052601616@qq.com"
    MAIL_PASSWORD = "zztasmtbvegxbbhb"  # 生成授权码，授权码是开启smtp服务后给出的
    MAIL_DEFAULT_SENDER = "1052601616@qq.com"
    Development = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

