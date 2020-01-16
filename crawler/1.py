# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
import sys
import importlib
importlib.reload(sys)
from bs4 import BeautifulSoup
import urllib.request
import requests

# url = 'http://www.022003.com/2_2447/973175.html'
def parse(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'}

    #urllib解析
    # url = urllib.request.Request(url=url, headers=headers)
    # page = urllib.request.urlopen(url)
    # html = page.read()


    #request解析
    html = requests.get(url, headers=headers)
    html = html.content.decode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    temp = soup.prettify()
    # print(temp)
    return soup
def next_url(url):
    tmp = str(parse(url))
    # res = re.compile(r'<a href *= *"(.*)">[\u4e00-\u9fa5]+')
    # res = re.compile('<a href = "(.*).html')
    res = re.compile('<a href="(/[0-9]*_[0-9]*/[0-9]*.html)')
    next_page = res.findall(tmp)
    # print(next_page[1])
    return next_page[1]


def resolve(url):
    soup = parse(url)
#    res = soup.find(id="content").get_text()
    print(soup.find('div', "xs-details-content").get_text())
    res = soup.find('div', "xs-details-content").get_text()
    print(res)
##    content = soup.find_all('div' class="xs-details-content text-xs")
    find_title = re.compile(r'<h1>(.*?)</h1>')
    title = find_title.findall(str(soup))
    print(title)
#    res = res.replace('请记住本书首发域名：www.022003.com。VIP中文_笔趣阁手机版阅读网址：m.022003.com','')
#    print('正在下载' + '\t' + title[0].replace("正文",''))
#    return title[0].replace("正文",'') + '\n' + res +'\n'
    return res


def download(url):
    for i in range(50):
        with open(r'C:\article2.txt', 'a', encoding='utf-8') as f:
            f.write(resolve(url))
        url = 'http://www.184ku.com' + next_url(url)

url = 'https://www.184ku.com/h0415/novel2/112116.htm'
print(resolve(url))
#download(url)