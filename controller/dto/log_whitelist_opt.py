#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 9:56 PM
# @Purpose  : 白名单表操作
from sqlalchemy import desc, extract, func
from sqlalchemy.exc import InvalidRequestError

from conf.db import DBSession
from models.attack_log_whitelist import attack_log_whitelist


class log_whitelist_opt:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def insert_white(self, dst_host, dst_port, honeycred, local_time, hostname, password, path, skin, useragent,
                     username, session, localversion, remoteversion, df, idid, inin, lenlen, mac, outout,
                     prec, proto, res, syn, tos, ttl, urgp, window, logtype, node_id, src_host, src_port, white, repo,
                     ntp_cmd, args, cmd, banner_id, data, function, vnc_client_response, vnc_password,
                     vnc_server_challenge, inputs, domain, headers_call_id, headers_content_length, headers_cseq,
                     headers_from, headers_to, headers_via, community_string, requests, urg, psh, fin, appname,
                     cltintname, database, language, servername, domainname):

        loginsert = attack_log_whitelist(dst_host=dst_host, dst_port=dst_port, honeycred=honeycred,
                                         local_time=local_time,
                                         hostname=hostname, password=password, path=path, skin=skin,
                                         useragent=useragent,
                                         username=username, session=session, localversion=localversion,
                                         remoteversion=remoteversion, df=df,
                                         idid=idid, inin=inin, lenlen=lenlen, mac=mac, outout=outout, prec=prec,
                                         proto=proto, res=res, syn=syn,
                                         tos=tos, ttl=ttl, urgp=urgp, window=window, logtype=logtype, node_id=node_id,
                                         src_host=src_host,
                                         src_port=src_port, white=white,
                                         repo=repo, ntp_cmd=ntp_cmd, args=args, cmd=cmd, banner_id=banner_id, data=data,
                                         function=function, vnc_client_response=vnc_client_response,
                                         vnc_password=vnc_password,
                                         vnc_server_challenge=vnc_server_challenge, inputs=inputs, domain=domain,
                                         headers_call_id=headers_call_id,
                                         headers_content_length=headers_content_length, headers_cseq=headers_cseq,
                                         headers_from=headers_from, headers_to=headers_to,
                                         headers_via=headers_via, community_string=community_string, requests=requests,
                                         urg=urg, psh=psh, fin=fin,
                                         appname=appname, cltintname=cltintname, database=database, language=language,
                                         servername=servername, domainname=domainname)

        if loginsert:
            try:
                self.session.add(loginsert)
                self.session.commit()
                return True
            except InvalidRequestError:
                self.session.rollback()
            except Exception as e:
                print(e)
            finally:
                self.session.close()
        else:
            return False

    # 查询日志表攻击列表数据
    def page_select_white(self, page_index):
        try:
            page_size = 10
            # num = 10*int(page) - 10
            logselect = self.session.query(attack_log_whitelist).filter(
                attack_log_whitelist.white == 2).order_by(
                desc(attack_log_whitelist.local_time),
                attack_log_whitelist.id).limit(page_size).offset(
                (page_index - 1) * page_size)
            return logselect
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 查询日志表白名单数据
    def page_select_whitelist(self, page_index, page_size=10):
        try:
            # num = 10*int(page) - 10
            # logselect = self.session.query(attack_log_whitelist).filter(
            #     attack_log_whitelist.white == 1).order_by(
            #     desc(attack_log_whitelist.local_time),
            #     attack_log_whitelist.id).limit(page_size).offset(
            #     (page_index - 1) * page_size)
            logselect = self.session.query(attack_log_whitelist).filter(
                attack_log_whitelist.white == 1).order_by(
                desc(attack_log_whitelist.local_time),
                attack_log_whitelist.id).slice((page_index - 1) * page_size, page_index * page_size)
            return logselect
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 查询当年每月白名单内攻击数量
    def white_select_num(self, months):
        try:
            white_num = self.session.query(
                extract('month', attack_log_whitelist.local_time).label('month'),
                func.count('*').label('count')).filter(
                extract('year', attack_log_whitelist.local_time) == months,
                attack_log_whitelist.white == 1).group_by('month').all()
            return white_num
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
