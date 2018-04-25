# import logging
#
# from flask import current_app
# from flask import session
from flask_script import Manager
# 这是数据库迁移
from flask_migrate import Migrate,MigrateCommand
from info import create_app,db,models

app = create_app('development')
manager = Manager(app)
Migrate(app,db)
# 将迁移命令添加到manager中
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':

    manager.run()
