"""
1、 加 __all__ = ()后，限制其他文件对对象的调用
2、 __fun3()也可以被调用
"""

# __all__ = ('A', 'fun2_n', '__fun3_n')
__all__ = ['A', 'fun2_n', '__fun3_n', '_fun4_n']
class A():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class B():
    def __init__(self, name, id):
        self.name = name
        self.id = id

def fun1_n():
    print('faith')
def fun2_n():
    print('vic')
def __fun3_n():
    print('my__fun3()');
def _fun4_n():
    print('90')