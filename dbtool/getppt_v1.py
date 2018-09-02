# -*- coding: utf-8 -*-

#导入第三方包和模块
import requests
from urllib import request
from bs4 import BeautifulSoup
import os
import re
import random
import datetime

target_url = 'http://www.1ppt.com/moban/jianjie/'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
target_req = request.Request(url = target_url, headers = header)
target_response = request.urlopen(target_req)
target_html = target_response.read().decode('gbk','ignore')
#print(target_html)
listmain_soup = BeautifulSoup(target_html,'lxml')
chapters = listmain_soup.find_all(class_ = 'pages')
#print (type(chapters))


download_soup = BeautifulSoup(str(chapters), 'lxml')
chapters_url=download_soup.find_all('a')
for link in chapters_url:
        download_url = "http://www.1ppt.com/" + link.get('href')
        download_name = link.string
        print(download_name + " : " + download_url)


