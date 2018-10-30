#!/usr/bin/python
# -*- coding: UTF-8 -*-

import redis

pool= redis.ConnectionPool(host='localhost',port=6379,password='123',decode_responses=True)
# pool= redis.ConnectionPool(host='localhost',port=6379,decode_responses=True)
DB=redis.Redis(connection_pool=pool)
# DB = redis.StrictRedis(host='localhost',port=6379,password='123',decode_responses=True,db=0)