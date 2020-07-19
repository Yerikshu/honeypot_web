#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 白名单表
from sqlalchemy import Column, String

from conf.db import Base, engine


class white_list(Base):
    __tablename__ = 'white_list'
    source_port = Column(String(10), nullable=False, primary_key=True)
    source_ip = Column(String(20), nullable=False, primary_key=True)
    dst_port = Column(String(10), nullable=False, primary_key=True)
    dst_ip = Column(String(20), nullable=False, primary_key=True)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
