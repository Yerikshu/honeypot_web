#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/21/20
# @Time     : 10:31 PM
# @Purpose  : 主机状态处理
import datetime
import hashlib

from controller.dto.host import Host

host = Host()


def hoststatus(lasttime, hostname, ip, status):
    # 计算host表主键id
    idmd5 = hashlib.md5()
    idmd5.update(hostname + ip)
    id = idmd5.hexdigest()
    return host.insert_data(id, lasttime, hostname, ip, status)


def hostonline():
    # 查询所有在线主机
    onlines = host.select_data()
    if onlines:
        for h in onlines:
            # 用当前时间减去主机最后在线时间
            time_value = datetime.datetime.now() - h.last_time
            # 时间间隔大于20秒就认为机器离线，更新数据库主机状态
            # 后续另外写crontab完成状态信息通知功能
            if time_value.seconds > 50:
                hoststatus(
                    h.last_time.strftime("%Y-%m-%d %H:%M:%S"), h.hostname,
                    h.ip, "offline")
            else:
                pass
    else:
        return False

    # [{'id': u'c68ed14008b0f10c1dfe874efeb435e6', 'last_time': '2018-10-30 12:20:22'},
    # {'id': u'e1e42e7f935d68b68d8f2c34de97cc3e', 'last_time': '2018-10-30 12:10:22'}]


def getHoststatus():
    hosts = host.select_allhost()
    if hosts:
        hostlists = []
        for h in hosts:
            hostdict = {
                "date": h.last_time.strftime("%Y-%m-%d %H:%M:%S"),
                "name": h.hostname,
                "address": h.ip,
                "tag": h.status
            }
            hostlists.append(hostdict)
        results = {"list": hostlists}
        return results