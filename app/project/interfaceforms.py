# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 17:23
@desc:
"""
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class InterfaceForm(FlaskForm):

    project_id = SelectField("项目名", validators=[DataRequired()], id='select_project')
    model_id = SelectField("模块名", validators=[DataRequired()], id='select_model')
    name = StringField("接口名")
    uri = StringField("接口uri")
    methods = SelectField("方法",choices=[('get','get'),('post','post'),('put','put')])
    desc = TextAreaField("接口描述")
    submit = SubmitField("提交")
