#参考:https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431864715651c99511036d884cf1b399e65ae0d27f7e000

class Student(object):
    #__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
    #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
    sName = "定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到"
    def __init__(self, name, score):   #注意：特殊方法“init”前后有两个下划线！！！
        self.name = name
        self.score = score