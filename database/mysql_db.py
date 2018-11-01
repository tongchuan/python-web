#!/usr/bin/python
# -*- coding: UTF-8 -*-


import MySQLdb
conn = MySQLdb.connect(host='172.17.0.3', port=3306, user='root', passwd='root', db='pythonDb', charset='utf8')
DB = conn.cursor()
# from flask_sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.sqlalchemy import SQLAlchemy
# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@172.17.0.3/pythonDb?charset=utf8'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
# db = SQLAlchemy(app)

# pip install MySQL-python
# pip install Flask-SQLAlchemy

db = None
def connMysql(app):
	global db
	app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:root@172.17.0.3/pythonDb?charset=utf8'
	app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
	db = SQLAlchemy(app)
