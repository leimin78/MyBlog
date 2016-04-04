__author__ = 'leimin'

# -*- coding: utf8 -*-

import os


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.path.join(basedir,'test.db')
SQLALCHEMY_COMMIT_ON_TEARDOWN = True