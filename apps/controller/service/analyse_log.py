#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:10 PM
# @Purpose  : 解析客户端请求过来的日志


# TODO:这个还是需要优化一下,写得太蠢了
import datetime


def parserlog(jsonlog):
    # 接收客户端post过来的数据格式化
    if jsonlog:


        if dst_host:
            if src_host:
                # 判断攻击主机是否存在于白名单列表内
                if (src_host, dst_host, dst_port) in whiteiplist() or dst_host == src_host or src_host in whiteiplist_scanner() or (src_host, dst_port) in whiteiplist_4A():
                    white = 1
                    loginst.insert_white(dst_host, dst_port, honeycred, local_time, hostname, password, path, skin, \
                                             useragent, username, session, localversion, remoteversion, df, idid, inin,
                                             lenlen, mac, outout, \
                                             prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host,
                                             src_port, white, \
                                             # 扩表新增
                                             repo, ntp_cmd, args, cmd, banner_id, data, function, vnc_client_response,
                                             vnc_password, \
                                             vnc_server_challenge, inputs, domain, headers_call_id,
                                             headers_content_length, headers_cseq, \
                                             headers_from, headers_to, headers_via, community_string, requests, urg,
                                             psh, fin, \
                                             appname, cltintname, database, language, servername, domainname)
                    return True
                else:
                    white = 2
                    logbool = loginst.insert(dst_host, dst_port, honeycred, local_time, hostname, password, path, skin, \
                                             useragent, username, session, localversion, remoteversion, df, idid, inin,
                                             lenlen, mac, outout, \
                                             prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host,
                                             src_port, white, \
                                             # 扩表新增
                                             repo, ntp_cmd, args, cmd, banner_id, data, function, vnc_client_response,
                                             vnc_password, \
                                             vnc_server_challenge, inputs, domain, headers_call_id,
                                             headers_content_length, headers_cseq, \
                                             headers_from, headers_to, headers_via, community_string, requests, urg,
                                             psh, fin, \
                                             appname, cltintname, database, language, servername, domainname)

                    if logbool and white == 2:
                        # 发送邮件功能
                        if switches() == 'on':
                            if str(logtype) == '2000':
                                logtype = 'ftp登录尝试'
                            elif str(logtype) == '3000':
                                logtype = 'web蜜罐被访问'
                            elif str(logtype) == '3001':
                                logtype = 'web蜜罐被登录'
                            elif str(logtype) == '4000':
                                logtype = 'ssh建立连接'
                            elif str(logtype) == '4001':
                                logtype = 'ssh远程版本发送'
                            elif str(logtype) == '4002':
                                logtype = 'ssh登录尝试'
                            elif str(logtype) == '6001':
                                logtype = 'telnet登录尝试'
                            elif str(logtype) == '5001':
                                logtype = '端口(SYN)扫描'
                            elif str(logtype) == '8001':
                                logtype = 'mysql登录尝试'
                            # 扩表新增
                            elif str(logtype) == '9418':
                                logtype = 'git clone请求'
                            elif str(logtype) == '11001':
                                logtype = 'ntp monlist请求'
                            elif str(logtype) == '17001':
                                logtype = 'redis命令'
                            elif (str(logtype) == '18001' or str(logtype) == '18002' or \
                                  str(logtype) == '18003' or str(logtype) == '18004' or str(logtype) == '18005'):
                                logtype = 'TCP连接请求'
                            elif str(logtype) == '12001':
                                logtype = 'vnc连接'
                            elif str(logtype) == '14001':
                                logtype = 'windows远程登录'
                            elif str(logtype) == '13001':
                                logtype = 'snmp扫描'
                            elif str(logtype) == '15001':
                                logtype = 'sip请求'
                            elif str(logtype) == '5002':
                                logtype = 'NMAP OS扫描'
                            elif str(logtype) == '5003':
                                logtype = 'NMAP NULL扫描'
                            elif str(logtype) == '5004':
                                logtype = 'NMAP XMAS扫描'
                            elif str(logtype) == '5005':
                                logtype = 'NMAP FIN扫描'
                            elif str(logtype) == '9001':
                                logtype = 'mssql登录sql账户认证'
                            elif str(logtype) == '9002':
                                logtype = 'mssql登录win身份认证'
                            elif str(logtype) == '7001':
                                logtype = 'http代理登录尝试'
                            content = "攻击主机：" + src_host + "攻击主机端口: " + src_port + "--" + "被攻击主机：" + dst_host + "被攻击主机端口：" + dst_port + "--" + "攻击时间：" + local_time
                            # 将发送邮件丢到任务队列
                            sched.add_job(
                                send_mail,
                                'date',
                                run_date=(datetime.now() +
                                          datetimes.timedelta(seconds=1)),
                                args=["蜜罐告警：" + logtype, content],
                                id=str(uuid.uuid1()))
                            return True

            else:
                return False
        else:
            return False
