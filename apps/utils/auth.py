#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : yerikyu
# @Date     : 20-8-8
# @Time     : 下午1:50
# @Purpose  : jwt认证模块
import json
from datetime import time

import jwt
from jwt import exceptions

from conf.key import SECRET_KEY, ALGORITHM


def create_token(name):
    """基于jwt创建token的函数"""
    headers = {
        "alg": "HS256",
        "typ": "JWT"
    }
    exp = int(time.time() + 20)
    payload = {
        "name": name,
        "exp": exp
    }
    token = jwt.encode(payload=payload, key=SECRET_KEY, algorithm=ALGORITHM, headers=headers).decode('utf-8')
    # 返回生成的token
    return token


def validate_token(token):
    """校验token的函数，校验通过则返回解码信息"""
    payload = None
    msg = None
    try:
        payload = jwt.decode(token, SECRET_KEY, True, algorithm=ALGORITHM)
        # jwt有效、合法性校验
    except exceptions.ExpiredSignatureError:
        msg = 'token已失效'
    except jwt.DecodeError:
        msg = 'token认证失败'
    except jwt.InvalidTokenError:
        msg = '非法的token'
    return payload, msg


@app.route('/login', methods=['POST'])
def login():
    """用户登录，用户名密码验证成功将会生成对应token，但不需要在本地保存，直接返回给用户"""
    username = request.form.get('username', None)
    pwd = request.form.get('password', None)
    if (not username) or (not pwd):
        return json.dumps({'status': 1, 'code': '400', 'msg': '用户或密码不允许为空！'}, ensure_ascii=False)
    if not db_source['user_table'].get(username, None):
        return json.dumps({'status': 1, 'code': '401', 'msg': '用户不存在！'}, ensure_ascii=False)
    if db_source['user_table'][username]['pwd'] != pwd:
        return json.dumps({'status': 1, 'code': '402', 'msg': '用户名或密码错误！'}, ensure_ascii=False)
    # 当登录校验通过，则为用户创建并返回token
    token = create_token(username)
    # 注意这里不存入本地了
    return json.dumps({'status': 1, 'code': '200', 'data': {'token': token}})


@app.route('/user_info', methods=['GET'])
def user_info():
    """查看用户信息，需要token校验"""
    token = request.args.get('token', None)
    if not token:
        return json.dumps({'status': 1, 'code': '500', 'msg': 'token不允许为空！'}, ensure_ascii=False)
    payload, msg = validate_token(token)
    # 直接对token进行合法性校验
    if msg:
        return json.dumps({'status': 1, 'code': '500', 'msg': msg}, ensure_ascii=False)
    username = payload['name']
    info = db_source['user_info_table'][username]
    return json.dumps({'status': 1, 'code': '200', 'data': {username: info}})
