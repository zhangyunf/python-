#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.text import MIMENonMultipart

sender = '17694839025@163.com'
receviers = '245124085@qq.com'
password = 'QazWsx123'

with open("HTML属性.html", "rb") as file:
    message_body = file.read()

message = MIMEText(message_body, _subtype="html", _charset="utf-8")
message["From"] = formataddr(["发送者", sender])
message["To"] = formataddr(["接受者", receviers])
message["Subject"] = Header("测试报告", "utf-8")

try:
    smtp = smtplib.SMTP("smtp.163.com", port=25)
    smtp.login(sender, password)
    smtp.sendmail(sender, receviers, message.as_string())
except Exception as error:
    print(error)
finally:
    smtp.quit()

