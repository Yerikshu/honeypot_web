# 蜂蜜坛子分析系统
具备的功能（未完待续）
- 核心功能
    - 白名单对已入库数据进行重新整理
    - 搜索功能
    - 报表归类输出
        - 按业务
        - 按时间
- 辅助功能
    - 主机状态发现
    - agent下线重启
    - iptable策略配置
        - 比如配置相关的白名单ip，其他的ip流量不允许通过，这个是给予内网安全进行考虑的
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


具体使用可以看看隔壁agent项目[介绍](https://github.com/Yerikshu/opencanary)

# 使用指南
1. 首次使用为了安全起见，建议使用` openssl rand -hex 32`更新秘钥并替换在` conf/key.py`中
