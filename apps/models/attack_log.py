#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 蜜罐日志未经过白名单表
from datetime import datetime

from sqlalchemy import Column, String, Integer, Unicode, TIMESTAMP, Boolean, DateTime, text

from conf.db import Base, engine


class attack_log(Base):
    __tablename__ = 'attack_log'

    id = Column(Integer, autoincrement=True, primary_key=True)
    dst_host = Column(String(50), server_default='')
    dst_port = Column(Integer, server_default=text("0"))
    honeycred = Column(Boolean, server_default=False)
    local_time = Column(DateTime, nullable=False, server_default=func.now())
    update_time = Column(TIMESTAMP, nullable=False)
    hostname = Column(String(50), nullable=True, server_default='')
    password = Column(String(50), nullable=True, server_default='')
    path = Column(Unicode(50), nullable=True, server_default='')
    skin = Column(String(50), nullable=True)
    useragent = Column(Unicode(250), nullable=True, server_default='')
    username = Column(String(50), nullable=True, server_default='')
    session = Column(String(50), nullable=True, session='')
    localversion = Column(String(50), nullable=True, server_default='')
    remoteversion = Column(String(50), nullable=True, server_default='')
    df = Column(String(30), nullable=True, server_default='')
    idid = Column(String(20), nullable=True, server_default='')
    inin = Column(String(50), nullable=True, server_default='')
    lenlen = Column(String(50), nullable=True, server_default='')
    mac = Column(String(60), nullable=True, server_default='')
    outout = Column(String(50), nullable=True, server_default='')
    prec = Column(String(20), nullable=True, server_default='')
    proto = Column(String(10), nullable=True, server_default='')
    res = Column(String(20), nullable=True, server_default='')
    syn = Column(String(10), nullable=True, server_default='')
    tos = Column(String(20), nullable=True, server_default='')
    ttl = Column(String(20), nullable=True, server_default='')
    urgp = Column(String(5), nullable=True, server_default='')
    window = Column(String(50), nullable=True, server_default='')
    logtype = Column(String(50), nullable=True, server_default='')
    node_id = Column(String(30), nullable=False, server_default='')
    src_host = Column(String(50), nullable=True, server_default='')
    src_port = Column(Integer, nullable=False, server_default=text("0"))
    repo = Column(String(150), nullable=True, server_default='')
    ntp_cmd = Column(String(150), nullable=True, server_default='')
    args = Column(String(150), nullable=True, server_default='')
    cmd = Column(String(150), nullable=True, server_default='')
    banner_id = Column(String(30), nullable=True, server_default='')
    data = Column(String(150), nullable=True, server_default='')
    function = Column(String(150), nullable=True, server_default='')
    vnc_client_response = Column(String(150), nullable=True, server_default='')
    vnc_password = Column(String(50), nullable=True, server_default='')
    vnc_server_challenge = Column(String(150), nullable=True, server_default='')
    inputs = Column(String(150), nullable=True, server_default='')
    domain = Column(String(150), nullable=True, server_default='')
    headers_call_id = Column(String(150), nullable=True, server_default='')
    headers_content_length = Column(String(150), nullable=True, server_default='')
    headers_cseq = Column(String(150), nullable=True, server_default='')
    headers_from = Column(String(150), nullable=True, server_default='')
    headers_to = Column(String(150), nullable=True, server_default='')
    headers_via = Column(String(150), nullable=True, server_default='')
    community_string = Column(String(50), nullable=True, server_default='')
    requests = Column(String(50), nullable=True, server_default='')
    urg = Column(String(50), nullable=True, server_default='')
    psh = Column(String(50), nullable=True, server_default='')
    fin = Column(String(50), nullable=True, server_default='')
    appname = Column(String(150), nullable=True, server_default='')
    cltintname = Column(String(150), nullable=True, server_default='')
    database = Column(String(50), nullable=True, server_default='')
    language = Column(String(50), nullable=True, server_default='')
    servername = Column(String(50), nullable=True, server_default='')
    domainname = Column(String(50), nullable=True, server_default='')


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)
