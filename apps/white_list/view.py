#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/24/20
# @Time     : 5:23 PM
# @Purpose  : 提取白名单配置信息
from typing import Optional

from loguru import logger
from pydantic import BaseModel

from apps.white_list.whitelist_opt import white_new

from fastapi.routing import APIRouter

router = APIRouter()

white_list_activate, white_list_deactivate = white_new().whitelist_data()


class Whitelist_info(BaseModel):
    src_port: str
    src_ip: str
    dst_port: str
    dst_ip: str


@router.get("/whitelist")
@logger.catch
async def get_whiteiplist():
    result = set()
    it = iter(white_list_activate)
    for x in it:
        result.add(x)
    return result


@router.post("/whitelist", response_model=Whitelist_info)
@logger.catch()
async def set_whitelist(item: Whitelist_info):
    # 提交的白名单配置信息
    if white_new().insert_whitelist(item):
        return item

