#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import render_template
import json
from controller.base import BaseClass
from database.mysql_db import DB,db
from module.user import User
import sys
reload(sys) 
sys.setdefaultencoding('utf8')
class MysqlClass(BaseClass):
	"""docstring for IndexClass"""
	def __init__(self):
		super(BaseClass,self).__init__()
	def create_function(self):
		return ''
		# db.create_all()
		# super(self).__init__()
	# def create_function(self):
	# 	sql = """CREATE TABLE EMPLOYEE (
	#          FIRST_NAME  CHAR(20) NOT NULL,
	#          LAST_NAME  CHAR(20),
	#          AGE INT,  
	#          SEX CHAR(1),
	#          INCOME FLOAT )"""
	# 	DB.execute(sql)
	def index_function(self):
		
		# sql = """
		# 	create table py_dept(
		# 		id int primary key auto_increment,
		# 		name varchar(50),
		# 		addtime timestamp NULL default CURRENT_TIMESTAMP,
		# 		description varchar(500)
		# 	)
		# """

		# sql = """
		# 	create table py_user(
		# 		id int primary key auto_increment,
		# 		name varchar(50) not null,
		# 		sex varchar(2) default'男' check(sex='男' or sex='女'),
		# 		age int,
		# 		address varchar(500),
		# 		email varchar(100),
		# 		addtime timestamp NULL default CURRENT_TIMESTAMP,
		# 		dept_id int,
		# 		foreign key(dept_id) references py_dept(`id`)
		# 	)ENGINE=InnoDB DEFAULT CHARSET=utf8;
		# """
		# DB.execute(sql)
		# cursor.execute("SELECT VERSION()")
		DB.execute("show tables;")
		results = DB.fetchall()
		return json.dumps(results)
		# conn = MySQLdb.connect(host='172.17.0.10', port=3306, user='root', passwd='root', db='mysql', charset='utf8')
		# conn = MySQLdb.connect(host='localhost', port=3306, user='root', passwd='root', db='mysql', charset='utf8',unix_socket='/var/run/mysqld/mysqld.sock')
		# db = MySQLdb.connect("localhost", "root", "root", "mysql", charset='utf8' )
		return '33333'
	
	def add_function(self):
		for x in xrange(30,50):
			me = User('admin'+str(x), 'admin'+str(x)+'@example.com')
			db.session.add(me)
			db.session.commit()
		return ''
	def del_function(self):
		db.session.delete(me)
		db.session.commit()
	def list_function(self):
		data = User.query.all()
		string = ''
		for user in data:
			string = string + str(user.id) + user.username + user. email + "<br />"
		return string
		return json.dumps(data)