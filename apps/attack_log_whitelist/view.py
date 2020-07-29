#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/29/20
# @Time     : 4:19 PM
# @Purpose  : 获取日志经过白名单的内容
from fastapi import APIRouter
from loguru import logger

from apps.attack_log_whitelist import log_whitelist_opt

router = APIRouter()

logselect = log_whitelist_opt


def total_atk_page():
    # 查询攻击列表数量
    return logselect.white_select_num()


# mintime:yyyy-MM-DD hh:mm:ss
# maxtime:yyyy-MM-DD hh:mm:ss
def total_wit_page(mintime, maxtime):
    # 查询过滤列表数量
    return logselect.select_filter_total(mintime, maxtime)


@router.get("/log/white")
@logger.catch
async def white_log():
    pass
