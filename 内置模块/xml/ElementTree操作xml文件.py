#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:ZhangYunFei
'''
xml所包含的元素类型
1.标签:<tag>
2.属性:<tag name="attribute">
3.数据<data>1<data>

读取
tree = ET.parse("path")

获取根节点
root = tree.getroot()

查找
element = root.iter("tag")# iter可以罗列该节点所包含的所有其他节点
element = root.findall("country")# findall只能用来查找直接子元素
element = root.find("tag")# 查找为tag的第一个直接子元素

方位Element的标签、属性、值
tag = element.tag
attrib = element.attrib
value = element.text
'''
import xml.etree.ElementTree as ET

# 从变量读取，参数为xml段，返回的是一个Element对象
# root = ET.fromstring(count_data_as_string)

# 打开xml文件,并读取
tree = ET.parse("a.xml")
# 获取根节点
root = tree.getroot()
print(root.attrib)

# 遍历xml文档
for child in root:
    print(root.tag, child.attrib)

    for i in child:
        print(i.tag, i.text)

# 只遍历year节点
for node in root.iter("year"):
    print(node.tag, node.text)


# 创建xml文件
# 创建根节点
a = ET.Element("root")

# 创建子节点，并添加属性
b = ET.SubElement(a, "sub1")
b.attrib = {"name": "name attribute"}

# 创建子节点，并添加数据
c = ET.SubElement(a, "sub2")
c.text = "test"

# 创建elementtree 文件对象，并写入
tree_txt = ET.ElementTree(a)
tree_txt.write("test.xml")

'''
修改xml文件
ElementTree.write("xmlfile")# 更新xml文件
Element.append()# 为当前element对象添加子元素
Element.set(key,value)# 为当前element的key属性设置value值
Element.remove(element)# 删除为element的节点
'''

# 读取待修改的文件
updateTree = ET.parse("test.xml")
root = updateTree.getroot()

# 创建新节点并添加为root的子节点
newEle = ET.Element("NewElement")
newEle.attrib = {"name": "NewElement", "age": "20"}
newEle.text = "This is a new element"
root.append(newEle)

# 修改sub1的name属性
sub1 = root.find("sub1")
sub1.set("name", "New Name")

# 修改sub2的数据值
sub2 = root.find("sub2")
sub2.text = "New Value"

# 写回源文件
updateTree.write("test.xml")
