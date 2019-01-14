# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 11:30
@desc:
"""

from flask import Blueprint
project = Blueprint("project", __name__)
from . import project_views, model_views, interface_views, testcase_views