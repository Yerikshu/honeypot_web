#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/28/20
# @Time     : 10:11 AM
# @Purpose  : redis配置文件


import redis


pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=5)
r = redis.Redis(connection_pool=pool)