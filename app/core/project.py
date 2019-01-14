# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/17/017 15:46
@desc:
"""

from model import Project


def get_all_project():
    projects = Project.query.order_by(Project.id.desc).all()