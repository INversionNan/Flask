from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, login_required

from apps.base.list import RegisterList, LoginList
from apps.base import base
# from apps.base.__init__ import base
from apps.model import User,EmailCodeModel
from apps.app import db
from exts import mail
import string
import random
from flask_mail import Message


# use blueprint and manage route
@base.route('/')
def index():
    return render_template('base/index.html')


@base.route('/register', methods=['POST', 'GET'])
def register():
    """
    /register:
        - GET: 获取注册页面
        - POST：获取注册页面提交的数据信息
            1). 判断是否为POST方法提交数据, 并且数据是否通过表单验证.
            2). 如果通过验证， 将表单提交的数据存储到数据库中,注册成功，跳转到登录页面.

            获取表单提交的数据， 有两种方式:
                *). form.data   {'email': 'hello@qq.com', 'username': 'hello'}
                *). form.email.data, form.username.data
    :return:
    """
    list = RegisterList()
    if list.validate_on_submit():
        new_user = User()
        new_user.username = list.username.data
        new_user.password = list.password.data
        new_user.email = list.email.data
        # new_user.role = Role.query.filter_by(name="VIP").first()
        db.session.add(new_user)
        flash("New user %s has registered successfully" % new_user.username, category='success')
        # token = new_user.generate_token()
        return redirect(url_for('base.login'))
    return render_template('base/register.html', form=list)


@base.route('/login', methods=['GET', 'POST'])
def login():
    list = LoginList()
    if list.validate_on_submit():
        user = User.query.filter_by(email=list.email.data).first()
        if user is not None and user.verify(list.password.data):
            login_user(user)
            user.ping()
            flash("User %s has loginned successfully" % user.username, category='success')
            return redirect(url_for('todolist.list_1'))
        else:
            flash("User %has failed to login" % list.email.data, category='error')
            return redirect(url_for('base.login'))
    return render_template('base/login.html', form=list)


@base.route('/logout')
@login_required
def logout():
    logout_user()
    flash("User has logged out successfully", category='success')
    return redirect(url_for('base.index'))


# send certification code
@base.route("/certificationCode/email")
def get_certification_code():
    email = request.args.get("email")
    source = string.digits * 4
    code = random.sample(source, 4)
    code = "".join(code)
    message = Message(subject="certificationCode", recipients=[email], body=f"Your certification code is: {code}")
    mail.send(message)
    email_code = EmailCodeModel(email=email, code=code)
    db.session.add(email_code)
    db.session.commit()
    # print(code)
    return jsonify({"code": 200, "message": "", "data": None})


@base.route("/mailtest")
def my_mail():
    message = Message(subject="sendEmail", recipients=["1052601616@qq.com"], body="test")
    mail.send(message)
    return "send successfully"
