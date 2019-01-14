# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 11:31
@desc:
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class AddTestCaseForm(FlaskForm):
    pass


class ProjectForm(FlaskForm):
    name = StringField("项目名", validators=[DataRequired(), Length(1, 64)])
    desc = TextAreaField("项目描述")
    submit = SubmitField("提交")
