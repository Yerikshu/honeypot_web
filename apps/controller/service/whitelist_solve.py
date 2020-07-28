#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/28/20
# @Time     : 9:56 AM
# @Purpose  : 数据包规则匹配实现基于策略的四元组进行匹配
from apps.white_list.whitelist_opt import white_new
from conf.redis import r_activate, r_deactivate

white_res_activate, white_res_deactivate = white_new().whitelist_data()


def whitelist_set():
    # 配置hset
    # name: dst_ip
    # key: dst_port: all/[port]
    # value: [s_ip]: all/[s_port]
    # redis中默认的存储时间暂时为永久，后续再考虑更新机制
    if white_res_activate:
        for item in white_res_activate:
            if not item.source_ip:
                continue
            # 源目ip和端口
            # port可能为any
            value = "{}:{}".format(item.source_ip, item.source_port)
            r_activate.hset(item.dst_ip, item.dst_port, value)

    if white_res_deactivate:
        for item in white_res_deactivate:
            if not item.source_ip:
                continue
            value = "{}:{}".format(item.source_ip, item.source_port)
            r_deactivate.hset(item.dst_ip, item.dst_port, value)


if __name__ == "__main__":
    whitelist_set()
