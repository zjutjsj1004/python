#列表生成式
print(list(x + 1 for x in range(1, 10)))

#要创建一个generator(生成器)，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
L = [x * x for x in range(10)] #list
print (L)

g = (x * x for x in range(10)) #generator(生成器)
print (next(g))
print (next(g))

for x in g:
    print(x, end=" ")

print("", end='\n')
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
g = odd()
next(g)
next(g)


#把函数改成generator(生成器)后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代
def fibgenerator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

for n in fibgenerator(6):
    print(n)