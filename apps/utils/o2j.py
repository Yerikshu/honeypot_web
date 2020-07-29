#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 7/29/20
# @Time     : 10:45 AM
# @Purpose  : 将对象转为json
from sqlalchemy import inspect


def object_as_json(obj):
    return {c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs}