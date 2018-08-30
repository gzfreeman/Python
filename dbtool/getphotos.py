# -*- coding: utf-8 -*-

#导入第三方包和模块
import requests
from bs4 import BeautifulSoup
import os

folder = 'test_img'
if not os.path.exists(folder):
    os.makedirs(folder)

def download(url):
    response = requests.get(url)
    name = url.split('/')[-1]
    f = open(folder + '/' + name + '.jpg', 'wb')
    f.write(response.content)
    f.close()

header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

pic_url='http://w3.afulyu.pw/pw/read.php?tid=996883'
resonse_i=requests.get(pic_url,headers = header)

rs=resonse_i.text
soup = BeautifulSoup(rs, 'lxml')
imgs_i = soup.find_all(name='img')

#imgs_i = soup.find_all(id='read_tpc')
#print(imgs_i)
for imgs in imgs_i:
        #img_src = img.get('src')
        if str(imgs.get('src'))[:4] == 'http':
            #print(imgs.get('src'))
            download(imgs.get('src'))