# -*- coding:utf-8 -*-
import os
import logging

# 邮件配置
sender = 'commqa@126.com'  # 发送方
receiver = 'test@126.com'  #接收方
emailusername = 'commqa@126.com'  # 登陆邮箱的用户名
emailpassword = '123456'  # 登陆邮箱的授权码
server = 'mail.126.com'  # smtp服务器

# 测试数据目录
datapath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# 项目配置
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 日志配置
# logpath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
#                     datefmt='%y-%m-%d %H:%M',
#                     filename=os.path.join(logpath, 'log.txt'),
#                     filemode='a')