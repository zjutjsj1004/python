#查找python的request模块(在urllib库里面)，只导入urlopen函数
#学习urllib库:https://docs.python.org/3/library/urllib.html
from urllib.request import urlopen
html = urlopen("http://pythonscraping.com/pages/page1.html")
print(html.read())