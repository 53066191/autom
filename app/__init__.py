# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:04
@desc:
"""

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import  LoginManager
from flask_mail import Mail
from flask_moment import Moment
from flask_pagedown import PageDown
from flask_sqlalchemy import SQLAlchemy

from config import Config, config

db = SQLAlchemy()
bootstrap = Bootstrap()
# nav = Nav()
mail = Mail()
moment = Moment()
ckeditor = CKEditor()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(env_config):
    app = Flask(__name__)
    app.config.from_object(config[env_config])
    config[env_config].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    from .main import main
    app.register_blueprint(main)

    from .auth import auth
    app.register_blueprint(auth)

    from .project import project
    app.register_blueprint(project)

    from .api_1_0 import api
    app.register_blueprint(api, url_prefix="/api/1.0")



    return app


