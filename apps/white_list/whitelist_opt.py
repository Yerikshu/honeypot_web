#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 4:53 PM
# @Purpose  : 白名单表操作
from loguru import logger
from sqlalchemy import inspect
from sqlalchemy.exc import InvalidRequestError

from apps.utils.o2j import object_as_json
from conf.db import DBSession
from apps.white_list.white_list_model import white_list


class white_new:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def whitelist_data(self):
        try:
            # 查询白名单表已激活数据
            white_ip_res_activate = self.session.query(white_list).filter(white_list.activate == 1).order_by(
                white_list.dst_port).all()
            # 查询白名单表未激活数据
            white_ip_res_deactivate = self.session.query(white_list).filter(white_list.activate == 0).all()
            return white_ip_res_activate, white_ip_res_deactivate
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            logger.error(e)
        finally:
            self.session.close()

    # 增加白名单
    def insert_whitelist(self, item):
        try:
            tmp = item.dict()
            wip_insert = white_list(**tmp)
            self.session.merge(wip_insert)
            self.session.commit()
            return True
        except InvalidRequestError:
            self.session.rollback()
            return False
        except Exception as e:
            logger.error(e)
            return False
        finally:
            self.session.close()

    # 读取全部列
    def as_json(self):
        result = list()
        for u in self.session.query(white_list).all():
            d = object_as_json(u)
            result.append(d)
        return result

    # TODO:增加白名单之后需要更新入库的数据
