# 蜂蜜坛子分析系统
具备的功能
- 核心功能
    - 白名单对已入库数据进行重新整理
    - 搜索功能
    - 报表归类输出
        - 按业务
        - 按时间
- 辅助功能
    - agent下线重启
    - 定时发邮件
        - 邮件文案个性化定制
        - 设备下线提醒
    - 配置日志清理
        - 系统运行日志进行汇总，压缩，配置存储策略

# 设计
为了轻量，就轻量到极致
api设计基于fastapi

底层数据库驱动由sqlalchemy提供

# agent
蜜罐的agent服务已经打包好并上传在腾讯云的docker 仓库，可以自行下载并安装

下载指令：
```
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent:2.0
```
需要注意的是对于latest版本，需要自己手动对服务进行编译安装，里面需要自己手动调整配置，个人强烈建议使用2.0版本，后续会根据需要持续迭代新版本
```
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent:latest
```
## 启动环境
目前仅仅测试redhat7以及centos7以上，因为对于其版本以下的系统，内核不支持docker服务

# 安装

## 自动话安装
直接执行命令
```
bash install/install_opencanary_agent.sh
```

## 手动安装
考虑到有些业务环境下不允许访问外网，这个时候可以通过ftp的形式将这些镜像文件、docker离线包上传到主机，


## 离线包下载
[docker-19.03.9.tgz](https://github.com)

[honey-agent.tar.gz](https://github.com)

## 安装蜜罐

通过sftp上传docker二进制文件及蜜罐镜像docker-19.03.9.tgz


tar -zxvf docker-19.03.9.tgz && cp docker/* /usr/bin/ && tar -zxvf honey-agent.tar.gz

## 启动docker服务   
dockerd &

## 加载镜像
docker load < honey-agent-2-0

## 创建容器并运行镜像，映射kern.log文件
setenforce 0
docker run -itd --name honey  --network=host -v /var/log/kern.log:/var/log/kern.log honeypot-agent:2.0

## 进入容器
docker exec -it honey bash
vi /root/.opencanary.conf  --->>>修改节点名称以及配置对应的4a地址，其他不用改
opencanaryd --start



