#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 20-8-6
# @Time     : 上午9:48
# @Purpose  : jwt秘钥配置


ALGORITHM = "HS256"
# 过期时间
ACCESS_TOKEN_EXPIRE_MINUTES = 30
# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "ad47ba0c480d4280d2ed35d199695907a92baf1ad2636602e9b1277244a24744"
