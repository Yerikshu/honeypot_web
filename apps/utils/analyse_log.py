#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:10 PM
# @Purpose  : 解析客户端请求过来的日志

import copy
import datetime

from apps.attack_log.attack_log_opt import log_opt
from apps.attack_log_whitelist.log_whitelist_opt import log_whitelist_opt
from conf.redis import r_activate

attack_log = log_opt()
white_log = log_whitelist_opt()


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

                if dst_host not in r_activate.keys():
                    # 攻击主机不存在于白名单列表内
                    attack_log.insert(jsonlog)
                    return True
                else:
                    # 攻击日志在白名单内，存在具体目的端口或者判断为any
                    if jsonlog["dst_port"] in r_activate.hgetall(dst_host) or 'any' in r_activate.hgetall(dst_host):
                        white_log.insert(jsonlog)
                        return True
                    tmp = r_activate.hget(dst_host, jsonlog["dst_port"]).split(":")
                    if "any" == tmp[1] or src_host == tmp[0] or jsonlog["src_port"] == tmp[1]:
                        white_log.insert(jsonlog)
                        return True
                    else:
                        attack_log.insert(jsonlog)
                        return True
            else:
                return False
        else:
            return False
