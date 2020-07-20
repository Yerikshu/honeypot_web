#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 用户关系模型

from datetime import datetime
from sqlalchemy import Column, String, Integer, TIMESTAMP

from conf.db import Base, engine


class user(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(32), nullable=False)
    bussiness = Column(String(32), nullable=False)  # 区分管理员所属业务
    create_time = Column(TIMESTAMP, default=datetime.now)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
