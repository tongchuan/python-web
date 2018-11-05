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
	def setex_function(self):
		# set(name, value, ex=None, px=None, nx=False, xx=False)
		# ex，过期时间（秒）
		# px，过期时间（毫秒）
		# nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
		# xx，如果设置为True，则只有name存在时，当前set操作才执行'''
		DB.set('setex','setex',ex=10)
		return DB.get('setex')
	def mset_function(self):
		DB.mset(name1='zhang',name2='tongchuan',ex=10)
		return json.dumps(DB.mget('name1','name2'))