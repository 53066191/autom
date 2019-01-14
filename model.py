# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:34
@desc:
"""
from flask import request
from flask_login import UserMixin
import libgravatar
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)

    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(128), unique=True, index=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    about_me = db.Column(db.Text())
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    avatar_hash = db.Column(db.String(32))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

        if self.email and self.avatar_hash is None:
            self.avatar_hash = libgravatar.md5_hash(self.email)

    def gravatar(self, size=100, default="identicon", rating='g'):
        use_ssl = True if request.is_secure else False
        if self.avatar_hash:
            url = 'https://secure.gravatar.com/avatar' if use_ssl else 'http://www.gravatar.com/avatar'
            return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
                url=url, hash=self.avatar_hash, size=size, default=default, rating=rating)
        return libgravatar.Gravatar(self.email).get_image(size=size, default=default, rating=rating, use_ssl=use_ssl)


    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)


class Project(db.Model):
    __tablename__ = "projects"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    desc = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    models = db.relationship('ProjectModel', backref='project',lazy='dynamic')
    testcases = db.relationship('TestCase', backref='project',lazy='dynamic')



class ProjectModel(db.Model):
    __tablename__ = "models"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    desc = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))


class TestCase(db.Model):
    __tablename__ = "testcases"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    desc = db.Column(db.Text())
    interface_id = db.Column(db.Integer, db.ForeignKey('interfaces.id'))
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'))
    steps = db.relationship('TestCaseStep', backref='testcase',lazy='dynamic')


class TestCaseStep(db.Model):
    __tablename__ = "steps"
    id = db.Column(db.Integer, primary_key=True)
    index = db.Column(db.Integer)
    desc = db.Column(db.String(500), unique=True)
    data = db.Column(db.Text())
    code = db.Column(db.Text())

    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    testcase_id = db.Column(db.Integer, db.ForeignKey('testcases.id'))
    interface_id = db.Column(db.Integer, db.ForeignKey('interfaces.id'))



class Interface(db.Model):
    __tablename__ = "interfaces"
    id = db.Column(db.Integer, primary_key=True)
    model_id = db.Column(db.Integer, db.ForeignKey('models.id'))
    name = db.Column(db.String(64), unique=True)
    methods = db.Column(db.String(64))
    uri = db.Column(db.String(128))
    desc = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow())
    testcases = db.relationship('TestCase', backref='interface',lazy='dynamic')



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))