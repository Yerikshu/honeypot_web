# 蜂蜜坛子分析系统
具备的功能（未完待续）
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
蜜罐的agent服务已经打包好并上传在腾讯云的docker 仓库，可以自行下载并安装，agent的[源码](https://github.com/thinkst/opencanary)，由于其目前只能适用于python2版本，后续计划升级到python3版本，目前先制作docker镜像暂时解决代码不能运行在新版服务器上面的问题

下载指令：
```
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent:2.1
```
需要注意的是对于latest版本，需要自己手动对服务进行编译安装，里面需要自己手动调整配置，个人强烈建议使用2.1版本，后续会根据需要持续迭代新版本
```
docker pull ccr.ccs.tencentyun.com/otherproject/honeypot-agent:latest
```
## 启动环境
目前仅仅测试redhat7以及centos7以上，因为对于其版本以下的系统，内核不支持docker服务

# 安装

## 自动化安装
直接执行命令
```
bash install/install_opencanary_agent.sh
```

## 手动安装
考虑到有些业务环境下不允许访问外网，这个时候可以通过ftp的形式将这些镜像文件、docker离线包上传到主机，


## 离线包下载
[docker-19.03.9.tgz](https://github.com/Yerikshu/honeypot_web/releases/tag/beta)

[honey-agent-2-0.tar.gz](https://github.com/Yerikshu/honeypot_web/releases/tag/2.0)

## 安装蜜罐

### 宿主机rsyslog配置
sed -i '50i kern.*                                              /var/log/kern.log' /etc/rsyslog.conf
chkconfig --level 2345 rsyslog on && service rsyslog restart

### 宿主机防火墙策略配置

#### 安装iptables service
cat /etc/redhat-release   ## 查看redhat小版本
我这里暂时提供redhat7.6所需要的iptable的[安装包](https://github.com/Yerikshu/honeypot_web/releases/tag/7.6)，后续根据需要在逐步添上
```
rpm -ivh iptables-services-1.4.21-28.el7.x86_64.rpm 
service iptables start
```

#### 添加iptables策略
直接在命令行添加以下命令
```
iptables -t mangle -A PREROUTING -p tcp -i lo -j LOG --log-level=warning --log-prefix="canaryfw: " -m limit --limit="3/hour"
iptables -t mangle -A PREROUTING -p tcp --syn -j LOG --log-level=warning --log-prefix="canaryfw: " -m limit --limit="5/second" !  -i lo
iptables -t mangle -A PREROUTING -p tcp --tcp-flags ALL URG,PSH,SYN,FIN -m u32 --u32 "40=0x03030A01 && 44=0x02040109 && 48=0x080Affff && 52=0xffff0000 && 56=0x00000402" -j LOG --log-level=warning --log-prefix="canarynmap: " -m limit --limit="5/second"
iptables -t mangle -A PREROUTING -p tcp -m u32 --u32 "6&0xFF=0x6 && 0>>22&0x3C@12=0x50000400" -j LOG --log-level=warning --log-prefix="canarynmapNULL: " -m limit --limit="5/second"
iptables -t mangle -A PREROUTING -p tcp -m u32 --u32 "6&0xFF=0x6 && 0>>22&0x3C@12=0x50290400" -j LOG --log-level=warning --log-prefix="canarynmapXMAS: " -m limit --limit="5/second"
iptables -t mangle -A PREROUTING -p tcp -m u32 --u32 "6&0xFF=0x6 && 0>>22&0x3C@12=0x50010400" -j LOG --log-level=warning --log-prefix="canarynmapFIN: " -m limit --limit="5/second"
```
```
iptables -t mangle  -L  ## 确认策略已添加
service iptables save  ## 保存策略
```
#### 测试扫描日志

```
curl http://127.0.0.1:443
```
查看是否出现源地址为本机，目的端口为443的日志

```
tail -f /var/log/kern.log 
canaryfw: IN=lo OUT= MAC=00:00:00:00:00:00:00:00:00:00:00:00:08:00 SRC=127.0.0.1 DST=127.0.0.1 LEN=40 TOS=0x00 PREC=0x00 TTL=64 ID=54161 DF PROTO=TCP SPT=443 DPT=39104 WINDOW=0 RES=0x00 ACK RST URGP=0
```

### docker环境配置

通过sftp上传docker二进制文件及蜜罐镜像之后解压缩
```
tar -zxvf docker-19.03.9.tgz && cp docker/* /usr/bin/ && tar -zxvf honey-agent-2-0.tar.gz
```
启动docker服务   
```
dockerd &
```
导入镜像
```
docker load < honey-agent-2-0
```
创建容器并运行镜像，映射kern.log文件
```
setenforce 0
docker run -itd --name honey  --network=host -v /var/log/kern.log:/var/log/kern.log honeypot-agent:2.0
```
进入容器
```
docker exec -it honey bash
vi /root/.opencanary.conf  --->>>修改节点名称以及配置对应的master地址，其他不用改
opencanaryd --start
```


# agen版本介绍
[大部分源码](https://github.com/Yerikshu/opencanary)这个项目，自己个性化部署后续陆续加上，还没来得及整理好

## 2.0
基础版本，由于之前在测试的时候已经做了一系列的迭代，所以这个公开的时候就直接上升到2.0，后续都在这个基础上升级迭代

## 2.1
[] 增加crontab功能
[] 对agent状态进行监测
[] 宕机自动恢复

# 后面有时间的话再提供物理机独立部署的攻略，也是挺麻烦的

# 注意：超级坑爹的bug  
这个是有时候在部署的过程中会出现这个错误：
```
2020-06-29T15:42:30+0800 [-] Unhandled Error
        Traceback (most recent call last):
          File "/usr/local/lib/python2.7/site-packages/twisted/python/log.py", line 103, in callWithLogger
            return callWithContext({"system": lp}, func, *args, **kw)
          File "/usr/local/lib/python2.7/site-packages/twisted/python/log.py", line 86, in callWithContext
            return context.call({ILogContext: newCtx}, func, *args, **kw)
          File "/usr/local/lib/python2.7/site-packages/twisted/python/context.py", line 122, in callWithContext
            return self.currentContext().callWithContext(ctx, func, *args, **kw)
          File "/usr/local/lib/python2.7/site-packages/twisted/python/context.py", line 85, in callWithContext
            return func(*args,**kw)
        --- <exception caught here> ---
          File "/usr/local/lib/python2.7/site-packages/twisted/internet/posixbase.py", line 614, in _doReadOrWrite
            why = selectable.doRead()
          File "/usr/local/lib/python2.7/site-packages/twisted/internet/inotify.py", line 249, in doRead
            fdesc.readFromFD(self._fd, self._doRead)
          File "/usr/local/lib/python2.7/site-packages/twisted/internet/fdesc.py", line 94, in readFromFD
            callback(output)
          File "/usr/local/lib/python2.7/site-packages/twisted/internet/inotify.py", line 276, in _doRead
            iwp._notify(path, mask)
          File "/usr/local/lib/python2.7/site-packages/twisted/internet/inotify.py", line 150, in _notify
            callback(self, filepath, events)
          File "/usr/local/lib/python2.7/site-packages/opencanary/modules/__init__.py", line 169, in onChange
            self.processAuditLines()
          File "/usr/local/lib/python2.7/site-packages/opencanary/modules/__init__.py", line 161, in processAuditLines
            self.handleLines(lines=lines)
          File "/usr/local/lib/python2.7/site-packages/opencanary/modules/portscan.py", line 57, in handleLines
            self.logger.log(data)
          File "/usr/local/lib/python2.7/site-packages/opencanary/logger.py", line 176, in log
            scheduler = TwistedScheduler()
          File "/usr/local/lib/python2.7/site-packages/apscheduler/schedulers/base.py", line 83, in __init__
            self.configure(gconfig, **options)
          File "/usr/local/lib/python2.7/site-packages/apscheduler/schedulers/base.py", line 122, in configure
            self._configure(config)
          File "/usr/local/lib/python2.7/site-packages/apscheduler/schedulers/twisted.py", line 37, in _configure
            super(TwistedScheduler, self)._configure(config)
          File "/usr/local/lib/python2.7/site-packages/apscheduler/schedulers/base.py", line 694, in _configure
            self.timezone = astimezone(config.pop('timezone', None)) or get_localzone()
          File "/usr/local/lib/python2.7/site-packages/tzlocal/unix.py", line 165, in get_localzone
            _cache_tz = _get_localzone()
          File "/usr/local/lib/python2.7/site-packages/tzlocal/unix.py", line 128, in _get_localzone
            utils.assert_tz_offset(tz)
          File "/usr/local/lib/python2.7/site-packages/tzlocal/utils.py", line 46, in assert_tz_offset
            raise ValueError(msg)
        exceptions.ValueError: Timezone offset does not match system offset: 39600 != 28800. Please, check your config files.
```
原因是时区问题，解决办法如下：
修改 /usr/local/lib/python2.7/site-packages/opencanary/logger.py
在176行，scheduler = TwistedScheduler()，修改为scheduler = TwistedScheduler(timezone="Asia/Shanghai")  ，强行设置为与操作系统相同的东八区即可

