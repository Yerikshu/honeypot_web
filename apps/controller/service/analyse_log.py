#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:10 PM
# @Purpose  : 解析客户端请求过来的日志

import copy
import datetime


def parserlog(jsonlog):
    # 接收客户端post过来的数据格式化
    jsonlog = copy.deepcopy(jsonlog)
    if jsonlog:
        if jsonlog.has_key("dst_host"):
            dst_host = jsonlog["dst_host"]
            # print type(dst_host)
        else:
            dst_host = ''
        if jsonlog.has_key("src_host"):
            src_host = jsonlog["src_host"]
        else:
            src_host = ''

        if jsonlog.has_key("logdata"):
            if jsonlog["logdata"].has_key("hostname"):
                jsonlog["hostname"] = jsonlog["logdata"]["hostname"]
            if jsonlog["logdata"].has_key("password"):
                jsonlog["password"] = jsonlog["logdata"]["password"]
            if jsonlog["logdata"].has_key("path"):
                jsonlog["path"] = jsonlog["logdata"]["PATH"]
            if jsonlog["logdata"].has_key("skin"):
                jsonlog["skin"] = jsonlog["logdata"]["skin"]
            if jsonlog["logdata"].has_key("useragent"):
                jsonlog["useragent"] = jsonlog["logdata"]["useragent"]
            if jsonlog["logdata"].has_key("username"):
                jsonlog["username"] = jsonlog["logdata"]["username"]
            if jsonlog["logdata"].has_key("session"):
                jsonlog["session"] = jsonlog["logdata"]["session"]
            if jsonlog["logdata"].has_key("localversion"):
                jsonlog["localversion"] = jsonlog["logdata"]["localversion"]
            if jsonlog["logdata"].has_key("remoteversion"):
                jsonlog["remoteversion"] = jsonlog["logdata"]["remoteversion"]
            if jsonlog["logdata"].has_key("df"):
                jsonlog["df"] = jsonlog["logdata"]["DF"]
            if jsonlog["logdata"].has_key("id"):
                jsonlog["idid"] = jsonlog["logdata"]["id"]
            if jsonlog["logdata"].has_key("in"):
                jsonlog["inin"] = jsonlog["logdata"]["in"]
            if jsonlog["logdata"].has_key("len"):
                jsonlog["lenlen"] = jsonlog["logdata"]["len"]
            if jsonlog["logdata"].has_key("mac"):
                jsonlog["mac"] = jsonlog["logdata"]["mac"]
            if jsonlog["logdata"].has_key("out"):
                jsonlog["outout"] = jsonlog["logdata"]["out"]
            if jsonlog["logdata"].has_key("prec"):
                jsonlog["prec"] = jsonlog["logdata"]["prec"]
            if jsonlog["logdata"].has_key("proto"):
                jsonlog["proto"] = jsonlog["logdata"]["proto"]
            if jsonlog["logdata"].has_key("res"):
                jsonlog["res"] = jsonlog["logdata"]["res"]
            if jsonlog["logdata"].has_key("syn"):
                jsonlog["syn"] = jsonlog["logdata"]["syn"]
            if jsonlog["logdata"].has_key("tos"):
                jsonlog["tos"] = jsonlog["logdata"]["tos"]
            if jsonlog["logdata"].has_key("ttl"):
                jsonlog["ttl"] = jsonlog["logdata"]["ttl"]
            if jsonlog["logdata"].has_key("urgp"):
                jsonlog["urgp"] = jsonlog["logdata"]["urgp"]
            if jsonlog["logdata"].has_key("window"):
                jsonlog["window"] = jsonlog["logdata"]["window"]
            # 扩表后的新加解析日志请求格式化
            if jsonlog["logdata"].has_key("repo"):
                jsonlog["repo"] = jsonlog["logdata"]["repo"]
            if jsonlog["logdata"].has_key("ntp cmd"):
                ntp_cmd = jsonlog["logdata"]["ntp cmd"]
            if jsonlog["logdata"].has_key("args"):
                jsonlog["args"] = jsonlog["logdata"]["args"]
            if jsonlog["logdata"].has_key("cmd"):
                jsonlog["cmd"] = jsonlog["logdata"]["cmd"]
            if jsonlog["logdata"].has_key("banner_id"):
                jsonlog["banner_id"] = jsonlog["logdata"]["banner_id"]
            if jsonlog["logdata"].has_key("data"):
                jsonlog["data"] = jsonlog["logdata"]["data"]
            if jsonlog["logdata"].has_key("function"):
                jsonlog["function"] = jsonlog["logdata"]["function"]

            if jsonlog["logdata"].has_key("vnc client response"):
                jsonlog["vnc_client_response"] = jsonlog["logdata"]["vnc client response"]
            if jsonlog["logdata"].has_key("vnc password"):
                jsonlog["vnc_password"] = jsonlog["logdata"]["vnc password"]
            if jsonlog["logdata"].has_key("vnc server challenge"):
                jsonlog["vnc_server_challenge"] = jsonlog["logdata"]["vnc server challenge"]

            if jsonlog["logdata"].has_key("input"):
                jsonlog["inputs"] = jsonlog["logdata"]["inputs"]

            if jsonlog["logdata"].has_key("domain"):
                jsonlog["domain"] = jsonlog["logdata"]["domain"]

            if jsonlog["logdata"].has_key("headers"):
                if jsonlog["logdata"]["headers"].has_key("call-id"):
                    jsonlog["headers_call_id"] = jsonlog["logdata"]["headers"]["call-id"][0]

                if jsonlog["logdata"]["headers"].has_key("content_length"):
                    jsonlog["headers_content_length"] = jsonlog["logdata"]["headers"]["content_length"][0]

                if jsonlog["logdata"]["headers"].has_key("cseq"):
                    jsonlog["headers_cseq"] = jsonlog["logdata"]["headers"]["cseq"][0]

                if jsonlog["logdata"]["headers"].has_key("from"):
                    jsonlog["headers_from"] = jsonlog["logdata"]["headers"]["from"][0]

                if jsonlog["logdata"]["headers"].has_key("to"):
                    jsonlog["headers_to"] = jsonlog["logdata"]["headers"]["to"][0]

                if jsonlog["logdata"]["headers"].has_key("via"):
                    jsonlog["headers_via"] = jsonlog["logdata"]["headers"]["via"][0]

            if jsonlog["logdata"].has_key("community_string"):
                jsonlog["community_string"] = jsonlog["logdata"]["community_string"]

            if jsonlog["logdata"].has_key("requests"):
                jsonlog["requests"] = jsonlog["logdata"]["requests"][0]

            if jsonlog["logdata"].has_key("urg"):
                jsonlog["urg"] = jsonlog["logdata"]["urg"]

            if jsonlog["logdata"].has_key("psh"):
                jsonlog["psh"] = jsonlog["logdata"]["psh"]

            if jsonlog["logdata"].has_key("fin"):
                jsonlog["fin"] = jsonlog["logdata"]["fin"]

            if jsonlog["logdata"].has_key("appname"):
                jsonlog["appname"] = jsonlog["logdata"]["appname"]

            if jsonlog["logdata"].has_key("cltintname"):
                jsonlog["cltintname"] = jsonlog["logdata"]["cltintname"]

            if jsonlog["logdata"].has_key("database"):
                jsonlog["database"] = jsonlog["logdata"]["database"]

            if jsonlog["logdata"].has_key("language"):
                jsonlog["language"] = jsonlog["logdata"]["language"]

            if jsonlog["logdata"].has_key("servername"):
                jsonlog["servername"] = jsonlog["logdata"]["servername"]

            if jsonlog["logdata"].has_key("domainname"):
                jsonlog["domainname"] = jsonlog["logdata"]["domainname"]

        if dst_host:
            if src_host:
                # 判断攻击主机是否存在于白名单列表内
                if (src_host, dst_host,
                    dst_port) in whiteiplist() or dst_host == src_host or src_host in whiteiplist_scanner() or (
                        src_host, dst_port) in whiteiplist_4A():
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
