#!/usr/bin/env python
# # -*- coding:utf-8 -*-
# fileName : class_inherite.py
"""
python的单继承
"""

class book(object):
    __author = ''
    __name = ''
    __page = ''

    def __check(self, item):
        if item == '':
            return 0
        else:
            return 1
    def show(self):
        if self.__check(self.__author):
            print(self.__author)
        else:
            print('No value')
        if self.__check(self.__name):
            print(self.__name)
        else:
            print('No value')

    def setname(self, name):
        self.__name = name
    def __init__(self, author, name):
        self.author = author
        self.name = name

class student(book):#继承book类
    __class = ''
    __sname = ''
    __grade = ''

    def showinfo(self):#使用show 方法
        self.show()


if __name__ == '__main__':
    b = student('jack', 'faith')
    b.show()
    b.showinfo()
