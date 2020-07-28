#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/28/20
# @Time     : 9:56 AM
# @Purpose  : 数据包规则匹配实现基于策略的四元组进行匹配
import hashlib

from apps.white_list.whitelist_opt import white_new
from conf.redis import r

white_res_activate, white_res_deactivate = white_new().whitelist_data()

md5 = hashlib.md5()  # 应用MD5算法


def whitelist_set():
    # 配置hset
    # name: whitelist
    # key: hash(source_ip, source_port, dst_ip, dst_port)
    # value: deactivate表示未激活,activate表示激活
    # redis中默认的存储时间暂时为永久，后续再考虑更新机制
    if white_res_activate:
        for item in white_res_activate:
            if not item.source_ip:
                continue
            if item.source_port == 'deny':
                tmp = "{},{},{}".format(item.source_ip, item.dst_ip, item.dst_port)
            else:
                tmp = "{},{},{},{}".format(item.source_ip, item.source_port, item.dst_ip, item.dst_port)

            md5.update(tmp.encode('utf-8'))
            r.sadd("acivate", md5.hexdigest())
    if white_res_deactivate:
        for item in white_res_deactivate:
            md5.update(item.__str__().encode('utf-8'))
            r.sadd("deacivate", md5.hexdigest())


if __name__ == "__main__":
    whitelist_set()
