# -*- coding: utf-8 -*-

#导入第三方包和模块
import requests
from bs4 import BeautifulSoup
import os
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())
folder = 'test_img'
pic_url='http://www.1ppt.com'
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
if not os.path.exists(folder):
    os.makedirs(folder)

def getLinks(articleUrl):
    html_ppt = requests.get(pic_url+articleUrl,headers=header)
    bsObj = BeautifulSoup(html_ppt.text, "lxml")
    ppturl = bsObj.findAll(href=re.compile("^(/moban/)"))
    return  ppturl
    #for link in ppturl:
        #print (link.get('href'))



#getLinks('http://www.1ppt.com/')
links = getLinks("")
for channel_url in links:
    print(channel_url)
#while len(links) > 0:
  #newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
  #if newArticle not in pages:
    #print(newArticle)
    #pages.add(newArticle)
    #links = getLinks(newArticle)

def download(url):
    response = requests.get(url)
    name = url.split('/')[-1]
    f = open(folder + '/' + name + '.jpg', 'wb')
    f.write(response.content)
    f.close()


#print(imgs_i)
#for imgs in imgs_i:
        #img_src = img.get('src')
        #if str(imgs.get('a'))[:4] == 'http':

            #print(pic_url+imgs.get('href'))
            #download(imgs.get('src'))