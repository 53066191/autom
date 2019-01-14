# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:41
@desc:
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from model import User


class RegistrationForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField("用户名", validators=[DataRequired(), Length(1, 64)])
    password = PasswordField('密码',
                             validators=[DataRequired(), EqualTo('password2', message="passwords must match")])
    password2 = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('提交')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data):
            return ValidationError("该邮箱已经被使用")

    def validate_username(self, field):
        if User.query.filter_by(username=field.data):
            return ValidationError("该用户名已经被使用")


class LoginForm(FlaskForm):
    email = StringField("邮箱", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    rember_me = BooleanField('Keep me logged in')

    submit = SubmitField('提交')
