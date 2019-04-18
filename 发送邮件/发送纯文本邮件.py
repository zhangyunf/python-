#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import smtplib
from email.mime.text import MIMEText# 设置文件内容以及格式
from email.header import Header#
from email.utils import formataddr

# 发送纯文本电子邮件
sender = '17694839025@163.com'
receviers = '245124085@qq.com'
password = 'QazWsx123'
# 设置邮件内容：第一个参数邮件正文文本内容，第二个参数plain 设置文本格式， 第三个utf-8设置编码
message = MIMEText('纯文本测试邮件', 'plain', 'utf-8')
message['From'] = formataddr(["测试", sender])# 发送者名称
message["To"] = formataddr(["接受者", receviers])# 接受者
subject = "测试"# 主题
message["Subject"] = Header(subject, "utf-8")# 邮件主题
smtp = smtplib.SMTP(host="smtp.163.com", port=25)
smtp.login(sender, password)
smtp.sendmail(sender, receviers, message.as_string())# 发送邮件






