from flask import Flask
from apps.model import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, ValidationError


class RegisterList(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(1, 100),
                                       Regexp('^\w*$', message="Username(email) must contain "
                                                               "alphanumeric characters "
                                                               "or underscores")],
                           render_kw={
                               'class': "layui-input",
                               "placeholder": "Username"
                           })
    email = StringField("Email", validators=[DataRequired(), Length(1, 100), Email()], render_kw={
        'class': "layui-input",
        "placeholder": "Email"
    })

    password = PasswordField("Password", validators=[DataRequired()],
                             render_kw={
                                 'class': "layui-input",
                                 "placeholder": "Password"
                             })
    confirmPassword = PasswordField("ConfirmPassword",
                                    validators=[DataRequired(), EqualTo('password', message="The two "
                                                                                            "passwords are different.")],
                                    render_kw={
                                        'class': "layui-input",
                                        "placeholder": "Confirm password"
                                    })

    submit = SubmitField("Register")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError("The email address %s has been registered." % field.data)

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError("The username %s has been registered." % field.data)


class LoginList(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()], render_kw={
        'class': "layui-input",
        "placeholder": "Email"
    })
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
        'class': "layui-input",
        "placeholder": "Password"
    })
    submit = SubmitField('Login')
