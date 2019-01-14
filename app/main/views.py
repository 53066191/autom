# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:24
@desc:
"""
from flask import render_template

from . import main

@main.route("/")
def index():
    return  render_template("main/index.html", user=None)


@main.route("/nav")
def nav():
    return render_template("menu.html", user=None)