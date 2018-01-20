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

#当前版本所有关键字
import keyword
print(keyword.kwlist)

#数据类型<3>
#数值运算
print(5 + 8)
print(4.3 - 6)
print(3 * 8)
print(3 / 7)
print(17 % 3)
print(2 ** 5)

#字符串
s = 'Yes,he doesn\'t'
print(s,"\n", type(s), "\n", len(s))

#防止转义
print('C:\some\name')
print(r'C:\some\name')

#字符串的相加 以及 chengfang
print('str'+'ing'," \n", 'my'*3)

#python的切片：与C字符串不同的是，Python字符串不能被改变。
# 向一个索引位置赋值，比如word[0] = 'm'会导致错误。

word = 'ilovepython'
print(word[ 1 : 5])
print(word[ 5 : ])
print(word[ -10 : -6 ])

#列表
a = ['him', 25, 100, 'her']
print(a)

#相加
b = [1, 2, 3]
c = [8, 9]
print(b + c)

#支持切片操作
s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s[0] = 77
print(s)
s[2 : 5] = [45, 89]
print(s)



#元组：
a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))