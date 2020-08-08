#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/29/20
# @Time     : 4:19 PM
# @Purpose  : 获取日志经过白名单的内容
import jwt
from fastapi import APIRouter
from loguru import logger
from pydantic import BaseModel

from apps.attack_log_whitelist.log_whitelist_opt import log_whitelist_opt

router = APIRouter()

logselect = log_whitelist_opt()


# 暂时默认分页为10页
class Item(BaseModel):
    white_list: int
    page: int


def total_atk_page():
    # 查询攻击列表数量
    return logselect.white_select_num()


# mintime:yyyy-MM-DD hh:mm:ss
# maxtime:yyyy-MM-DD hh:mm:ss
def total_wit_page(mintime, maxtime):
    # 查询过滤列表数量
    return logselect.select_filter_total(mintime, maxtime)


@router.post("/log/white")
@logger.catch
async def white_log():
    tmp = logselect.select_whitelist()
    it = iter(tmp)
    result = set()
    for i in it:
        result.add(i)
    return result
