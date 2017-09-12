#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
