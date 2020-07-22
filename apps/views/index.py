#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 10:14 PM
# @Purpose  : 首页

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return
