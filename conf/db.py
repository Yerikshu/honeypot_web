#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 数据库配置文件
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 数据库配置
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_USER = os.environ.get("DB_USER", "honeypot")
DB_PWD = os.environ.get("DB_PWD", "123456")
DB_PORT = os.environ.get("DB_PORT", "45212")
DB_NAME = os.environ.get("DB_NAME", 'honeyAnlyse')

# 创建对象基类
Base = declarative_base()

# 初始化数据库连接
engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %
                       (DB_USER, DB_PWD, DB_HOST, DB_PORT, DB_NAME),
                       encoding='utf-8', echo=True,
                       pool_size=100, pool_pre_ping=True, pool_recycle=3600)

# 创建DBsession类型
Session = sessionmaker(bind=engine)
DBSession = Session()
