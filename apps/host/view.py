#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/21/20
# @Time     : 10:17 PM
# @Purpose  : 获取主机状态列表
import datetime
from typing import Optional
from asgi_request_id import RequestIDMiddleware, get_request_id
from fastapi import FastAPI
from pydantic import BaseModel

from apps.base_route import router
from apps.host.service import hoststatus, getHoststatus

# host = FastAPI(title="主机访问id记录")

# host.add_middleware(
#     RequestIDMiddleware,
#     incoming_request_id_header="request_id",
# )


class host_info(BaseModel):
    hostname: str
    ip: str
    status: str


@router.post("/host")
async def agent_host(item: Optional[host_info] = None):
    """ 接收post过来的主机信息 """
    # 根据蜜罐客户端提交过来请求，以服务器端时间为准（从服务器端生成时间）
    lasttime = datetime.datetime.now()
    hostname = item.hostname
    ip = item.ip
    status = item.status

    # 主机信息入库
    if hoststatus(lasttime, hostname, ip, status):
        # TODO:这个地方是要配置日志记录，后续写上
        # log.write("insert status data ok")
        pass


# TODO:注意完成jwt鉴权操作
# @jwtauth
@router.get("/host")
async def agent_host_status():
    return getHoststatus()
