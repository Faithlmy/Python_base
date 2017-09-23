"""=== class ==="""

# def s_test():
#     def do_local():
#         s = 'local spam'
#
#     def do_nonlocal():
#         nonlocal s
#         s = 'nonlocal spam'
#
#     def do_global():
#         global s
#         s = 'global spam'
#
#     s = "test spam"
#     do_local()
#     print("After local assignment:", s)
#     do_nonlocal()
#     print("After nonlocal assignment:", s)
#     do_global()
#     print("After global assignment:", s)
#
# s_test()
# print("In global scope:", s)

"""=== class and property"""
# class MyClass():
#     """learn  class"""
#     i = 2
#     def f(self):
#         """functions"""
#         return 'self3'
#
# x = MyClass()
# print(x.i)
#
#
# print(x.__class__)
# print(x.__doc__)
# print('='*30)
#
# print(x.f())
# print(x.f().__add__('m'))#selfm
# print(x.f().__eq__('self'))#true
# print(x.f().__format__('s'))
# print(x.f().__le__('self'))
# print('*'*100)
# print(x.f().capitalize())
# print(x.f().casefold())
# print(x.f().find('t'))
# print(x.f().isalnum())
# #print(x.f().count(40, '#'))
# print(x.f().center(10, '#'))#返回以self为中心的10个宽度的字符（this method returns centerd in a string of length）
# print(x.f().isalpha())
# print(x.f().casefold())
# print(x.f().__iter__)
# print(x.f().__dict__)

"""calling class"""
# class Animal:
#     kind = 'cat'
#     def __init__(self, name):
#         self.n = name
#
# a = Animal('dog')
# print(a.kind)
# print(a.n)

"""class initialization"""
# class Animal:
#     k = []
#     def __init__(self):
#         pass
#     def addAnimal(self,name):
#         self.k.append(name)
#
# a = Animal()
# a.addAnimal('d')
# print(a.k)

"""call and add member"""
# class Animal:
#     k = []
#     def __init__(self, name):
#         self.n = name
#
#     def addAnimal(self, name):
#         self.k.append(name)
# a = Animal('dog')#TypeError
#
# a.addAnimal('d1')
# a.addAnimal('d2')
# print(a.n)
# print(a.k)

""""===calling function==="""
""""1、注意f2中self的迷惑性，在类C中调用的时候容易犯错
    2、函数不能写在类下面，写类下面报 NameError: name 'f1' is not defined"""

# def f1(x):
#     return x
# def f2(self, y, z):
#     return y+z
#
# class C:
#     f1 = f1(3)
#     #f2 = f2(5, 6)#TypeError: f2() missing 1 required positional argument: 'z'
#     f2 = f2('s', 5, 6)
#     def g(self):
#         return 'hello world'
#
# c = C()
# print(c.f2)
# print(c.f1)
# print(c.g())

"""从fun_class.py中调用函数"""
# from fun_class import fun1
# print(fun1(2))

"""从p8_EAE下的fun2_class.py中调用函数"""
# from p8_EAE.fun2_class import fun2
# print(fun2(3))

"""===python的变量在类中的应用==="""
"""
   1、_xx  是 protected
   2、__xx 是 private
   3、__xx__ 是 特殊变量  用户控制的命名空间内的变量或是属性
"""
# class A:
#     def __init__(self):
#         self.__private()
#         self.public()
#     def __private(self):
#         print('A.__private()')
#     def public(self):
#         a = self.__private()
#         print('A.private()')
#
# class B(A):
#     def __private(self):
#         print('B.__provate()')
#
#     def public(self):
#         print('B.public()')
#
# class C(A):
#     pass
# class D:
#     pass
#
# a = A()
# b = B()
# c = C()
# d = D()
# print('*'*50)
# print(a.public())
# print(b.public())
# print('=====')
# print(b._A__private())
# print(dir(b))
# print(dir(c))
# print(dir(d))

"""类的调用"""
# class A:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         # self.x4=4
#         # self.x5=4
#     def _p(self):#不能调用私有方法
#         sum_p = self.x + self.y
#         return sum_p
#     def p(self):#内部调用，以便外部调用
#         p = self._p()
#         return p
#         #print(p)
#     def __m(self):
#         sum__m = self.x + self.y
#         return sum__m
#     def m(self):
#         m = self.__m()
#         return m
#     def sum(self, x1, x2, x3):
#         s = x1 + x2 + x3
#         #s = self.x4 + self.x5
#         return s
#
# a = A(2,7)
# #a.p()
# #print(a.sum(2,9,4))
# #print(a.p())
# print(a.m())

"""访问私有变量"""
# class per():
#     def __init__(self):
#         self.__name = ''
#         self.__age = ''
#         self.n = 8
#         self._p = 9
#
#     #给私有变量加get set 方法，然后调用
#     def get_name(self):
#         return self.__name
#     def set_name(self, value):
#         self.__name = value
# per = per()
# per.set_name('k')
# print(per.get_name())
# print(per._p)

"""加装饰器访问私有变量"""
# class Person():
#     name = property()
#     age = property()
#     def __init__(self):
#         self.__name = ''
#         self.__age = ''
#     #@name.getter
#     def name(self):
#         return self.__name
#     #@name.setter
#     def name(self,value):
#         self.__name = value
#     #@age.getter
#     def age(self):
#         return self.__age
#     #@age.setter
#     def age(self, value):
#         self.__age = value
# p = Person()
# p.age = 30
# p.name = 'kk'
# print(p.name)
# print(p.age)

"""私有函数中的私有变量"""
class A:
    mp = property()
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def _pro(self):
        self.__mp = ''
        sum_pro = self.x + self.y
        m_p = a.mp
        s_pro = m_p + self.x
        #return sum_pro
        return s_pro, sum_pro
    def pro(self):#私有函数公有化
        p, q = self._pro()
        return p, q
    """#私有变量公有化"""
    def mp(self, v):
        self.__mp = v
    def mp(self):
        tp = self.__mp
        return tp

a = A(9,8)
#print(a.pro())
a.mp = 3
print(a.pro())
