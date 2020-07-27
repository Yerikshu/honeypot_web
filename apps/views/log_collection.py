#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:00 PM
# @Purpose  : 接收agent的日志请求
import json
from typing import Optional

from loguru import logger
from pydantic import BaseModel

from apps.base_route import router
from apps.controller.service.analyse_log import parserlog


# 由于发送过来的日志内容很多,
# 而且保证都是json格式,
# 还没想好怎么提前做好序列化构造
class item(BaseModel):
    param: str


@router.post("/log")
@logger.catch
async def receive_agent_log(item: Optional[item] = None):
    item = json.loads(item.param.lower())
    parserlog(item)
