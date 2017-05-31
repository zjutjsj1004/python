from bs4 import BeautifulSoup

soup = BeautifulSoup(open("index.html"), "lxml")
print (soup)

soup = BeautifulSoup("<html> data </html>", "lxml")
print (soup)

print ("---------------------1---------------------")
soup = BeautifulSoup('<b class="boldest"> Extremely </b>', "lxml")
tag = soup.b
print (tag)
print (tag.name)

tag.name = "blockquote" #修改标签名 -- b修改为blockquote
print (tag) #<blockquote class="boldest"> Extremely </blockquote>
print (soup.b) #None （应该b标签已经修改为blockquote）
print (soup.blockquote)#<blockquote class="boldest"> Extremely </blockquote>
print (soup.blockquote.attrs) #blockquote标签的属性

tag['id'] = 1 #在标签添加一个属性id
print(tag) #<blockquote class="boldest" id="1"> Extremely </blockquote>

print("----------2--------------------")
print (tag.string)
tag.string = 'd'
print (tag.string)
print (tag)
print (soup.name)

print("----------3--------------------")
html_doc = """
<html><head><title>The Dormouse's story</title><titleNo></titleNo></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
soup = BeautifulSoup(html_doc, "lxml")
print (soup.find_all('a'))

print ("----------------4-----------------------")
head_tag = soup.head
print(head_tag)

title_tag = head_tag.contents[0] #得到head_tag下的第一个子节点
print (title_tag)#<title>The Dormouse's story</title>

title_tagNone = head_tag.contents[1]#得到head_tag下的第二个子节点
print (title_tagNone) #<titleno></titleno>

print (title_tag.contents)

 #如果一个指定名字的参数不是搜索内置的参数名,搜索时会把该参数当作指定名字tag的属性来搜索,
 #如果包含一个名字为 id 的参数,Beautiful Soup会搜索每个tag的”id”属性
print (soup.find_all(id='link2'))

print ("----------------5-----------------------")
print (soup.select("title")) #CSS选择器:http://www.w3school.com.cn/cssref/css_selectors.asp


