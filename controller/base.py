#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import datetime
import json
class BaseClass(object):
	def __init__(self):
		print(self)
	def gettime(self):
		return time.time()
	def getDateTime(self):
		return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
	def getDateTime2(self):
		return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	def dumps(self, strjson):
		return json.dumps(strjson)
	# def loads(self, strjson):
	# 	return json.loads(strjson)