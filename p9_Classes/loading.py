#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
python的重载
"""
class human:
    __age = 0
    __sex = ''
    __heigth = 0
    __weigth = 0
    name = ''

    def __init__(self, age, sex, height, weight):
        self.age = age
        self.sex = sex
        self.heigth = height
        self.weigth = weight

    def setname(self, name):
        self.name = name

    def show(self):
        print(self.name)
        print(self.__age)
        print(self.__sex)
        print(self.__heigth)
        print(self.__weigth)
class student(human):
    __classes = 0
    __grade = 0
    __num = 0

    def __init__(self, classes, grade, num, age, sex, height, weight):#重载
        self.__classes = classes
        self.__grade = grade
        self.__num = num
        human.__init__(self, age, sex, height, weight) #调用human的初始化方法

    def show(self):
        human.show(self)
        print(self.__classes)
        print(self.__grade)
        print(self.__num)

if __name__ == '__main__':
    a = student(12, 3, 20170305, 18, 'male', 175, 65)
    a.setname('faith')
    a.show()