# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:40
@desc:
"""

from flask import render_template, redirect, url_for, flash, request

from app import db
from app.auth.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required

from model import User
from .import auth


@auth.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.session.add(user)
        return redirect(url_for("main.index", user=user))

    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.verify_password(form.password.data):
            login_user(user, form.rember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash("用户名或者密码错误")
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash("you have logout!")
    return redirect(url_for("main.index"))




