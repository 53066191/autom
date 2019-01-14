# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/18/018 10:52
@desc:
"""
from flask import request, current_app, render_template
from flask_login import login_required

from app.project.testcaseforms import TestCaseForm, TestStepForm
from model import TestCase, Interface, Project, TestCaseStep
from . import project


@project.route("/testcase/show", methods=["get"])
@login_required
def testcase_show():
    testcases = TestCase.query.order_by(TestCase.timestamp.desc()).all()
    page = request.args.get('page', 1, type=int)
    pagination = Interface.query.order_by(Interface.timestamp.desc()).paginate(
        page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False
    )

    return render_template('testcase/show.html', pagination=pagination, testcases=testcases)


@project.route("/testcase/add", methods=["get"])
@login_required
def testcase_add():
    testcase_form = TestCaseForm()
    testcase_form.project_id.choices = [(row.id, row.name) for row in Project.query.all()]
    teststep_form = TestStepForm()
    teststep_form.interface_id.choices = [(row.id, row.name)
                                          for row in Interface.query.all()]
    return render_template("testcase/add.html", testcase_form=testcase_form, teststep_form=teststep_form)


@project.route("/testcase/edit/<id>", methods=["get"])
@login_required
def testcase_edit(id):
    testcase = TestCase.query.filter_by(id=id).first()
    testcase_form = TestCaseForm()
    testcase_form.project_id.choices = [(testcase.project_id, Project.query.filter_by(id=testcase.project_id).first().name)]
    testcase_form.name.data = testcase.name
    testcase_form.desc.data = testcase.desc
    teststep_form = TestStepForm()
    teststep_form.testcase_id.data = id
    teststep_form.interface_id.choices = [(row.id, row.uri) for row in Interface.query.all()]
    case_steps = TestCaseStep.query.filter_by(testcase_id=id).all()
    return render_template("testcase/edit.html", testcase_form=testcase_form, teststep_form=teststep_form, steps=case_steps)
