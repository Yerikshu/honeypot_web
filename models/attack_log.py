#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 蜜罐日志未经过白名单表

from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean

from conf.db import Base, engine


class attack_log(Base):
    __tablename__ = 'attack_log'

    id = Column(Integer, autoincrement=True, primary_key=True)
    dst_host = Column(String(50), nullable=False)
    dst_port = Column(Integer, nullable=False)
    honeycred = Column(Boolean, nullable=True)
    local_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), nullable=True)
    password = Column(String(50), nullable=True)
    path = Column(Unicode(50), nullable=True)
    skin = Column(String(50), nullable=True)
    useragent = Column(Unicode(250), nullable=True)
    username = Column(String(50), nullable=True)
    session = Column(String(50), nullable=True)
    localversion = Column(String(50), nullable=True)
    remoteversion = Column(String(50), nullable=True)
    df = Column(String(30), nullable=True)
    idid = Column(String(20), nullable=True)
    inin = Column(String(50), nullable=True)
    lenlen = Column(String(50), nullable=True)
    mac = Column(String(60), nullable=True)
    outout = Column(String(50), nullable=True)
    prec = Column(String(20), nullable=True)
    proto = Column(String(10), nullable=True)
    res = Column(String(20), nullable=True)
    syn = Column(String(10), nullable=True)
    tos = Column(String(20), nullable=True)
    ttl = Column(String(20), nullable=True)
    urgp = Column(String(5), nullable=True)
    window = Column(String(50), nullable=True)
    logtype = Column(String(50), nullable=True)
    node_id = Column(String(30), nullable=False)
    src_host = Column(String(50), nullable=True)
    src_port = Column(Integer, nullable=False)
    white = Column(Integer, nullable=False)
    # 扩表
    repo = Column(String(150), nullable=True)
    ntp_cmd = Column(String(150), nullable=True)
    args = Column(String(150), nullable=True)
    cmd = Column(String(150), nullable=True)
    banner_id = Column(String(30), nullable=True)
    data = Column(String(150), nullable=True)
    function = Column(String(150), nullable=True)
    vnc_client_response = Column(String(150), nullable=True)
    vnc_password = Column(String(50), nullable=True)
    vnc_server_challenge = Column(String(150), nullable=True)
    inputs = Column(String(150), nullable=True)
    domain = Column(String(150), nullable=True)
    headers_call_id = Column(String(150), nullable=True)
    headers_content_length = Column(String(150), nullable=True)
    headers_cseq = Column(String(150), nullable=True)
    headers_from = Column(String(150), nullable=True)
    headers_to = Column(String(150), nullable=True)
    headers_via = Column(String(150), nullable=True)
    community_string = Column(String(50), nullable=True)
    requests = Column(String(50), nullable=True)
    urg = Column(String(50), nullable=True)
    psh = Column(String(50), nullable=True)
    fin = Column(String(50), nullable=True)
    appname = Column(String(150), nullable=True)
    cltintname = Column(String(150), nullable=True)
    database = Column(String(50), nullable=True)
    language = Column(String(50), nullable=True)
    servername = Column(String(50), nullable=True)
    domainname = Column(String(50), nullable=True)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
