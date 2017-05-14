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
  except AttributeError as e:
    print ("Tag was not found")
    return None
  else:
    nameList = bsObj.findAll("span", {"class":"green"}) #因为keyword中的class是python中的关键字，所以我们这里的class需要用引号包起来，https://docs.python.org/3/reference/lexical_analysis.html#keywords
    for name in nameList:
      print (name.get_text)
    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    allText = bsObj.findAll(id="text")
    print(allText[0].get_text())
    return True

title = getTitle("http://www.pythonscraping.com/pages/warandpeace.html")


