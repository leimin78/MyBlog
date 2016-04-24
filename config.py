__author__ = 'leimin'

# -*- coding: utf8 -*-

import os
import dbconfig
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <18898761417@139.com>'

    @staticmethod
    def init_app(app):
        pass

#研发环境
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.139.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = '18898761417@139.com'
    MAIL_PASSWORD = '**************'
    SQLALCHEMY_DATABASE_URI = dbconfig.SQLALCHEMY_DATABASE_URI

#测试环境
class TestingConfig(Config):
    Testing = True
    SQLALCHEMY_DATABASE_URI = dbconfig.SQLALCHEMY_DATABASE_URI_TEST

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = dbconfig.SQLALCHEMY_DATABASE_URI_PRODUCT


config = {
    'development': DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,
    'default' : DevelopmentConfig
}



