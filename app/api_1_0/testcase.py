# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/19/019 10:15
@desc:
"""
from flask import request, jsonify
from flask_login import login_required

from app import db
from app.api_1_0 import api
from model import TestCase, TestCaseStep


@api.route("/testcase/add", methods=["post"])
@login_required
def add_testcase():
    project_id = request.json.get("project_id")
    name = request.json.get("name")
    desc = request.json.get("desc")
    testcase_data = TestCase(name=name,desc=desc, project_id=project_id)
    try:
        db.session.add(testcase_data)
        return jsonify({"code": 0, "message": "sucess"})
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 1, 'message': '添加失败，原因:%s！' % e, })

@api.route("/testcase/<case_id>/step/add", methods=["post"])
@login_required
def add_testcase_step(case_id):
    index = request.json.get("index")
    steps = TestCaseStep.query.filter_by(testcase_id=case_id).all()
    for step in steps:
        if int(index) == step.index:
            return jsonify({'code': 1, 'message': '添加失败，原因:%s序号已经存在！' % index})

    desc = request.json.get("desc")
    interface_id = request.json.get("interface_id")
    data = request.json.get("data")
    code = request.json.get("code")
    test_step = TestCaseStep(testcase_id=case_id, index=index, desc=desc, interface_id=interface_id, data=data, code=code)
    try:
        db.session.add(test_step)
        return jsonify({"code": 0, "message": "sucess"})
    except Exception as e:
        db.session.rollback()
        return jsonify({'code': 1, 'message': '添加失败，原因:%s！' % e, })