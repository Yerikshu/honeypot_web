#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/30/20
# @Time     : 9:40 AM
# @Purpose  : 攻击日志未经过白名单部分
from fastapi import APIRouter
from loguru import logger

router = APIRouter()


@router.get("/log/attack")
@logger.catch
async def white_log():
    pass
