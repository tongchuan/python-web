#!/usr/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, url_for,abort, render_template,request, send_from_directory, make_response
from flask_cors import CORS
import os
import json
import sys
reload(sys) 
sys.setdefaultencoding('utf8')

from config import config

app = Flask(__name__,static_folder=config['static'])
# app.add_url_rule('/favicon.ico', redirect=url_for(config['static'], filename='favicon.ico'))
CORS(app, resources=r'/*', supports_credentials=True)


@app.before_request
def before_request():
	if str(request.method).upper() == 'OPTIONS' :
		return ''
	# print(request.data)
	# print(request.method)
	# pass
    # ip = request.remote_addr
    # url = request.url
    # print(dir(request))
    # # ['__class__', '__delattr__', '__dict__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_cached_json', '_get_data_for_json', '_get_file_stream', '_get_stream_for_parsing', '_load_form_data', '_parse_content_type', 'accept_charsets', 'accept_encodings', 'accept_languages', 'accept_mimetypes', 'access_route', 'application', 'args', 'authorization', 'base_url', 'blueprint', 'cache_control', 'charset', 'close', 'content_encoding', 'content_length', 'content_md5', 'content_type', 'cookies', 'data', 'date', 'dict_storage_class', 'disable_data_descriptor', 'encoding_errors', 'endpoint', 'environ', 'files', 'form', 'form_data_parser_class', 'from_values', 'full_path', 'get_data', 'get_json', 'headers', 'host', 'host_url', 'if_match', 'if_modified_since', 'if_none_match', 'if_range', 'if_unmodified_since', 'input_stream', 'is_json', 'is_multiprocess', 'is_multithread', 'is_run_once', 'is_secure', 'is_xhr', 'json', 'list_storage_class', 'make_form_data_parser', 'max_content_length', 'max_form_memory_size', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 'on_json_loading_failed', 'parameter_storage_class', 'path', 'pragma', 'query_string', 'range', 'referrer', 'remote_addr', 'remote_user', 'routing_exception', 'scheme', 'script_root', 'shallow', 'stream', 'trusted_hosts', 'url', 'url_charset', 'url_root', 'url_rule', 'user_agent', 'values', 'view_args', 'want_form_data_parsed']
    # print ip,
    # print url
@app.after_request
def af_request(response):
	print("after_request")
	response = make_response(response)
	response.headers['Access-Control-Allow-Origin'] = '*'
	response.headers['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PUT,DELETE'
	response.headers['Access-Control-Allow-Headers'] = 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type'
	return response

	# # resp = make_response(resp)
	# resp.headers['Access-Control-Allow-Origin']='*'
	# resp.headers['Access-Control-Allow-Methods'] = 'POST,GET,OPTIONS,PUT,DELETE'
	# resp.headers['Access-Control-Allow-Headers'] = 'DNT,X-CustomHeader,Keep-Alive,User-Agent,X-Requested-With,If-Modified-Since,Cache-Control,Content-Type'
	# return resp


def controller(module, func):
	# try:
		PACKAGE = __import__(config['package']+'.'+module+'_'+config['moduleSuffix'])
		MODULE = getattr(PACKAGE,module+'_'+config['moduleSuffix'])
		CLASS = getattr(MODULE,str(module).capitalize()+str(config['classSuffix']).capitalize())
		OBJECT = CLASS()
		FUNCTION = getattr(OBJECT,func+''+config['functionSuffix'])
		return FUNCTION()
	# except BaseException:
	# 	return error_function('地址错误')
	

@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<module>/<func>', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE','OPTIONS'])
def default(module,func):
	# print(func)
	return controller(module, func)

@app.route('/<module>', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE','OPTIONS'])
def main(module):
	return controller(module,config['function'])


@app.route('/', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE','OPTIONS'])
def index():
	return render_template('index.html')
	return controller(config['module'],config['function'])



def error_function(error):
	return render_template('error.html',error=error)

@app.errorhandler(404)
def page_not_found(error):
	# print(error)
	return '404'

@app.errorhandler(500)
def page_not_found(error):
	# print error
	return render_template('error.html',error=error)
	# return error


@app.route('/method', methods=['GET', 'HEAD', 'POST', 'PUT', 'DELETE','OPTIONS'])
def method():
	return 'method'
def login():
	return 'login'

@app.route('/login', methods=['POST', 'GET'])
def login():
	return 'login'

@app.route('/temp')
def temp():
	return render_template('index.html',name=__name__)
if __name__=='__main__':
	from database.mysql_db import connMysql
	connMysql(app)
	app.debug = True
	app.run(host='0.0.0.0',port=8888,debug=True)

