#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""#函数"""
#语法：
def fun(str):
    print(str)
    return
#调用函数，函数的参数不能为空，为空将会报错
fun("hello")
fun(str="meng")


"""传可变对象"""
# 可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1, 2, 3, 4]);
    print("函数内取值: ", mylist)
    return


# 调用changeme函数
mylist = [10, 20, 30];
changeme(mylist);
print("函数外取值: ", mylist)


"""#不定长参数"""
def p( arg1, *arg2):
    print("输出：")
    print(arg1)
    for a in arg2:
        print(a)
    return
p(3)
p(10,90,23)#自动匹配for


"""#匿名函数："""
#1、 lambda只是一个表达式，函数体比def简单很多。
#2、 lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
#3、 lambda函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
#4、 虽然lambda函数看起来只能写一行，却不等同于C或C + +的内联函数，后者的目的是调用小函数
#    时不占用栈内存从而增加运行效率。

s = lambda a1, a2: a1 + a2
print(s(12, 90))


"""列表翻转"""
# #翻转1
# def reverse(li):
#     for i in range(0, len(li)/2):
#         temp = li[i]
#         li[i] = li[-i-1]
#         li[-i-1] = temp
#
# m = [1, 2, 3, 4, 5]
# reverse(m)
# print(m)
#
# #翻转2
# def reverse(ListInput):
#     RevList=[]
#     for i in range (len(ListInput)):
#         RevList.append(ListInput.pop())
#     return RevList
#
# #简化翻转
# def reverse(li):
#     for i in range(0, len(li)/2):
#         li[i], li[-i - 1] = li[-i - 1], li[i]
# l = [1, 2, 3, 4, 5]
# reverse(l)
# print(l)