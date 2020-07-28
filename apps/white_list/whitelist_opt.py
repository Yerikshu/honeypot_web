#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 4:53 PM
# @Purpose  : 白名单表操作
from sqlalchemy.exc import InvalidRequestError

from conf.db import DBSession
from apps.white_list.white_list import white_list


class white_new:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def whitelist_data(self):
        try:
            # 查询白名单表已激活数据
            white_ip_res_activate = self.session.query(white_list).filter(white_list.activate == 1).order_by(white_list.dst_port).all()
            # 查询白名单表未激活数据
            white_ip_res_deactivate = self.session.query(white_list).filter(white_list.activate == 0).all()
            return white_ip_res_activate, white_ip_res_deactivate
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 增加白名单
    def insert_white_ip(self, src_host):
        try:
            wip_insert = white_list(sourceip=src_host)
            self.session.merge(wip_insert)
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # TODO:增加白名单之后需要更新入库的数据
