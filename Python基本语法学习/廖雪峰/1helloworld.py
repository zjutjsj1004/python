print("hello world")

age = input("youe age:")
age = int(age)
if age > 12:
    print("old")
else:
    print("young") 


print('a"a')

print("a'a")

print(r'\t')
print(r"\t")

a = 'ABC'
b = a
a = 'XYZ'
print(b)

print('\u4e2d\u6587')

#Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A'))
print(ord('中'))
print(chr(25991))
print(chr(20013))
print("'\u4e2d\u6587'") #\u4e2d  就是20013的整数编码

print("中文")


#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
testA = ()
if testA:
    print("testA")
else:
    print("no testA")

print(str(hex(121))) #利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串


def FunctionName(args):
    if not isinstance(args, int):
        print ("not int")
        return
    print("FunctionName")

FunctionName('111')
FunctionName(111)


#默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end())


#可变参数:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431752945034eb82ac80a3e64b9bb4929b16eeed1eb9000
def calc(*number):
    sum = 0
    for n in number:
        sum = sum + n
    print(sum)

calc(1,2)
#calc([1,2]) #nsupported operand type(s) for +: 'int' and 'list'
listA = [1,2]
calc(*listA)

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person(1,2)  #name: 1 age: 2 other: {}

#如果要限制关键字参数的名字，就可以用命名关键字参数,命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
def person1(name, age, *, city, job):
    print(name, age, city, job)
person1(1,2, city=1, job=2)

#参数组合  -- 参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。


#f(n) = {
#            1        n = 0
#            n*f(n-1) n > 0
#       }
def fact(n):
    if isinstance(n, int):
        if(n == 0):
            return 1
        else:
            return fact(n - 1) * n
    else:
        return "invalid param"

print(fact(3))
print(fact('3'))


for k in 'ab':
    print("k:%s" % k)

#判断是不是可迭代对象
from collections import Iterable
print( isinstance('abc', Iterable))

#enumerate 下标循环
def testEnumerate():
    for i, value in enumerate(['A', 'B', 'C']):
        print(i, value)
    for x in [(1, 1), (2, 4), (3, 9)]:
        print(x)
testEnumerate()

#列表生成式
print(list(x + 1 for x in range(1, 10)))