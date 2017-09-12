#!/usr/bin/python
# -*- coding: UTF-8 -*-

#脚本程序标记号码 <1、2、3>注意和文档中对比

#直接输出：
print("hello,世界");

#python的一种输出：
import sys
x = "faith"
sys.stdout.write(x + '\n')


#Python的变量：<1>
x = 4
y = 5
print("x = ", x)
print("y = ", y)
d1 = id(x)
d2 = id(y)
print("x的id=", d1) # x的id= 1747109648
print("y的id=", d2) # y的id= 1747109680

print("x和y交换后")
x = y
d3 = id(x)
d4 = id(y)
print("x的id=", d3) # x的id= 1747109680
print("y的id=", d4) # y的id= 1747109680


#变量作用域：<2>
c = 5
print(c)
def s():
    c = 6
    print(c)
s()
print(c)#结果是5 6 5

while True:
    newvar = 8
    print(newvar)
    break;
print(newvar)
try:
    newlocal = 7
    raise Exception
except:
    print(newlocal)  # 结果是： 8 8 7


def scopetest():
    var = 6;
    print(var)
var = 5
print(var)
scopetest()
print(var)# 5 6 5


def scopetest():
    global var
    var = 6;
    print(var)  #
var = 5
print(var)
scopetest()
print(var)# 5 6 6


def scopetest():
    var = 6;
    print(var)  #

    def innerFunc():
        print(var)  # look here

    innerFunc()
var = 5
print(var)
scopetest()
print(var)  #5 6 6 5