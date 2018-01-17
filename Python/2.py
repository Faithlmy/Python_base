#!/usr/bin/python3
# -*- coding: UTF-8 -*-
print("======comper=======")
while True:
    try:
        age = int(input("your dogs age: "))
        print(" ")
        if age < 0: 
            print("你是在逗我吧!") 
        elif age == 1: 
            print("相当于 14 岁的人。") 
        elif age == 2: 
            print("相当于 22 岁的人。") 
        elif age > 2: 
            human = 22 + (age -2)*5 
            print("对应人类年龄: ", human) 
    except ValueError: 
        print("error")
### 退出提示
input("点击 enter 键退出")