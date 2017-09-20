"""list.append"""

#list操作（11个）
f = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(f.count('banana'))
# #f.append('pp')
# f[len(f) : ] = ['hello']#和f.append()的效果一样
# #f.insert(3, 'banana')
# #f.extend('meng')
# f[len(f):] = 'yao '#和f.extend('yao')一样
# f.remove('y')
#f.pop(3)
#f.clear()
#del f[:]
#f.index('meng', 4)
#print(f)


"""stacks."""
# s = [3, 4, 5]
# s.append(6)
# print(s)
# s.append(7)
# print(s)
#
# print(s.pop())#删除最新的一个元素，或者指定一个位置上的元素
# print(s.pop(2))
# print(s)
# s.insert(3, 9)#添加指定位置的元素
# print(s)
# s.insert(6, 100)
# print(s)
# s.insert(1, 200)
# print(s)
"""=================================================================================="""

"""Queues"""
# from collections import deque
# q = deque(["A", "B", "C"])
# q.append("D")
# print(q)
# print(q.popleft())


"""求平方或者立方"""
# sq = []
# for x in range(10):
#     sq.append(x ** 3)
# print(sq)
#
# sq = list(map(lambda x: x**3, range(10)))
# print(sq)
#
# sq = [x**2 for x in range(10)]
# print(sq)

"""组合"""
# c = []
# for i in range(4):
#     for j in range(2):
#         if i != j:
#             c.append((i, j))
# print(c)


"""求平方, [里面直接计算]"""
# s = [-6, -5, -2, 0, 1, 3]
# print([x ** 2 for x in s])
#
# print('*'*9)
# print([x ** 2  for x in range(5)])

"""拆开"""
# vec = [[1,2,3], [4,5,6], [7,8,9]]
# print([num for elem in vec for num in elem])

"""pi的演示"""
# from math import pi
# cc = [str(round(pi, i)) for i in range(0,3)]
# print(cc)

"""==========================================================================="""
"""矩阵的表示1"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# m = [[row[i] for row in matrix] for i in range(4)]
# print(m)

"""矩阵的表示2"""
# t = []
# for i in range(4):
#     t.append([row[i] for row in matrix])
# print(t)

"""矩阵表示3"""
#print(list(zip(*matrix)))

"""==================================================================================="""
"""del用法"""
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# #del a[2:4]
# #del a[:]
# print(a)

"""================================================================================================"""
"""元组"""
# tup = 23, 34, 45, 'faith'
# print(tup)
# u = tup, (12, 13, 14)
# print(u)

"""借用上面的元组，测试in的用法"""
# print(23 in tup)#T
# print((23, 34, 45) in tup)#F
# print((23, 34, 45, 'faith') in u)#T
# print((23, 34, 45, 'faith') in tup)#F
# print(tup in u)#T
# print(100 in tup)#F

"""set配合 逻辑运算符的用法"""
#set会自动过滤字符串里面重复的字符，并无序输出
#没有a+b
# a = set('abbgkk')
# b = set('aabccd')
# print(a)
# print(b)
# print(a - b)
# print(a | b)#相当于a+b
# print(a & b)
# print(a ^ b)
#
# nt = {x for x in b if x not in 'abc'}
# print(nt)
"""======================================================================================================"""
"""字典"""
"""first"""
#tel = {'c': 3, 'a': 1, 'd': 4, 'b': 2, }
# print(tel)
# print(tel.keys())
# print(tel.pop('a'))#移除a，并将1返回
# print(sorted(tel.keys()))
# print(sorted(tel.values()))

"""second"""
# tel['f'] = 5#添加f
# print(tel)
# del tel['b']#移除b
# print(tel)

"""dictionaries的4种表示，自己感觉第3种有点麻烦"""
#  1
#print({x: x ** 2 for x in range(5)})
#x下面这两种写法会报语法错误
#print([x, x ** 2 for x in range(5)])
#print([x: x ** 2 for x in range(5)])

#  2
# dt = dict(z = 26, x = 24, w = 23, y = 25)#字典的顺序不同
# print(dt)

# 3
# d3 = dict([('m', 3), ('n', 4), ('k', 7)])
# print(d3)

#  4  最开始就用了

"""==================================================================================================="""
"""looping 技巧"""
# kdict = tel = {'c': 3, 'a': 1, 'd': 4, 'b': 2, }
# for x, y in kdict.items():
#     print(x, y)
#
# for i, j in enumerate(['ta', 'tb', 'tc']):
#     print(i, j)

"""zip的表演"""
# questions = ['name', 'quest', 'favorite color']
# answers = ['lancelot', 'the holy grail', 'blue']
# for q, a in zip(questions, answers):
#     print('what is your {0}?  It is {1}.'.format(q, a))

"""reversed"""
# for i in reversed(range(1, 10, 2)):
#     print(i)

"""sorted"""
# a = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(a):
#     print(i)

"""looping create new list"""
# import math
# rd = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# fd = []
# for v in rd:
#     if not  math.isnan(v):
#         fd.append(v)
# print(fd)

"""=====  5.7  more on conditions  ======"""
""" 1、 or 输出or串从左到右第一个非空字符"""
s1, s2, s3, s4 = '', 'a', 'k', 's',
n = s3 or s2 or s4
m = s1 or s2 or s4
print(n)
print(m)