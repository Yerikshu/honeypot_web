#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/28/20
# @Time     : 10:11 AM
# @Purpose  : redis配置文件


import redis


"""pool_activate = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=5, max_connections=10, password=)"""
pool_activate = redis.BlockingConnectionPool(host='localhost', port=6379, decode_responses=True, db=5, max_connections=10)
r_activate = redis.Redis(connection_pool=pool_activate)


""" pool_deactivate = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=6, max_connections=10, password=)"""
pool_deactivate = redis.BlockingConnectionPool(host='localhost', port=6379, decode_responses=True, db=6, max_connections=10)
r_deactivate = redis.Redis(connection_pool=pool_deactivate)


