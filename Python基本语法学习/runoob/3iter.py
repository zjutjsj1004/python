#参考；http://www.runoob.com/python3/python3-iterator-generator.html
list = [1,2,3,4]
it = iter(list)# 创建迭代器对象
print(it)
print(next(it))# 输出迭代器的下一个元素
print(next(it))
