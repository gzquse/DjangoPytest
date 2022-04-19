# -*- coding:utf-8 -*-
"""
模块描述:
 实战，解析猫眼电影网页数据
作者：Sniper.ZH
"""
import requests
from bs4 import BeautifulSoup

url = 'https://www.maoyan.com/films?showType=2'
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Cookie": "_lxsdk_cuid=1802731cf529c-0025303556276e-35736a03-384000-1802731cf53c8; uuid_n_v=v1; uuid=D3B70700BBCD11EC9E7A2BC5FC6F637BAB6F92F9988E479DABF2733260028CC0; _lxsdk=D3B70700BBCD11EC9E7A2BC5FC6F637BAB6F92F9988E479DABF2733260028CC0; _csrf=6a8f1c1f250e54c343292b6fe7358760106a9dd3cd59781f8b82bc0e67c69cc5; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1649925018; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1649925352; __mta=174388125.1649925020550.1649925350907.1649925352500.13; _lxsdk_s=1802731cf53-da4-ca4-98%7C%7C51"
}
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
# print(response.status_code)
# print(response.text)
# with open("maoyan.html", "wb") as wf:
#     wf.write(response.content)

# soup = BeautifulSoup(open("maoyan.html", encoding='utf-8'), features="lxml")
soup = BeautifulSoup(response.text, features="lxml")
# 解析标签区域
tags_div = soup.find(class_='tags-panel')
for line in tags_div.find_all(class_='tags-lines'):
    print(line.find(class_='tags-title').text)
    for a_tag in line.find_all("a"):
        print(a_tag.text, end=" ")
    print()

# 解析电影内容
movies_div = soup.find(class_='movie-list')

for dd in movies_div.select("dd"):
    print("-"*50)
    # print(dd.prettify())
    print("电影名字:", dd.find("span", class_="name").text)
    for hover in dd.find(class_='movie-item-hover').find_all(class_='movie-hover-title'):
        tag = hover.find(class_='hover-tag')
        if tag:
            print(hover.find(class_='hover-tag').text, end=" ")
            print(hover.contents[2].strip())

    print("图片:", dd.find("img", class_='movie-hover-img').attrs['src'])

# 正则表达式
