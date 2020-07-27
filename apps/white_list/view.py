#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:23 PM
# @Purpose  : 提取白名单配置信息
from loguru import logger
from pydantic import BaseModel

from apps.base_route import router
from apps.white_list.whitelist_opt import white_new

white_list = white_new.white_ip()


@router.get("/white_list")
@logger.catch
async def whiteiplist():
    result = set()
    it = iter(white_list)
    for x in it:
        result.add(x)
    return result
