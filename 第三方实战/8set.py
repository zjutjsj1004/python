# https://blog.csdn.net/sunmenggmail/article/details/8546804
# python中set集合如何决定是否重复？

class Item(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar
    
    def __repr__(self):
        return "Item(%s, %s)" % (self.foo, self.bar)
    
    def __eq__(self, other):
        if isinstance(other, Item):
            return ((self.foo == other.foo) and (self.bar == other.bar))
        else:
            return False
    
    def __hash__(self):
        return hash(self.foo + " " + self.bar)
 
print (set([Item('1', '2'), Item('1', '2')]))