#!/usr/bin/python
# -*- coding: UTF-8 -*-
from flask import jsonify, request
import json
import time
import datetime
from database.redis_db import DB

# import sys
# reload(sys) 
# sys.setdefaultencoding('utf8')

class UserClass(object):
	"""docstring for user"""
	def __init__(self):
		pass
		# super(self).__init__()
		# self.arg = arg
	def index_function(self):
		return 'user.indez3333x'

	def abc_function(self):
		# application/json
		# jsdata = json.loads(request.get_json())
		if request.method == "POST":
			jsdata = request.get_json()
			if not jsdata :
				jsdata = request.get_data()
			
			jsdata['num']=range(33)
			jsdata['ddd']="开始"
			return json.dumps(jsdata)
			print(json.dumps(jsdata))

			# jsdata['num']=range(33)
			# return json.dumps(jsdata)
		elif request.method == "GET":

			# request.form.get("key", type=str, default=None) 获取表单数据
			# request.args.get("key") 获取get请求参数
			# request.values.get("key") 获取所有参数
			# value = request.values.get("key") 
			# return value
			data = {'user.abc':'张彤川','age':999}
			data2 = json.dumps(data)
			text = json.loads(data2)
			# print(text)
			return json.dumps(data,sort_keys=True, indent=2, separators=(',', ': '))
		# return jsonify(data)
		'''
			request = [
			    "__class__",
			    "__delattr__",
			    "__dict__",
			    "__doc__",
			    "__enter__",
			    "__exit__",
			    "__format__",
			    "__getattribute__",
			    "__hash__",
			    "__init__",
			    "__module__",
			    "__new__",
			    "__reduce__",
			    "__reduce_ex__",
			    "__repr__",
			    "__setattr__",
			    "__sizeof__",
			    "__str__",
			    "__subclasshook__",
			    "__weakref__",
			    "_cached_data",
			    "_cached_json",
			    "_get_data_for_json",
			    "_get_file_stream",
			    "_get_stream_for_parsing",
			    "_load_form_data",
			    "_parse_content_type",
			    "_parsed_content_type",
			    "accept_charsets",
			    "accept_encodings",
			    "accept_languages",
			    "accept_mimetypes",
			    "access_route",
			    "application",
			    "args",
			    "authorization",
			    "base_url",
			    "blueprint",
			    "cache_control",
			    "charset",
			    "close",
			    "content_encoding",
			    "content_length",
			    "content_md5",
			    "content_type",
			    "cookies",
			    "data",
			    "date",
			    "dict_storage_class",
			    "disable_data_descriptor",
			    "encoding_errors",
			    "endpoint",
			    "environ",
			    "files",
			    "form",
			    "form_data_parser_class",
			    "from_values",
			    "full_path",
			    "get_data",
			    "get_json",
			    "headers",
			    "host",
			    "host_url",
			    "if_match",
			    "if_modified_since",
			    "if_none_match",
			    "if_range",
			    "if_unmodified_since",
			    "input_stream",
			    "is_json",
			    "is_multiprocess",
			    "is_multithread",
			    "is_run_once",
			    "is_secure",
			    "is_xhr",
			    "json",
			    "list_storage_class",
			    "make_form_data_parser",
			    "max_content_length",
			    "max_form_memory_size",
			    "max_forwards",
			    "method",
			    "mimetype",
			    "mimetype_params",
			    "on_json_loading_failed",
			    "parameter_storage_class",
			    "path",
			    "pragma",
			    "query_string",
			    "range",
			    "referrer",
			    "remote_addr",
			    "remote_user",
			    "routing_exception",
			    "scheme",
			    "script_root",
			    "shallow",
			    "stream",
			    "trusted_hosts",
			    "url",
			    "url_charset",
			    "url_root",
			    "url_rule",
			    "user_agent",
			    "values",
			    "view_args",
			    "want_form_data_parsed"
			]
		'''
	def ztc_function(self):
		data = {
			'name': True,
			'age':1000,
			'Number': 999999999,
			'list': [1,2,3,4,5],
			'message': 'abc',
			'tup': ('abc','cde'),
			'dict': {'a':'a','b':'b'},
			'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		}
		# data = '{"success":true,"message":"success","data":[{"id":"G001ZM000000000BTNSAVE00000000000001","code":"save","name":"保存","url":"/note/freectr/item/save","icon":null,"needparams":null,"afteraction":null,"beforeaction":null,"urltype":"local"},{"id":"G001ZM000000000BTNEDIT00000000000001","code":"edit","name":"编辑","url":null,"icon":null,"needparams":"1","afteraction":null,"beforeaction":null,"urltype":"local"},{"id":"G001ZM000000000BTNDEL000000000000001","code":"del","name":"删除","url":"/note/freectr/item/del","icon":null,"needparams":"1","afteraction":null,"beforeaction":null,"urltype":"local"}],"code":20000,"total":0}'
		# data = json.dumps(json.loads(data))
		return json.dumps(data);
	def get_function(self):
		return DB.get('name')
