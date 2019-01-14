# encoding: utf-8
"""
@author: liuyun
@time: 2018/12/12/012 10:06
@desc:
"""

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db, login_manager
from model import User, Project, TestCase, Interface


def make_shell_context():
    return dict(app=app, db=db, User=User,Project=Project, TestCase=TestCase, Interface=Interface)


app = create_app('development')


manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
