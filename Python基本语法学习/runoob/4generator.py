''' http://www.runoob.com/python3/python3-iterator-generator.html
在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行 next()方法时从当前位置继续运行。
'''

#python调试配置:http://jingyan.baidu.com/article/00a07f38503a2b82d028dc26.html
import sys

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
        print("count:", counter)
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
var = 0 
while True:
    var = var + 1
    print(var)
    try:
        print (next(f), end=" ")
    except StopIteration:
        print("StopIteration")
        sys.exit()
    except:
        print("except")
        sys.exit()