#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 蜜罐日志未经过白名单表
from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean, DateTime, text, func

from conf.db import Base, engine, DBSession


class Attack_log(Base):
    __tablename__ = 'attack_log'

    id = Column(Integer, autoincrement=True, primary_key=True)
    dst_host = Column(String(50), server_default='')
    dst_port = Column(Integer, server_default=text("0"))
    honeycred = Column(Boolean, server_default=text("False"))
    local_time = Column(DateTime, server_default=func.now())
    update_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), server_default='')
    password = Column(String(50), server_default='')
    path = Column(Unicode(50), server_default='')
    skin = Column(String(50), nullable=True)
    useragent = Column(Unicode(250), server_default='')
    username = Column(String(50), server_default='')
    session = Column(String(50), server_default='')
    localversion = Column(String(50), server_default='')
    remoteversion = Column(String(50), server_default='')
    df = Column(String(30), server_default='')
    idid = Column(String(20), server_default='')
    inin = Column(String(50), server_default='')
    lenlen = Column(String(50), server_default='')
    mac = Column(String(60), server_default='')
    outout = Column(String(50), server_default='')
    prec = Column(String(20), server_default='')
    proto = Column(String(10), server_default='')
    res = Column(String(20), server_default='')
    syn = Column(String(10), server_default='')
    tos = Column(String(20), server_default='')
    ttl = Column(String(20), server_default='')
    urgp = Column(String(5), server_default='')
    window = Column(String(50), server_default='')
    logtype = Column(String(50), server_default='')
    node_id = Column(String(30), server_default='')
    src_host = Column(String(50), server_default='')
    src_port = Column(Integer, server_default=text("0"))
    repo = Column(String(150), server_default='')
    ntp_cmd = Column(String(150), server_default='')
    args = Column(String(150), server_default='')
    cmd = Column(String(150), server_default='')
    banner_id = Column(String(30), server_default='')
    data = Column(String(150), server_default='')
    function = Column(String(150), server_default='')
    vnc_client_response = Column(String(150), server_default='')
    vnc_password = Column(String(50), server_default='')
    vnc_server_challenge = Column(String(150), server_default='')
    inputs = Column(String(150), server_default='')
    domain = Column(String(150), server_default='')
    headers_call_id = Column(String(150), server_default='')
    headers_content_length = Column(String(150), server_default='')
    headers_cseq = Column(String(150), server_default='')
    headers_from = Column(String(150), server_default='')
    headers_to = Column(String(150), server_default='')
    headers_via = Column(String(150), server_default='')
    community_string = Column(String(50), server_default='')
    requests = Column(String(50), server_default='')
    urg = Column(String(50), server_default='')
    psh = Column(String(50), server_default='')
    fin = Column(String(50), server_default='')
    appname = Column(String(150), server_default='')
    cltintname = Column(String(150), server_default='')
    database = Column(String(50), server_default='')
    language = Column(String(50), server_default='')
    servername = Column(String(50), server_default='')
    domainname = Column(String(50), server_default='')


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    drop_db()
    print('Drop attack_log table')

    init_db()
    print('create attack_log table')

# SQL:
# CREATE TABLE attack_log (
# 	id INTEGER NOT NULL AUTO_INCREMENT,
# 	dst_host VARCHAR(50) DEFAULT '',
# 	dst_port INTEGER DEFAULT 0,
# 	honeycred BOOL DEFAULT False,
# 	local_time DATETIME DEFAULT now(),
# 	update_time TIMESTAMP NOT NULL,
# 	hostname VARCHAR(50) DEFAULT '',
# 	password VARCHAR(50) DEFAULT '',
# 	path VARCHAR(50) DEFAULT '',
# 	skin VARCHAR(50),
# 	useragent VARCHAR(250) DEFAULT '',
# 	username VARCHAR(50) DEFAULT '',
# 	session VARCHAR(50) DEFAULT '',
# 	localversion VARCHAR(50) DEFAULT '',
# 	remoteversion VARCHAR(50) DEFAULT '',
# 	df VARCHAR(30) DEFAULT '',
# 	idid VARCHAR(20) DEFAULT '',
# 	inin VARCHAR(50) DEFAULT '',
# 	lenlen VARCHAR(50) DEFAULT '',
# 	mac VARCHAR(60) DEFAULT '',
# 	outout VARCHAR(50) DEFAULT '',
# 	prec VARCHAR(20) DEFAULT '',
# 	proto VARCHAR(10) DEFAULT '',
# 	res VARCHAR(20) DEFAULT '',
# 	syn VARCHAR(10) DEFAULT '',
# 	tos VARCHAR(20) DEFAULT '',
# 	ttl VARCHAR(20) DEFAULT '',
# 	urgp VARCHAR(5) DEFAULT '',
# 	`window` VARCHAR(50) DEFAULT '',
# 	logtype VARCHAR(50) DEFAULT '',
# 	node_id VARCHAR(30) DEFAULT '',
# 	src_host VARCHAR(50) DEFAULT '',
# 	src_port INTEGER DEFAULT 0,
# 	repo VARCHAR(150) DEFAULT '',
# 	ntp_cmd VARCHAR(150) DEFAULT '',
# 	args VARCHAR(150) DEFAULT '',
# 	cmd VARCHAR(150) DEFAULT '',
# 	banner_id VARCHAR(30) DEFAULT '',
# 	data VARCHAR(150) DEFAULT '',
# 	`function` VARCHAR(150) DEFAULT '',
# 	vnc_client_response VARCHAR(150) DEFAULT '',
# 	vnc_password VARCHAR(50) DEFAULT '',
# 	vnc_server_challenge VARCHAR(150) DEFAULT '',
# 	inputs VARCHAR(150) DEFAULT '',
# 	domain VARCHAR(150) DEFAULT '',
# 	headers_call_id VARCHAR(150) DEFAULT '',
# 	headers_content_length VARCHAR(150) DEFAULT '',
# 	headers_cseq VARCHAR(150) DEFAULT '',
# 	headers_from VARCHAR(150) DEFAULT '',
# 	headers_to VARCHAR(150) DEFAULT '',
# 	headers_via VARCHAR(150) DEFAULT '',
# 	community_string VARCHAR(50) DEFAULT '',
# 	requests VARCHAR(50) DEFAULT '',
# 	urg VARCHAR(50) DEFAULT '',
# 	psh VARCHAR(50) DEFAULT '',
# 	fin VARCHAR(50) DEFAULT '',
# 	appname VARCHAR(150) DEFAULT '',
# 	cltintname VARCHAR(150) DEFAULT '',
# 	`database` VARCHAR(50) DEFAULT '',
# 	language VARCHAR(50) DEFAULT '',
# 	servername VARCHAR(50) DEFAULT '',
# 	domainname VARCHAR(50) DEFAULT '',
# 	PRIMARY KEY (id),
# 	CHECK (honeycred IN (0, 1))
# )

