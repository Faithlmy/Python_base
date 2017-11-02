"""=======Built in Functions and Example======"""

import python_built_in_source as b
"""===abs()==="""
# print(abs(-5))
# print(abs(-1.0))
# print(abs(-.4))
# print(abs(1-9))
#print(b.abs.__doc__)

"""===all(iterable)=="""

# def bll(iterable):
#     for element in iterable:
#         if not element > 5:
#             return False
#     return True
# aa = bll([10, 20, 30])
# print(aa)

# a = [10, 20, 30]
# a_first = all([ x > 2 for x in a])
# a_second = all([ x > 20 for x in a])
# print(a_first)
# print(a_second)

# print(all ( [ True, True, True ] ))
# print(all ( [ True, True, False ] ))
# print(all ( [ "", "a", "b"]))#False
# print(all ( [ " ", "a", "b"]))#Ture

# def bll(iterable):
#     for element in iterable:
#         if not element.__eq__('n'):
#             return False
#     return True
# aa = bll(['n', 'n', 'n'])
# print(aa)

# aa = ['k', 'n', 'n']
# print( all( [x.__eq__('n') for x in aa]))
# print(any( [x.__eq__('n') for x in aa]))


# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

"""===ascii==="""
# randomList = ['Python', 'Pythön', 5]
# print(ascii(randomList))

"""===bin()==="""
# print(bin(2))
# print(bin(-2))
# print(bin(99999))

"""===callable()==="""
# print(callable(0))
# print(callable('faith'))

# def a_add(a, b):#函数返回True
#     return a + b
# print(callable(a_add))

"""===nested function==="""
# def a_add(a):#函数返回True
#     def a_plus(c):
#         return a+c
#     n = a_plus(a)#调用内部函数，但是不能在外层调用
#     return n
# b = a_add(1)
# print(b)


# def outer(num1):
#     def inner_increment(num1):  # hidden from outer code
#         return num1 + 1
#     num2 = inner_increment(num1)
#     return num1, num2
#
# inner_increment(10)#会报错 name 'inner_increment' is not defined
# a, b = outer(10)
# print(a, b)


# x = 1111111111111111
# def f1():
#     #x=1
#     print('------>f1 ',x)
#     def f2():
#         #x = 2
#         print('---->f2 ',x)
#         def f3():
#             x=3
#             print('-->f3 ',x)
#         f3()
#     f2()
# f1()

# class A:#类 返回TRUE
#     def method(self):
#         return 0
# print(callable(A))
# a = A()
# print(callable(a))#类没有实现__call__, 返回 False

# class B:#类 返回TRUE
#     def __call__(self, *args, **kwargs):
#         return 0
# print(callable(B))
# a = B()
# print(callable(a))#类实现__call__, 返回 True

# class A:#类 返回TRUE
#     def __call__(self, *args, **kwargs):
#         pass
#     def method(self):
#         return 0
# print(callable(A))
# a = A()
# print(callable(a))#类实现__call__, 返回 Ture
# print(callable(a.method()))#返回 False

#print(chr(97))

"""===compile()===="""
"""===complex()===="""

"""===delattr==="""
"""删除类的属性"""
# class Coordinate:
#     x = 3
#     y = 5
#     z = 10
# c = Coordinate()
# print(c.x)
# print(c.y)
# print(c.z)
# print('*'*10)
# delattr(Coordinate,'z')
# print(c.x)
# print(c.y)
# #print(c.z) #AttributeError: 'Coordinate' object has no attribute 'z'

#print(dir())
# class Shape:
#     def __dir__(self):
#         return ['area', 'perimeter']
# #print(dir(Shape))
# print(divmod(2,4))

"""===enumerate()==="""
# s = ['A', 'B', 'C']
# m = list(enumerate(s, 1))
# print(m)

"""===eval()==="""

"""===exec()==="""
# program = 'a = 5\nb=10\nprint("Sum =", a+b)'
# exec(program)

# code = compile('a = 1+9', '<int>', 'exec')
# #code = compile('a = 1+9', '<int>', 'none')
# #ValueError: compile() arg 3 must be 'exec', 'eval' or 'single'
# exec(code)
# print(a)

# program = input('Enter a program:')
# exec(program)

"""===format()==="""
# print("Sammy has {} balloons.".format(5))
# print("Sammy the {1} has a pet {0}!".format("shark", "pilot fish"))
# print("Sammy is a {3}, {2}, and {1} {0}!".format("happy", "smiling", "blue", "shark"))
# print("Sammy the {0} {1} a {pr}.".format("shark", "made", pr = "pull request"))
# print("Sammy ate {0:.3f} percent of a pizza!".format(75.765367))
# print("Sammy has {0:4} red {1:16}!".format(5, "balloons"))
# print("Sammy has {0:<4} red {1:^16}!".format(5, "balloons"))
# print("{:*^20s}".format("Sammy"))
# print("Sammy ate {0:5.0f} percent of a pizza!".format(75.765367))

"""===froznset==="""
"""===getattr==="""
"""===globals==="""
"""===hasatter==="""
"""===hash()==="""
# print(hash('1.0'))
# print(hash('1'))
"""===help==="""
"""===hex==="""
#print(hex(255))
#print('%#x' %255, '%x' %255, '%X' %255)
#print(format(255, '#x'), format(255, 'x'), format(255, 'X'))
#print(f'{255:#x}', f'{255:x}', f'{255:X}')#官网看的但是有误，不知道原因

"""===id==="""
print(id('a'))
print(id('b'))

"""===input==="""
#s = input('--->')
#print(s)

"""===isinstance==="""
import os
print(dir(os))