#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python的运算符重载
"""

class  Mylist:

    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)

    def __add__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + n

    def __sub__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] - n

    def __mul__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] * n

    def __div__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] / n

    def __mod__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] % n

    def __pow__(self, n):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] ** n

    def __len__(self):
        return len(self.__mylist)

    def show(self):
        print(self.__mylist)


if __name__ == '__main__':
    m = Mylist(1, 2, 3, 4)
    m.show()
    m + 5
    m.show()