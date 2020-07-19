#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 白名单表操作

from sqlalchemy.exc import InvalidRequestError

from conf.db import DBSession
from models import attack_log_whitelist


class log_whitelist:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    # 查询白名单新表数据
    def white_ip(self):
        try:
            white_ip_res = self.session.query(attack_log_whitelist).all()
            return white_ip_res
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 增加白名单
    def insert_white_ip(self, src_host):
        try:
            wip_insert = attack_log_whitelist(sourceip=src_host)
            self.session.merge(wip_insert)
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
