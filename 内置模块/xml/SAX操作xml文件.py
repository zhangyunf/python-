#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei

'''
sax是一种基于事件驱动的api。
利用sax解析xml文档牵涉到两个部分：解析器和时间处理器。
解析器负责读取xml文档，并向事件处理器发送事件，如元素开始跟元素结束事件。
而事件处理器则负责对事件作出响应，对传递的xml数据进行处理。
1、对大型文件进行处理
2、只需要文件的部分内容，或者只需要从文件中得到特定信息
3、想建立自己的对象模型的时候

'''

from xml.sax import ContentHandler
from xml import sax

class MovieHandler(ContentHandler):

    def __init__(self):
        # 初始化数据，并增加一个当前数据
        self.CurrentData = ""
        self.type = ""
        self.format = ""
        self.year = ""
        self.rating = ""
        self.stars = ""
        self.description = ""

    # 文档启动的时候调用
    def startDocument(self):
        print("xml开始解析中")

    # 元素开始事件处理
    def startElement(self, name, attrs):
        self.CurrentData = name
        if self.CurrentData == "movie":
            print("----------movie--------")
            title = attrs["title"]
            print("Title:{0}".format(title))

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "type":
            self.type = content
        elif self.CurrentData == "format":
            self.format = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "rating":
            self.rating = content
        elif self.CurrentData == "stars":
            self.stars = content
        elif self.CurrentData == "description":
            self.description = content

    # 元素结束事件处理
    def endElement(self, name):
        if self.CurrentData == 'type':
            print('Type:{0}'.format(self.type))
        elif self.CurrentData == 'format':
            print('Format:{0}'.format(self.format))
        elif self.CurrentData == 'year':
            print('Year:{0}'.format(self.year))
        elif self.CurrentData == 'rating':
            print('Rating:{0}'.format(self.rating))
        elif self.CurrentData == 'stars':
            print('Stars:{0}'.format(self.stars))
        elif self.CurrentData == 'description':
            print('Description:{0}'.format(self.description))
        self.CurrentData = ""

    # 文档结束的时候调用
    def endDocument(self):
        print('XML文档解析结束!')

if __name__=='__main__':

    handler = MovieHandler()
    parser = sax.make_parser()
    # parser.setFeature(sax.handler.feature_namespaces, 0)
    parser.setContentHandler(handler)
    parser.parse("sax_test.xml")

