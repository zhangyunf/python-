#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart# 添加附件

# 发送纯文本电子邮件
sender = '17694839025@163.com'
receviers = '245124085@qq.com'
password = 'QazWsx123'

message = MIMEMultipart()
message["From"] = formataddr(["发送者", sender])
message["To"] = formataddr(["接受者", receviers])
message["Subject"] = Header("添加附件邮件", "utf-8")
# 邮件的正文内容
message.attach(MIMEText("正文", "plain", "utf-8"))
# 构建邮件附件
att1 = MIMEText(open("知识点.txt").read(), "base64", 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 解决中文乱码
att1.add_header("Content-Dispositon", 'attachment', filename=('utf-8', '', "知识点.txt"))
# att1["Content-Disposition"] = 'attachment; filename="知识点.txt"'
message.attach(att1)

smtp = smtplib.SMTP("smtp.163.com", port=25)
smtp.login(user=sender, password=password)
smtp.sendmail(sender, receviers, message.as_string())