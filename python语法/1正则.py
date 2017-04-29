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
        