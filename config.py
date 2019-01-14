# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:05
@desc:
"""

import os
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config():
    SECRET_KEY = "HARD TO GUESS"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = "smtp.sina.com"
    MAIL_PORT = 465
    MAIL_USERNAME = 'kiktech@sina.com'
    MAIL_PASSWORD = 'kiktech2016'
    MAIL_USE_SSL = True

    SQLALCHEMY_DATABASE_URI = '''sqlite:///''' + os.path.join(base_dir, 'data.sqlite')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    FLASKY_POSTS_PER_PAGE = 100


config = {
    'development': DevelopmentConfig,
    'production': ""
}
