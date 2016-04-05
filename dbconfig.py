__author__ = 'leimin'

# -*- coding: utf8 -*-

import os


basedir = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir,'test.db')
SQLALCHEMY_DATABASE_URI=r'sqlite:///D:/MyBlog/test.db'
#print SQLALCHEMY_DATABASE_URI
SQLALCHEMY_COMMIT_ON_TEARDOWN = True