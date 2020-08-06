#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 白名单表,可以根据需要过滤源目端口以及ip
from sqlalchemy import Column, String, text

from conf.db import Base, engine


class White_list(Base):
    __tablename__ = 'white_list'
    src_port = Column(String(10), nullable=False, primary_key=True)
    src_ip = Column(String(20), nullable=False, primary_key=True)
    dst_port = Column(String(10), nullable=False, primary_key=True)
    dst_ip = Column(String(20), nullable=False, primary_key=True)
    # 激活判断默认是激活状态
    activate = Column(String(1), server_default=text("1"))


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    drop_db()
    print('Drop white_list table')

    init_db()
    print('create white_list table')

# SQL
# CREATE TABLE white_list (
# 	src_port VARCHAR(10) NOT NULL,
# 	src_ip VARCHAR(20) NOT NULL,
# 	dst_port VARCHAR(10) NOT NULL,
# 	dst_ip VARCHAR(20) NOT NULL,
# 	activate VARCHAR(1) DEFAULT 1,
# 	PRIMARY KEY (src_port, src_ip, dst_port, dst_ip)
# )
