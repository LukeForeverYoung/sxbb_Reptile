from functools import reduce

# coding=utf-8

# urllib模块提供了读取Web页面数据的接口
import urllib

# re模块主要包含了正则表达式

import  xml.dom.minidom
from lxml import etree
from pip._vendor import requests
import sys
from bs4 import BeautifulSoup
import json
pre='https://ow365.cn/img/'
html_str=requests.get('https://sxbb.me/O7R9n').text
soup=BeautifulSoup(html_str)
iframe=soup.find_all('iframe')[0]
fra_url=iframe['src']

html_str=requests.get(fra_url).text
soup=BeautifulSoup(html_str)
#print(soup.prettify())
Url_value=soup.find_all(id='Url')[0]['value']
Img_value=soup.find_all(id='Img')[0]['value']
Vid_value=soup.find_all(id='VID')[0]['value']
print(Url_value)
print(Img_value)
print(Vid_value)
for i in range(0,45):
    receive = requests.get('https://ow365.cn/pdf/GetNextPage/?f='+Url_value+'&img='+Img_value+'&isMobile=false&isNet=True&vid='+Vid_value)
    #soup=BeautifulSoup(receive)
    next_id = json.loads(receive.text)["NextPage"]
    headers = { 'Host':'ow365.cn',
                'Connection':'keep-alive',
                'Cache-Control':'no-cache',
                'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                'DNT':'1',
                'Referer': 'https://ow365.cn/pdf/'+Url_value,
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh,zh-CN;q=0.9,zh-HK;q=0.8,zh-TW;q=0.7'
    }
    now_img=requests.get('https://ow365.cn/img/?img='+next_id,headers=headers)
    print(now_img.content)
    f = open(str(i)+'.gif','wb')
    f.write(now_img.content)
    f.close()
    Img_value=next_id