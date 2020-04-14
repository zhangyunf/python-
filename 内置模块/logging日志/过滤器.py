#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
import logging

logger_one = logging.getLogger('one')
logger_one.setLevel(logging.INFO)
logger_two = logging.getLogger('one.two')
logger_two.setLevel(logging.INFO)


formatter_one = logging.Formatter('%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter_one)
fil = logging.Filter(name='one.two')
handler.addFilter(fil)

logger_one.addHandler(handler)
logger_two.addFilter(handler)

logger_one.info('你好')
logger_two.info('hello world')
