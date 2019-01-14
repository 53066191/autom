# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/17/017 17:07
@desc:
"""
from flask import request, jsonify

from app import db
from model import Interface
from . import api


@api.route("/interface/add", methods=["post"])
def add_interface():

    model_id = request.json.get("model_id")
    name = request.json.get("name")
    methods = request.json.get("methods")
    uri = request.json.get("uri")
    desc = request.json.get("desc")
    interface_data = Interface(model_id=model_id, name=name, methods=methods, uri=uri, desc=desc)
    try:
        db.session.add(interface_data)
        return jsonify({"code": 0, "message": "sucess"})
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 1, 'message': '添加失败，原因:%s！' % e, })


@api.route("/get_project/interface/<id>", methods=['get'])
def get_project_by_interface(id):
    project_id = Interface.query.filter_by(id=id).project_id
    return
