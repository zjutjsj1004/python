# -*- coding:UTF-8 -*-
#抓取糗事百科首页文章
#参考博客：http://python.jobbole.com/81351/

import urllib
import urllib2
import sys
import re
type = sys.getfilesystemencoding()
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    #data = response.read()
    #data = data.decode('UTF-8')
    #data = data.encode(type)
    #print data

    content = response.read().decode('UTF-8').encode(type)
    print content
    #if sys.version_info < (3, 4):  #python 判断 :https://segmentfault.com/q/1010000000127878
        #pattern = re.compile('<div class=\"article block untagged mb15\" .*([\x80-\xff]+)')
    #else:
        #pattern = re.compile('<div class=\"article block untagged mb15\" .*([\u4e00-\u9fa5]+)')
    
    pattern = re.compile('<span>(.*?)</span>',re.S)  # re.S(全拼：DOTALL): 点任意匹配模式，改变'.'的行为
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!findall start'
    items = re.findall(pattern,content)
    print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!findall end'
    for item in items:
        #pattern = re.compile('(<br/>)')
        #item = pattern.sub('', item)
        print item
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reson
