#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/22/20
# @Time     : 5:49 PM
# @Purpose  :
import time
from typing import Callable
from fastapi import Request, Response

from fastapi.routing import APIRouter


router = APIRouter()

from .host import view

# class BaseRoute(APIRoute):
#     def get_route_handler(self) -> Callable:
#         original_route_handler = super().get_route_handler()
#
#         async def custom_route_handler(request: Request) -> Response:
#             before = time.time()
#             response: Response = await original_route_handler(request)
#             duration = time.time() - before
#             response.headers["X-Response-Time"] = str(duration)
#             response.headers["Access-Control-Allow-Origin"] = "*"  # 这个地方可以写域名
#             response.headers["Access-Control-Allow-Methods"] = 'POST, GET'
#             response.headers["Access-Control-Max-Age"] = 1000
#             response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
#             response.headers["Server"] = "Apache-Coyote/1.1"
#
#             print(f"route duration: {duration}")
#             print(f"route response: {response}")
#             print(f"route response headers: {response.headers}")
#             return response
#
#         return custom_route_handler
