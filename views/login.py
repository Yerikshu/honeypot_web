#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 10:29 PM
# @Purpose  : 登录认证
from typing import Optional

from fastapi import FastAPI, Header

login = FastAPI()


@login.post("/auth/*")
async def auth(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}