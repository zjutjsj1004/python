# -*- coding = utf-8 -*-
#获取https://github.com/phodal 地址的Email:h@phodal.com
# coding:utf-8
#登陆参考：https://segmentfault.com/a/1190000005895018
import requests
from bs4 import BeautifulSoup

USERNAME = 'FizLBQ'
PWD = 'Ll139196'

LoginUrl_GET = 'https://github.com/login'
LoginUrl = 'https://github.com/session'

headers = {
    'Host': 'github.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://github.com',
    'Connection': 'keep-alive',
}

formData = {
    'commit': 'Sign+in',
    'utf8': "✓",
    "login": "XXXXXX",
    "password": "XXXXXX",

}
s = requests.Session()
RESULT = s.get(LoginUrl_GET, headers=headers)


content = RESULT.content

#注意需要进行二级制读写，不然报错：UnicodeDecodeError 'gbk' codec can't decode byte 0x9d in position 1270
with open('login.html', 'wb') as fp:
    fp.write(content)
html = open('login.html', 'rb')
soup = BeautifulSoup(html, "html.parser")
token = soup.find('input', {'name': 'authenticity_token'})['value']
formData['authenticity_token'] = token

# RESULT = s.post(LoginUrl, headers=headers, data=formData,)
RESULT = s.post(LoginUrl, data=formData,)

content=RESULT.content
print (RESULT.url)

print (RESULT.status_code)
print (RESULT.cookies)

with open('bitbucket.html', 'wb') as fp:
    fp.write(content)

print ("```````````````````````````")
#http://blog.csdn.net/boomhankers/article/details/53931614
ss = s.get("https://github.com/phodal", headers=headers)  #注意这里加不加headers=headers效果相同
soupPhodal = BeautifulSoup(ss.text, "html.parser")
print ("--------------------------")
print (soupPhodal.find_all('a')) #找到所有的a标签以及内容
print ("-----------打印出邮箱对应标签所有内容---------------")
print (soupPhodal.find('a', {"class":'u-email'}))
print ("------------打印出邮箱--------------")
print (soupPhodal.find('a', {"class":'u-email'}).get_text()) #打印出邮箱




