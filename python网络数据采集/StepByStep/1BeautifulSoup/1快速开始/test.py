from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc,  "html.parser")

soupPrettofy = soup.prettify()
print(soupPrettofy) #将html进行按照标准的缩进格式的结构输出

#写入文件
'''
output = open('data.html', 'w')
output.write(soupPrettofy)
'''
print (soup.title) #这里不能用soupPrettofy.title，打印title标签和标签里面的内容
print (soup.title.name) #name:打印标签
print (soup.title.string) #string:打印标签内容
print (soup.title.parent.name) #parent:title的父标签

print (soup.p)
print (soup.p["class"]) #第一个标签p中class属性的内容

print ("--------------------------")
print (soup.a)
print ("--------------------------")
print (soup.find_all('a')) #找到所有的a标签以及内容
print ("--------------------------")
print (soup.find_all('p')) #找到所有的p标签以及内容
print ("--------------------------")
print (soup.find(id='link3'))
print (soup.find(href='http://example.com/tillie'))
print ("--------------------------")
#print (soup.find("class"='sister'))  #注意我们不能用这种方式查找
print (soup.find('a', {"class":'sister'})) #BeautifulSoup查找class标签需要用这种方式，同时class需要加上"",这句话是找到第一个a标签，同时class为sister

#从文档中找到所有<a>标签的链接
print ("----------从文档中找到所有<a>标签的链接----------------")
for link in soup.find_all('a'):
    print (link.get('href'))  #这里不能用link.href,这种方式只使用于标签，获取标签属性需要用get
    print (str(link.get('id')) + "&&&" + str(link.get('class'))) #这里不加str进行转换，两个值是不能进行拼接的
    print ((link.get('id')) + "&&&") #这里不加str进行转换，两个值是也可以进行拼接的
    print (type(link.get('id')))

#从文档中获取所有文字内容
print ("----------从文档中获取所有文字内容----------------")
print (soup.get_text())