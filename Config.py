import logging
from redis import StrictRedis


class Config(object):
    '''项目的配置'''
    DEBUG = True

    SECRET_KEY = '46vwHa33g6CHeVppQz9y4Nk7IG+uMPcm4YyB9ijHRlh0mwltAFdu6ZmMB9lbY907'

    # 为mysql添加配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    SESSION_TYPE = 'redis'

    SESSION_USE_SIGNER = True
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_PERMANENT = False

    PERMANENT_SESSION_LIFEIME = 86400 * 2

    LOG_LEVEL = logging.DEBUG

class DevelopementConfig(Config):
    # 开发环境下
    DEBUG = True

class ProductionConfig(Config):
    # 生产环境下
    DEBUG = False
    LOG_LEVEL = logging.WARNING

class TestingConfig(Config):
    # 单元测验
    DEBUG = True
    TESTING = True

config = {
    'development':DevelopementConfig,
    'production':ProductionConfig,
    'testing':TestingConfig
}