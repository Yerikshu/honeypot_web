#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/19/20
# @Purpose  : 主机表操作
from loguru import logger
from sqlalchemy import desc
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.dialects.mysql import insert

from apps.host.model import Host
from conf.db import DBSession


class host_opt:
    def __init__(self):
        self.session = DBSession

    def insert_data(self, id, last_time, hostname, ip, status):
        host_insert = Host(id=id, local_time=last_time, hostname=hostname, ip=ip, status=status)
        # insert_stmt = insert(host). \
        # values(id=id, local_time=last_time, hostname=hostname, ip=ip, status=status)

        # on_conflict_stmt = insert_stmt.on_duplicate_key_update(
        #     last_time=last_time, status=status)
        if host_insert:
            try:
                self.session.add(host_insert)
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

    def select_data(self):
        """
            查询在线主机
        """
        try:
            host_online = self.session.query(host).filter(
                Host.status == "online").order_by(desc(host.last_time)).all()
            return host_online
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            print(e)
        finally:
            self.session.close()

    def select_allhost(self):
        """
            查询所有主机
        """
        try:
            all_host = self.session.query(Host).order_by(desc(Host.last_time)).all()
            return all_host
        except InvalidRequestError:
            self.session.rollback()
        except Exception as e:
            logger.error(e)
        finally:
            self.session.close()
