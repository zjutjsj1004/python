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
    data = response.read()
    data = data.decode('UTF-8')
    data = data.encode(type)
    print data


except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reson
