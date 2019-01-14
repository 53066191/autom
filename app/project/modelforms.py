# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/15/015 11:27
@desc:
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class ModelForm(FlaskForm):
    project_id = IntegerField("项目id", validators=[DataRequired()])
    name = StringField("模块名", validators=[DataRequired(), Length(1, 64)])
    desc = TextAreaField("模块描述")
    submit = SubmitField("提交")
