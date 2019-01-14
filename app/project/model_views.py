# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/15/015 14:57
@desc:
"""
from flask import request, flash, redirect, url_for
from flask_login import login_required

from app import db
from model import ProjectModel
from . import project

@project.route("/model/show",methods=["post"])
@login_required
def model_show():

    id = request.form.get("id")
    project_model = ProjectModel(project_id=request.form.get("id"), name=request.form.get("name"), desc=request.form.get("desc"))
    db.session.add(project_model)
    flash("模块添加成功")
    return redirect(url_for("project.edit", id=id))

@project.route("/model/edit", methods=["get", "post"])
@login_required
def model_edit():
    return "a"

