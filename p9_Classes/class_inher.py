#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
python的多继承
"""
class A:
    name = 'A'
    __num = 1

    def show(self):
        print(self.name)
        print(self.__num)

    def  setnum(self, num):
        self.__num = num

class B:
    nameb = 'B'
    __numb = 2

    def show(self):
        print(self.nameb)
        print(self.__numb)

    def setnum(self, numb):
        self.__num = numb

class C(A, B):

    def showall(self):
        print(self.name)
        print(self.nameb)


if __name__ == '__main__':
    c = C()
    c.showall()
    c.show()
    c.setnum(90)
    c.show()