from urllib.request import urlopen
from bs4 import BeautifulSoup
def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e: #如果urlope错误就返回HTTP错误代码，程序就会显示错误内容
    print (e)
    return None
  try:
    #如果服务器不存在， html 就是一个 None 对象， html.read() 就会抛出AttributeError 
    bsObj = BeautifulSoup(html.read(), "html.parser")
    title = bsObj.rrrr.rr
  except AttributeError as e:
    print ("Tag was not found")
    return None
  else:
    print (title)
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print ("title cound not ne found")
else:
  print (title)


