from flask import current_app
from apps.app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from authlib.jose import jwt, JoseError

# from datetime import datetimepicker

table_user_comment = db.Table("table_user_comment",
                              db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                              db.Column("comment_id", db.Integer, db.ForeignKey("comment.id"), primary_key=True))

table_user_role = db.Table("table_user_role",
                           db.Column("user_id", db.Integer, db.ForeignKey("users.id"), primary_key=True),
                           db.Column("role_id", db.Integer, db.ForeignKey("role.id"), primary_key=True))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    pass_word = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200))
    phone_number = db.Column(db.String(50))
    confirmed = db.Column(db.Boolean, default=False)

    # new user information
    name = db.Column(db.String(200))
    location = db.Column(db.String(200))
    information = db.Column(db.String(200))

    # create time date and the argument 'default' can accept the function as the default value
    create_time = db.Column(db.DateTime, default=datetime.utcnow())
    last = db.Column(db.DateTime(), default=datetime.utcnow())

    # foreign key link
    # Role_id = db.relationship("Role", secondary=table_user_role, backref=db.backref("user"))
    tasks = db.relationship('Task', backref='user')

    # 反向引用: 1). User添加属性categories   2). Category添加属性user
    categories = db.relationship('Kind', backref='user')

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.pass_word = generate_password_hash(password)

    def verify(self, password):
        return check_password_hash(self.pass_word, password)

    def generate_token(self, operation, **kwargs):
        header = {'alg': 'HS256'}
        secret_key = current_app.config['SECRET_KEY']
        data = {'id': User.id, 'operation': operation}
        data.update(**kwargs)
        return jwt.encode(header=header, payload=data, key=secret_key)

    def validate_token(self, token, operation):
        """用于验证用户注册和用户修改密码或邮箱的token, 并完成相应的确认操作"""
        secret_key = current_app.config['SECRET_KEY']
        try:
            data = jwt.decode(token, secret_key)
            print(data)
        except JoseError:
            return False
        # 其他字段确认
        else:
            self.confirmed = True
            db.session.add(self)
            db.session.commit()
            return True

    # def confirm(self,token):

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def __repr__(self):
        return "<User: %s>" % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

    # num = db.Column(db.Integer,default=10)
    def __repr__(self):
        return "<Role: %s>" % self.name


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    task_Title = db.Column(db.String(200))  # task  title
    task_content = db.Column(db.String(200))  # task content
    task_status = db.Column(db.Boolean, default=False)  # task status
    task_time = db.Column(db.DateTime, default=datetime.utcnow)  # task create time
    task_deadline = db.Column(db.DateTime)
    # task_deadline = db.Column(db.DateTime, default=datetime.time(task_time))
    task_urgent = db.Column(db.Integer, default=False)  # task priority

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('kinds.id'))

    def __repr__(self):
        return "Task %s" % (self.task_content[:7])


class Kind(db.Model):
    __tablename__ = 'kinds'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    add_time = db.Column(db.DateTime, default=datetime.utcnow)  # task create time
    # User:Category=1:N
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # 反向引用
    tasks = db.relationship('Task', backref='kind')

    def __repr__(self):
        return "<Category %s>" % self.name


class EmailCodeModel(db.Model):
    __tablename__ = "email_code"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    code = db.Column(db.String(100))
    # used = db.Column(db.Boolean)


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(128))
    text = db.Column(db.TEXT)
    create_time = db.Column(db.String(64))
    # 关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', backref='user')


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(256))  # 评论内容
    create_time = db.Column(db.String(64))
    # 关联博客id
    blog_id = db.Column(db.Integer, db.ForeignKey("blog.id"))
    # 关联用户id
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    blog = db.relationship("Blog", backref="blog")
    user = db.relationship("User", backref="use")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
