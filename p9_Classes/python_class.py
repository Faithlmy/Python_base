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


class MyClass():
    """learn  class"""
    i = 2
    def f(self):
        """functions"""
        return 'self3'

x = MyClass()
print(x.i)


print(x.__class__)
print(x.__doc__)
print('='*30)

print(x.f())
print(x.f().__add__('m'))#selfm
print(x.f().__eq__('self'))#true
print(x.f().__format__('s'))
print(x.f().__le__('self'))
print('*'*100)
print(x.f().capitalize())
print(x.f().casefold())
print(x.f().find('t'))
print(x.f().isalnum())
#print(x.f().count(40, '#'))
print(x.f().center(10, '#'))#返回以self为中心的10个宽度的字符（this method returns centerd in a string of length）
print(x.f().isalpha())
print(x.f().casefold())


print(abs(-9))

import os
import sys
import  math