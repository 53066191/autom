# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 17:23
@desc:
"""
from flask_ckeditor import CKEditorField
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, HiddenField, IntegerField
from wtforms.validators import DataRequired, Length

from model import Project


class TestCaseForm(FlaskForm):
    project_id = SelectField("项目名", validators=[DataRequired()], id='select_project')
    name = StringField("用例名", validators=[DataRequired(), Length(1, 256)])
    desc = TextAreaField("用例描述")
    submit = SubmitField("提交")


class TestStepForm(FlaskForm):
    interface_id = SelectField("接口uri",validators=[DataRequired()], id='select_interface')
    testcase_id = HiddenField()
    index = IntegerField("序号")
    desc = TextAreaField("步骤描述")
    datas = StringField("数据")
    code = CKEditorField("代码")
    submit = SubmitField("提交")

