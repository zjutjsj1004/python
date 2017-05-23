#获取https://github.com/phodal 地址的Email:h@phodal.com
#注意点:
#1、我们在网页看到的邮箱，看源码以后发现是UNICODE编码格式
#2、Email格式
'''
    body
      DIV
      DIV
      DIV
      DIV role="main"
        DIV id="js-pjax-container"
          DIV class="container-lg clearfix px-3 mt-4"
           DIV class="col-3 float-left pr-3"
            <ul> class="vcard-details border-top border-gray-light py-3"
              <li>
              <li>
              <li>
                <a>
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("https://github.com/phodal")
bsObj = BeautifulSoup(html.read(), "html.parser")#
#bsObj = BeautifulSoup(html.read())
'''
不加"html.parser"会存在警告:UserWarning: No parser was explicitly specified, so I'm using the bes
t available HTML parser for this system ("html.parser"). This usually isn't a problem, but if you run this code on anoth
er system, or in a different virtual environment, it may use a different parser and behave differently.

The code that caused this warning is on line 4 of the file .\scrapetest.py. To get rid of this warning, change code that
 looks like this:

 BeautifulSoup(YOUR_MARKUP})

to this:

 BeautifulSoup(YOUR_MARKUP, "html.parser")

  markup_type=markup_type))
  '''


parse = bsObj.findAll(href='h@phodal.com')
##print (bsObj)
#parse = bsObj.findAll(re.compile('^svg'), attrs={"itemprop":"email"})

print (parse)


