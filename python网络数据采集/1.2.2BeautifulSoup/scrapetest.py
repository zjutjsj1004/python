from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
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

#下面三者产生的结果一样的
print(bsObj.h1)
print(bsObj.html.body.h1)
print(bsObj.html.h1)