#迭代器

#判断是不是可迭代对象
from collections import Iterable  #可迭代对象：Iterable
from collections import Iterator  #可迭代对象：Iterable
print( isinstance('abc', Iterable))
print( isinstance(iter('abc'), Iterator))