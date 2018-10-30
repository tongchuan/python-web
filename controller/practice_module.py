#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
from controller.base import BaseClass
class PracticeClass(BaseClass):
	"""docstring for practiceClass"""
	def __init__(self):
		super(BaseClass, self).__init__()

	def index_function(self):
		return 'index'
	def l16_function(self):
		
		str1 = "datetime.date.today().strftime('%d/%m/%Y') : " + \
						datetime.date.today().strftime('%d/%m/%Y') + "<br />" + \
						"datetime.date(1941, 1, 5).strftime('%d/%m/%Y') : " + \
						datetime.date(1941, 1, 5).strftime('%d/%m/%Y') + "<br />" + \
						"(datetime.date(1941,1,5) + datetime.timedelta(days=1)).strftime('%d/%m/%Y') : " + \
						(datetime.date(1941,1,5) + datetime.timedelta(days=1)).strftime('%d/%m/%Y') + "<br />" + \
						"datetime.date(1941,1,5).replace(year=datetime.date(1941,1,5).year + 1).strftime('%d/%m/%Y') : " + \
						datetime.date(1941,1,5).replace(year=datetime.date(1941,1,5).year + 1).strftime('%d/%m/%Y')
		return '%s' % str1
		return 'a'
