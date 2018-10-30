#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import jsonify, request
import json
import time
import datetime
from database.redis_db import DB
from controller.base import BaseClass

class RedisClass(BaseClass):
	"""docstring for RedisClass"""
	def __init__(self):
		# pass
		super(BaseClass,self).__init__()
	def index_function(self):
		# print(self.gettime())
		# for x in xrange(1,1000):
		# 	DB.set('names'+str(x), 'name'+str(x))
		# # DB.set('ages','11111111111111111111')
		# return DB.get('ages')
		# return '232322'
		return json.dumps(DB.keys('*'))
		# return 'ddd'
	def set_function(self):
		# 获取 application/json
		jsdata = request.get_json()
		if not jsdata :
			jsdata = request.get_data()
		print(json.dumps(jsdata))
		DB.set(jsdata['key'],jsdata['content'])
		return DB.get(jsdata['key'])
		# DB.set()