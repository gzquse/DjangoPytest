# -*- coding:utf-8 -*-
"""
模块描述:
 解析html网页内容
 beautifulSoup4
作者：Sniper.ZH
"""
import requests
from bs4 import BeautifulSoup

response = requests.get('http://127.0.0.1:8001/login/')

response.encoding = 'utf-8'
# print(response.text)
with open("test_login.html", "wb") as tf:
    tf.write(response.content)

# 第一步安装三方库
# pip install beautifulsoup4
# pip install lxml
# 从html文档中提取数据的一个工具库
# xml html xml的子集
# lxml html.parser

# 第二步 解析文档
soup = BeautifulSoup(open('test_login.html', encoding='utf-8'), features='lxml')

print(type(soup))

# 1.通过tag取元素
# title head
# print(soup.title)
# print(soup.head)
# # 格式化输出
# print(soup.head.prettify())

# print(soup.head.prettify())

# 2.获取元素的文本
# print(soup.title.text)
# print(soup.title.string)

print(soup.title.text)

# text可以获取子元素内部文本，string只能获取当前元素自己的文本
# print(soup.head.text)
# print("-"*30)
# print(soup.head.string)

# 3.获取多个元素文本内容
# tag获取元素的方法，只能获得第一个匹配的元素
# print(soup.head.prettify())

# strings得到一个生成器
# print(soup.head.strings)
# # for s in soup.head.strings:
# for s in soup.head.stripped_strings:
#     print("-"*30)
#     print(s)

# 4.获取元素属性
# print(soup.img)
# print(soup.img.attrs)
# print(soup.img.attrs['src'])

# 5.获取多个元素
# 获取子元素的方法
# for dd in soup.head.contents:
# for dd in soup.head.children:
#     print("-"*30)
#     print(dd)

# contents 和 children
# contents可以用下标获取指定的元素，children不行
# print(type(soup.head.contents))
# print(soup.head.contents[1])
# print(type(soup.head.children[1]))  # 不能用下标

# 6.find find_all
# for div in soup.find_all('div'):
#     print("-" * 30)
#     print(div.prettify())

# for dd in soup.find_all(class_='layui-icon'):
#     print("-" * 30)
#     print(dd.prettify())

# 7 css选择器
for dd in soup.select(".layui-icon"):
    print("-" * 30)
    print(dd.prettify())

# 选择的结果，就算只有一个，也是一个列表
print(soup.select('title')[0])
