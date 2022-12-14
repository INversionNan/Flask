from flask import Flask
from flask_wtf import FlaskForm
from wtforms.validators import Length
from wtforms import SubmitField, StringField, TextAreaField


class ChangeUserList(FlaskForm):
    # realname = StringField('Real Name', validators=[Length(0, 100)])
    name = StringField('Real Name', validators=[Length(0, 100)])
    location = StringField('User Address', validators=[Length(0.100)])
    information = TextAreaField('User information')
    submit = SubmitField('Change user list')
