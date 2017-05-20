from urllib.request import urlopen
from bs4 import BeautifulSoup

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print (textPage.read())

print ("-----------------------------1111111---------------------------------------------")

textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print (textPage.read(), 'UTF-8')


print ("----------------------------22222222----------------------------------------------")
html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "lxml")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
print (content)