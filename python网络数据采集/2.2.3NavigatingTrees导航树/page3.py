#处理子标签和其他后代标签
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
    #descendants和children 区别：http://blog.csdn.net/sodaoo/article/details/70230128
    childs = bsObj.find("table", {"id":"giftList"}).children  #children 只能输出直接子节点
    for child in childs:
      print (child)
    print ("1!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    childs = bsObj.find("table", {"id":"giftList"}).descendants #descendants 输出直接子节点和直接子节点下的子节点，以此类推，也就是直接子节点下的所有节点
    for child in childs:
      print (child)
    print ("2!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    childs = bsObj.find("table", {"id":"giftList"}).tr.next_siblings  #next_siblings:处理兄弟标签，下面就是输出所有产品行
    for child in childs:
      print (child)
    return True

title = getTitle("http://www.pythonscraping.com/pages/page3.html")


