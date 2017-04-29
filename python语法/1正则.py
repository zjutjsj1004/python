# -*- coding:UTF-8 -*-
#python 正则表达式学习
#参考:http://www.runoob.com/regexp/regexp-syntax.html    (main)
#参考：http://www.runoob.com/python/python-reg-expressions.html
#参考：http://www.jb51.net/article/65286.htm
#参考: http://www.jb51.net/article/50511.htm


import re
import sys
type = sys.getfilesystemencoding()

print (re.match('www', 'www.runoob.com').span()) #不加.span()会返回一直地址
print (re.match('runoob', 'www.runoob.com'))

 
line = "Cats are smarter than dogs"
 
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
 
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"


print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配


phone = "2004-959-559 # 这是一个国外电话号码"
 
# 删除字符串中的 Python注释 
num = re.sub(r'#.*$', "", phone) #美元符号，匹配一个字符串的结尾或者字符串最后面的换行符
print "电话号码是: ", num
 
# 删除非数字(-)的字符串 
num = re.sub(r'\D', "", phone) #\D 非数字
print "电话号码是 : ", num

stringTmp = 'c1212'
items = re.findall(r'[1-9][2-9{0, 1}]', stringTmp)
for item in items:
        print item[0]


test = "<span>上联：光换kindle不读书，穷烧耳机不听歌。"
print test
if sys.version_info < (3, 4):  #python 判断 :https://segmentfault.com/q/1010000000127878
        pattern = re.compile('[\x80-\xff]+')
else:
        pattern = re.compile('[\u4e00-\u9fa5]+')
items = re.findall(pattern,test)
for item in items:
        print item

test = "<a href=\"/article/118941806\" target=\"_blank\" class=\'contentHerf\' ><div class=\"content\"><span>神一般的巧合<br/>一个11朋友11，关系很好，就是那种你一张嘴他就知道你要说啥，好久没联系了，那天跟他聊天，然后他说要不交换qq干和密码玩，我说可以，我的密码是前面几个字母，后面是520，没想到他的秘码是前面是几个字母，后面是1314，突然心里面真的有一种感觉，想要跟他一辈子在一起的的感觉，却迫于某些原因却只能说是真的好巧，心里面那些波涛汹涌的话到嘴边又咽下去。不知道他有没有玩糗百，会不会看见</span></div></a>"
pattern = re.compile('(<br/>)')
test = pattern.sub('', test)
if sys.version_info < (3, 4):  #python 判断 :https://segmentfault.com/q/1010000000127878
        pattern = re.compile('a href="/article/118941806" target="_blank" class=\'contentHerf\' ><div class="content"><span>(.*[\x80-\xff]+)')
else:
        pattern = re.compile('a href="/article/118941806" target="_blank" class=\'contentHerf\' ><div class="content"><span>(.*[\u4e00-\u9fa5]+)')
items = re.findall(pattern, test)
for item in items:
        print item
