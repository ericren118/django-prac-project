from .base import *

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1"]

## 务必修改以下值，确保运行时系统安全:
SECRET_KEY = 'k#-6u4k@_n6dwm+9o5meuddmyy63o88$f%nc__p)9g9q(r&l2s'

## 如果仅使用数据库中的账号，以下 LDAP 配置可忽略
## 替换这里的配置为正确的域服务器配置，同时可能需要修改 base.py 中的 LDAP 服务器相关配置:
LDAP_AUTH_URL = "ldap://101.200.59.94:389"
LDAP_AUTH_CONNECTION_USERNAME = "admin"
LDAP_AUTH_CONNECTION_PASSWORD = "Jonsn@wbcxnwei3529"

INSTALLED_APPS += (
    # other apps for production site
)


## 钉钉群的 WEB_HOOK， 用于发送钉钉消息
DINGTALK_WEB_HOOK = "https://oapi.dingtalk.com/robot/send?access_token=xxxxx"