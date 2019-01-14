# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/17/017 15:35
@desc:
"""
from flask import request, render_template, jsonify, current_app, redirect, url_for
from flask_login import login_required

from app.project.interfaceforms import InterfaceForm
from model import Project, ProjectModel, Interface
from . import project


@project.route("/interface/show", methods=["get"])
@login_required
def interface_show():
    interfaces = Interface.query.order_by(Interface.timestamp.desc()).all()
    form = InterfaceForm()
    form.project_id.choices = [(row.id, row.name) for row in Project.query.all()]
    form.model_id.choices = [(row.id, row.name) for row in ProjectModel.query.all()]
    page = request.args.get('page', 1, type=int)
    pagination = Interface.query.order_by(Interface.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False
    )

    return render_template('interface/show.html', form=form, pagination=pagination,interfaces=interfaces)

