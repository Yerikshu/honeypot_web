#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 4:58 PM
# @Purpose  : 日志表操作
from loguru import logger
from sqlalchemy import desc, extract, func
from sqlalchemy.exc import InvalidRequestError

from conf.db import DBSession
from apps.attack_log.model import Attack_log


class log_opt:
    """增删改查"""

    def __init__(self):
        self.session = DBSession

    def insert(self, param):

        loginsert = Attack_log(**param)

        if loginsert:
            try:
                self.session.add(loginsert)
                self.session.commit()
                return True
            except InvalidRequestError:
                self.session.rollback()
            except Exception as e:
                logger.error(e)
            finally:
                self.session.close()
        else:
            return False

    # 查询日志表攻击列表数据
    def page_select_attack(self, page_index, page_size=10):
        try:
            # logselect = self.session.query(attack_log).filter(
            #     attack_log.white == 1).order_by(
            #     desc(attack_log.local_time),
            #     attack_log.id).limit(page_size).offset(
            #     (page_index - 1) * page_size)
            logselect = self.session.query(Attack_log).filter(
                Attack_log.white == 1).order_by(
                desc(Attack_log.local_time),
                Attack_log.id).limit(page_size).slice((page_index - 1) * page_size, page_index * page_size)

            return logselect
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            logger.error(e)
        finally:
            self.session.close()

    # 查询当年每月攻击数量
    def attack_select_num(self, months):
        try:
            attack_num = self.session.query(
                extract('month', Attack_log.local_time).label('month'),
                func.count('*').label('count')).filter(
                extract('year', Attack_log.local_time) == months).group_by('month').all()
            return attack_num
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            logger.error(e)
        finally:
            self.session.close()

    # 查询各类攻击数量
    def pie_select_num(self, years):
        try:
            pie_num = self.session.query(
                func.count(Attack_log.logtype),
                Attack_log.logtype).group_by(Attack_log.logtype).filter(
                extract('year', Attack_log.local_time) == years,
                Attack_log.white == 2).all()
            return pie_num
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 查询攻击数据总量
    def select_attack_total(self):
        try:
            total_attack = self.session.query(
                func.count(Attack_log.id)).filter(
                Attack_log.white == 2).scalar()
            return total_attack
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    # 查询过滤列表总量
    def select_filter_total(self):
        try:
            total_filter = self.session.query(
                func.count(Attack_log.id)).filter(
                Attack_log.white == 1).scalar()
            return total_filter
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()
