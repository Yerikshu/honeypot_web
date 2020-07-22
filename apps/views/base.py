#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/20/20
# @Time     : 10:24 PM
# @Purpose  : 请求基础类

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class base(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()



