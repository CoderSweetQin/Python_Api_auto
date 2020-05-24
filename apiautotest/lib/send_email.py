# -*- coding: utf-8 -*-
import smtplib
from email.header import Header
from email.mime.text import MIMEText  # 发送纯文本信息
from email.mime.multipart import MIMEMultipart  # 混合信息
import sys
from config import config
import os
import zipfile
import time

basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)


def zip_report(input_path, output_path, output_name):
    """将测试报告生成压缩文件"""
    f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
    files = os.listdir(input_path)
    for file in files:
        if (os.path.splitext(file)[1] == ".html"):
            f.write(input_path + '/' + file)
            f.close()
    return output_path + r"/" + output_name


def send_mail_report(title, attach_name="testReport.zip", receiver="qa@126.com"):
    """
    将测试报告发送到邮件
    :param title: 邮件主题
    :param attach_name: 附件名字
    :param receiver:收件人，默认为qa邮件组
    :return:
    """
    sender = config.sender  # 测试报告邮件发件人邮件地址
    server = config.server  # 测试报告邮箱服务器smtp服务器
    username = config.emailusername  # 测试报告邮件发件人邮箱账户
    password = config.emailpassword  # 测试报告邮件发件人邮箱密码

    """获取最新测试报告"""
    report_dir = config.basedir + "/report/"
    html_report = ""
    for root, sub_dirs, files in os.walk(report_dir):
        for file in files:
            if os.path.splitext(file)[1] == ".html":  # 判断该目录下的文件扩展名是否为html
                html_report = file

    # 改变当前的相对路径由 testSuite变更为report,然后压缩report下面的测试报告Report.html文件
    os.chdir(report_dir)
    cwd = os.getcwd()
    print("cwd is:" + cwd)
    zip_report(r"./", './', attach_name)  # 将Report.html文件压缩成.zip文件，存放路径为./report

    """生成邮件的内容"""
    msg = MIMEMultipart()
    msg["subject"] = title
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    with open(os.path.join(report_dir, html_report), 'rb') as f:
        mail_body = f.read()
    html = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg.attach(html)

    """将测试报告压缩文件添加到邮件附件"""
    att = MIMEText(open('./' + attach_name, 'rb').read(), 'base64', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att.add_header("Content-Disposition", "attachment", filename=attach_name)
    msg.attach(att)

    """发送邮件"""
    msg['from'] = sender
    msg['To'] = receiver
    msg['Subject'] = Header(title, 'utf-8')

    smtp_conn = smtplib.SMTP_SSL(server, 465)

    for i in range(10):
        try:
            smtp_conn.login(username, password)
            break
        except Exception as e:
            print(str(e))
            if "authentication failed" in str(e):
                print("连接邮件服务器失败，正在重试第" + str(i + 1) + "次！！！")
            else:
                break

    smtp_conn.sendmail(sender, receiver.split(","), msg.as_string())
    smtp_conn.quit()


def send_mail(title, msg):
    # 发件人
    sender = config.sender
    # 收件人
    receiver = config.receiver
    # smtp服务器
    server = config.server
    # 标题
    title = title
    # 内容
    message = msg
    # 账户
    username = config.emailusername
    # 密码
    password = config.emailpassword

    msg = MIMEText(message)
    msg["Subject"] = title
    msg["From"] = sender
    msg["To"] = receiver
    # 建立连接
    s = smtplib.SMTP_SSL(server)
    # 认证
    s.login(username, password)
    # 发送邮件
    s.sendmail(sender, receiver.split(","), msg.as_string())
    s.quit()
