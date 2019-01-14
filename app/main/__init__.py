# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:05
@desc:
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views

