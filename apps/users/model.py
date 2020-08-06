#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 用户关系模型

from datetime import datetime

from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from sqlalchemy import Column, String, Integer, TIMESTAMP

from conf.db import Base, engine


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), nullable=False)
    password = Column(String(64), nullable=False)
    bussiness = Column(String(32), nullable=False)  # 区分管理员所属业务
    create_time = Column(TIMESTAMP, default=datetime.now)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


# model兼容性
PydanticUser = sqlalchemy_to_pydantic(User)

if __name__ == "__main__":
    drop_db()
    print('Drop user table')

    init_db()
    print('create user table')

# SQL
# CREATE TABLE user (
# 	id INTEGER NOT NULL AUTO_INCREMENT,
# 	username VARCHAR(50) NOT NULL,
# 	password VARCHAR(64) NOT NULL,
# 	bussiness VARCHAR(32) NOT NULL,
# 	create_time TIMESTAMP NULL,
# 	PRIMARY KEY (id)
# )
