#!/usr/bin/env python
# -*- coding:utf-8 -*-
# file: faith_string.py
# """
# 介绍python字符串用法
# """
#
# """===字符串操作====="""
#
#
#
# print('+'*100)
# """===字符串索引和分割====="""
# str = 'abcdefghijklmn'
# print(str[2])
# print(str[3:8])
# print(str[:-2])
#
# print('+'*100)
# """===字符串格式化==="""
# """
# %c 单个字符
# %d 十进制数
# %o 八进制数
# %s 字符串
# %x 十六进制数 （小写字母）
# %X 十六进制数（大写字母）
# """
# s = 'I am %s'
# print(s % 'faith')
#
# s = 'I %s %s hello'
# print(s % ('am', 'faith'))
#
# print('1 %c 1 %c %d' % ('+', '=', 2))
#
# print('c = % X' % 0xa)
#
#
# print('+'*100)
# n = """字符串和\n数字的转换"""
# print(n)
# #print('10' + 4)#TypeError: Can't convert 'int' object to str implicitly
# print(int('10') + 4)
# print('10' + '4')
#
# print('+'*100)
# """原始字符串"""
# import os
# path = r'/home/faith/lmy'
# s = os.listdir(path)
# print(s)
#
# print('='*50)
# """===列表和元组==="""
# list = []
# list.append(1)#向列表里面添加元素
# print(list)
#
# list.count(2)#统计2在列表中出现的次数
#
# list.extend([2, 4, 8, 1, 0])#向列表中田间一个列表
# print(list)
# l = [45, 90]
# list.extend(l)
# print(list)
#
# print(list.index(8))#获取8在列表中的位置
#
# list.insert(5, 100)
# print('100', list)#在3的位置添加100
#
# print(list.pop(2))#删除列表中第2个数
# print(list)
#
# list.remove(1)#删除列表中第一次出现的1
# print(list)
#
# list.remove(1)
# print(list)
#
# list.reverse()#列表倒序
# print(list)
#
# list.sort()#列表成员从新排序
# print(list)
#
# print('='*50)
# """元组"""
# tup = ('a', 'b', 'c', 'd')
# list.insert(3, tup)#列表中插入元组
# print(list)
#
# print('+' * 50)
# """字典"""
# dic = {'apple': 2, 'banana': 1}
# print(dic)
# dic.copy()#复制字典
# print(dic)
#
# dic['tea'] = 5#增加一项到字典中
# print(dic.items())
#
# print(dic.pop('apple'))#删除一项并将值返回
# print(dic)
# print(dic.items())
# print(dic.keys())#获取键的列表
# print(dic.values())#获取值的列表
#
# dic.update({'apple': 9})#更新apple 没有就添加
# print(dic)
#
# dic.clear()#清空字典
# print(dic)
#
# """===================================="""
# print('字符串的拼接')
# print('app' + 'le')#第一种
# f1 = ['a', 'p', 'p', 'l', 'e']
# print(''.join(f1))#第二种
# f2 = ['apple', 'banana']
# print(''.join(f2))
# print('%s%s%s'%('app', 'le', 'banaba'))#第三种
import re

def connstring():
    for i in range(1000000):
        f1 = ['a', 'p', 'p', 'l', 'e']
        ''.join(f1)

def faith_str():
    str = 'hi, P_base!P_base!'
    print(str.capitalize())  # 将首字母大写
    print(str.count('p'))  # 计算p出现的次数
    print(str.count('P_base'))
    print(str.find('i'))  # 字符串中某一个字符串出现的位置
    print(str.isalnum())  # 字符串中是否包含数字
    print(str.isalpha())  # 是否包含字母
    print(str.isdigit())  # 是否仅仅包含数字
    print(str.islower())  # 是否全为小写字母
    print(str.isspace())  # s是否均为空白字符
    print(str.istitle())  # 是否首字母大写
    print(str.isupper())  # 是否均为大写字母
    print('joinmy ', str.join('faith'))  # 连接字符串
    print(str.lower())  # 全部转换为小写字母
    print('split', str.split())  # 分割字符串
    print(str.swapcase())  # 大小写互换
    print(str.title())  # 字符串首字母大写
    print(str.upper())  # 全部转换成大写
    print(len(str))  # 字符串长度

def faith_split():

    """
    three method of spit:
    1. split
    2.splitlines
    3. import re --> re.split()
    :return:
    """
    str = "This is the voa, " \
          "special english health report"

    str1 = '''I have a pen
    I have a apple
apple pen'''

    str4 = """
    I have a pen
    """
    print(str.split()[0], '\n',
          str.split()[1], '\n',
          str.split('is'), '\n',
          str.split(), '\n',
          str.split(' '), '\n',
          str.split(','), '\n',
          )

    str3 = ''.join(str1.split('\n'))# convert list to str
    print(str1, '\n',
          str1.splitlines(), '\n',
          str1.split('\n'), '\n',
          type(str1.split('\n')), '\n',
          type(str), '\n',
          type(str1.split('\n')), '\n',
          type(str3), '\n',
          str3, '\n',
          str3.split(' ')[1], '\n',
          str4.split(), '\n',
          )

    str5 = '1144109319@qq.com'
    print(re.split('@|\.', str5))
    str6 = '10.191.131.11'
    str7 = re.split('\.', str6)
    print(str7)
    print(type(str7))

    for i in str7:
        print(i)


    # print(str8)
    # print(type(str5))
    # print(type(str8))
    # for i in list(str5):
    #     print(i)
def faith_list_foreach():
    """
    three method of foreach
    :return:
    """
    str8 = ['a', 'b', 'c', 'd']
    for i in str8:
        print(i)

    for i, val in enumerate(str8):
        print('number is %s, value is %s'%(i, val))

    print('\n')

    for i in range(len(str8)):
        print('number is %s, value is %s'%(i, str8[i]))


if __name__ == '__main__':
    # connstring()
    # faith_str()
    # faith_split()
    faith_list_foreach()