import uuid
from threading import Thread

from flask import current_app, request,jsonify
from flask_mail import Mail, Message
from flask import render_template
from apps.base import base
from exts import mail
from flask_mail import Message, Mail
from apps.model import EmailCodeModel
from flask_login import login_user, logout_user, login_requires, current_user


# @base.route('/email_captcha/')
# @login_requires
# def email_captcha():
#     email = request.args.get('email')
#     if not email:
#         return restful.params_error('请输入邮箱')  # restful. 封装的函数，返回前端数据
#     '''`
#     生成随机验证码，保存到memcache中，然后发送验证码，与用户提交的验证码对比
#     '''
#     captcha = str(uuid.uuid1())[:6]  # 随机生成6位验证码
#     # 给用户提交的邮箱发送邮件
#     message = Message('Task List forum email verification code', recipients=[email], body='您的验证码是：%s' % captcha)
#     try:
#         mail.send(message)  # 发送
#     except:
#         return restful.server_error()
#     mbcache.set(email, captcha)
#     return restful.success()


def send_mail(send_to, filename, **kwargs):
    app = current_app._get_current_object()
    mail = Mail(app)
    with app.app_context():
        msg = Message(
            subject='测试',
            recipients=send_to,
            sender=app.config['MAIL_USERNAME'],
            html=render_template(filename + '.html',
                                 info=kwargs)
        )
        mail.send(msg)
