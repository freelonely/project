# 所有代码的文件
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.ext.session import Session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import CSRFProtect
from flask.ext.wtf.csrf import generate_csrf
from redis import StrictRedis
from Config import config


db = SQLAlchemy()
# python3.6之后给变量加注释
redis_store = None # type:StrictRedis

def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):

    setup_log(config_name)
    app = Flask(__name__)
    '''加载配置'''
    app.config.from_object(config[config_name])
# 初始化
    db.init_app(app)

    global redis_store

    redis_store = StrictRedis(host=config[config_name].REDIS_HOST,port=config[config_name].REDIS_PORT,decode_responses=True)

    CSRFProtect(app)

    Session(app)

    from info.utils.common import do_index_class

    app.add_template_filter(do_index_class,'index_class')

    @app.after_request
    def after_request(response):
        csrf_token = generate_csrf()

        response.set_cookie('csrf_token',csrf_token)
        return response

    # 注册蓝图
    from info.modules.news import news_blu
    app.register_blueprint(news_blu)

    # 注册蓝图
    from info.modules.index import index_blu
    app.register_blueprint(index_blu)
    # 注册蓝图
    from info.modules.passport import passport_blu
    app.register_blueprint(passport_blu)
    return app
