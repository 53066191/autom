# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/17/017 16:58
@desc:
"""
from flask import request, jsonify

from model import ProjectModel, Interface, TestCase
from . import api


@api.route("/get_model_by_project")
def _get_model_by_project():
    project_id = request.args.get('project_id', '01', type=str)
    result = [(row.id, row.name) for row in ProjectModel.query.filter_by(project_id=project_id).all()]
    return jsonify(result)


@api.route("/get_interface_by_project")
def _get_interface_by_project():
    project_id = request.args.get('project_id', '01', type=str)
    result = []
    for model_row in ProjectModel.query.filter_by(project_id=project_id).all():
        for interface_row in Interface.query.filter_by(model_id=model_row.id):
            result.append((interface_row.id, interface_row.uri))
    return jsonify(result)
