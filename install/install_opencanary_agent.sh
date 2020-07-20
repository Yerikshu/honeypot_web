#!/bin/sh
#Author: yerik_shu
#Email : treestore@foxmail.com
#Date  : 2020-07-20
#Environment: Centos7.6|Redhat7

curl -sSL http://acs-public-mirror.oss-cn-hangzhou.aliyuncs.com/docker-engine/internet | sh -

docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent:2.1