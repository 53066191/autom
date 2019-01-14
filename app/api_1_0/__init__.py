# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/17/017 16:56
@desc:
"""

from flask import Blueprint

api = Blueprint("api", __name__)
from . import views, interface, testcase