#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 4:53 PM
# @Purpose  : 白名单表操作


from sqlalchemy.exc import InvalidRequestError

from conf.db import DBSession
from models.white_list import white_list


class white_new:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    # 查询白名单新表数据
    def white_ip(self):
        try:
            white_ip_res = self.session.query(white_list).all()
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
            wip_insert = white_list(sourceip=src_host)
            self.session.merge(wip_insert)
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # TODO:增加白名单之后需要更新入库的数据
