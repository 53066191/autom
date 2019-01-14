# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 11:30
@desc:
"""
from flask_login import login_required

from app import db
from app.project.modelforms import ModelForm
from app.project.projectforms import ProjectForm
from model import Project, ProjectModel
from . import project
from flask import render_template, url_for, redirect, request, current_app, flash

@project.route("/project/show", methods=['GET', 'POST'])
@login_required
def show():
    add_form = ProjectForm()
    project_datas =Project.query.all()
    page = request.args.get('page', 1, type=int)

    pagination = Project.query.order_by(Project.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False
    )

    if add_form.validate_on_submit():
        project_data = Project(name=add_form.name.data, desc=add_form.desc.data)
        db.session.add(project_data)
        return redirect(url_for("project.show"))

    return render_template("project/show.html", projects=project_datas, pagination=pagination, add_form=add_form)

@project.route("/project/edit/<id>", methods=['GET', 'POST'])
@login_required
def edit(id):
    project_data = Project.query.filter_by(id=id).first()
    form = ProjectForm()

    if form.validate_on_submit():
        project_data.desc = form.desc.data
        db.session.add(project_data)
        flash("修改成功")
        return redirect(url_for("project.show"))

    form.name.data = project_data.name
    form.desc.data = project_data.desc
    models = project_data.models.order_by(ProjectModel.timestamp.desc()).all()
    add_model_form = ModelForm()
    add_model_form.project_id = id

    return render_template("project/edit.html", form=form, models=models, model_form=add_model_form)
