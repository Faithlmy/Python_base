"""python的io"""

"""=============repr的用法==================="""
"""A"""
# x = 20*10
# y = 3*1.9
# print('x is ' + repr(x) + ',  y is ' + repr(y))

"""B"""
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
#     #end=' '不加end，将会出现显示不整齐，切end可以控制输出的间隔"
#     print(repr(x).rjust(1), repr(x*x).rjust(2), repr(x*x*x).rjust(3),end=' ')
#     print(repr(x*x*x*x).rjust(4))

"""C <--- .formt的用法 --->"""
# # for x in range(1, 11):
# #     #d用来控制间隔
# #     print('{0:2d},{1:3d},{2:5d}'.format(x, x*x, x*x*x))
# print('{0} and {1}'.format('A', 'B'))
# print('{1} and {0}'.format('A', 'B'))

# #下面这种写法将会报SyntaxError
# #print('{1} and {0} and {3}'.format('A', 'B', 'C'))
# #Syntax rules: print('{a1}{a2}{a3}'.format(a1='', a2='', a3=''))
# print('{1} and {0} or {d}'.format('A', 'B', d='C'))
# print('{a1}{a2}{a3}'.format(a1='A', a2='B', a3='C'))
# print('{a2}{a3}{a1}'.format(a1='A', a2='B', a3='C'))

#这条命令有误
import math
print('{0:.3f}.'.format(math.pi))

#
tab = {'sj': 40, 'ax': 30, 'bv': 90}
for m, n in tab.items():
    print('{0:2} ==> {1:5}'.format(m, n))
    print('{0:2} ==> {1:5d}'.format(m, n))
    # #以下两种或报ValueError
    # print('{0:2d} ==> {1:5d}'.format(m, n))
    # print('{0:2d} ==> {1:5}'.format(m, n))

"""D <--- str.rjust() ---> """
# s = 'this'
# print(s.rjust(3, '#'))
# print(s.rjust(5, '#'))
# print(s.rjust(10, '#'))

