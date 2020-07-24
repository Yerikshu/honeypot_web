#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/22/20
# @Time     : 3:51 PM
# @Purpose  : 日志记录
import os
import time
from loguru import logger

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# print(f"log basedir{basedir}")  # /xxx/python_code/FastAdmin/backend/app
# 定位到log日志文件
log_path = os.path.join(basedir, 'logs')

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_path_error = os.path.join(log_path, f'{time.strftime("%Y-%m-%d")}_error.log')


logger.add(log_path_error, format="{time} {level} {message}", filter="my_module", level="ERROR")