#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 蜜罐主机状态表
from conf.db import Base

from sqlalchemy import Column, String, TIMESTAMP, UniqueConstraint


class host(Base):
    __tablename__ = 'Host'

    id = Column(String(50), primary_key=True)
    last_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), nullable=False)
    ip = Column(String(50), nullable=False)
    status = Column(String(10), nullable=False)

    __table_args__ = (
        # 设置联合唯一索引
        UniqueConstraint('hostname', 'ip', name='uix_hostname_ip'),
        # 设置联合索引
        # Index('uix_hostname_ip', 'hostname', 'ip'),
    )


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    init_db()
    print('create Host table')

"""
CREATE TABLE `Host` (
	id VARCHAR(50) NOT NULL,
	last_time TIMESTAMP NOT NULL,
	hostname VARCHAR(50) NOT NULL,
	ip VARCHAR(50) NOT NULL,
	status VARCHAR(10) NOT NULL,
	PRIMARY KEY (id),
	CONSTRAINT uix_hostname_ip UNIQUE (hostname, ip)
)
"""