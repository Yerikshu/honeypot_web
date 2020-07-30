#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 9:56 PM
# @Purpose  : 白名单表操作
from loguru import logger
from sqlalchemy import desc, extract, func
from sqlalchemy.exc import InvalidRequestError

from apps.utils.o2j import object_as_json
from conf.db import DBSession
from apps.attack_log_whitelist.model import attack_log_whitelist


class log_whitelist_opt:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def insert(self, param):

        loginsert = attack_log_whitelist(**param)

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
            logger.info(e)
        finally:
            self.session.close()

    # 查询日志表白名单数据
    def select_whitelist(self):
        try:
            result = list()
            page_size = 10
            # logselect = self.session.query(attack_log_whitelist).filter(
            #     attack_log_whitelist.white == 1).order_by(
            #     desc(attack_log_whitelist.local_time),
            #     attack_log_whitelist.id).limit(page_size).offset(
            #     (page_index - 1) * page_size)
            # logselect = self.session.query(attack_log_whitelist).filter().order_by(
            #     desc(attack_log_whitelist.local_time),
            #     attack_log_whitelist.id).slice((page_index - 1) * page_size, page_index * page_size)
            log_select = self.session.query(attack_log_whitelist).order_by(desc(attack_log_whitelist.local_time)).all()
            # for u in log_select:
            #     d = object_as_json(u)
            #     result.append(d)
            return log_select
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            logger.error(e)
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

    # 查询过滤列表总量
    # 按时间过滤
    # mintime:yyyy-MM-DD hh:mm:ss
    # maxtime:yyyy-MM-DD hh:mm:ss
    def select_filter_total(self, min_time, max_time):
        try:
            total_filter = self.session.query(
                func.count(attack_log_whitelist.id)).filter(attack_log_whitelist.local_time <= max_time).filter(
                attack_log_whitelist.local_time >= min_time
                ).scalar()
            return total_filter
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
