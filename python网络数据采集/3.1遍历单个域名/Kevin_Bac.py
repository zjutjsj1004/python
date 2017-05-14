#regex
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getTitle(url):
  try:
    html = urlopen(url)
  except HTTPError as e: #如果urlope错误就返回HTTP错误代码，程序就会显示错误内容
    print (e)
    return None
  try:
    #如果服务器不存在， html 就是一个 None 对象， html.read() 就会抛出AttributeError 
    bsObj = BeautifulSoup(html.read(), "html.parser")
  except AttributeError as e:
    print ("Tag was not found")
    return None
  else:
    links = bsObj.find("div", {"id":"bodyContent"})
    childs = links.findAll("a", href = re.compile("^(/wiki/)((?!:).)*$"))
    for child in childs:
      if 'href' in child.attrs:
        print (child.attrs['href'])
    return True

title = getTitle("https://en.wikipedia.org/wiki/Kevin_Bacon")


