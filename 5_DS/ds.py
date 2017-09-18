
"""stacks"""
s = [3, 4, 5]
s.append(6)
print(s)
s.append(7)
print(s)

print(s.pop())#删除最新的一个元素，或者指定一个位置上的元素
print(s.pop(2))
print(s)
s.insert(3, 9)#添加指定位置的元素
print(s)
s.insert(6, 100)
print(s)
s.insert(1, 200)
print(s)


"""Queues"""
from collections import deque
q = deque(["A", "B", "C"])
q.append("D")
print(q)
print(q.popleft())


"""求平方或者立方"""
sq = []
for x in range(10):
    sq.append(x ** 3)
print(sq)

sq = list(map(lambda x: x**3, range(10)))
print(sq)

sq = [x**2 for x in range(10)]
print(sq)

"""组合"""
c = []
for i in range(4):
    for j in range(2):
        if i != j:
            c.append((i, j))
print(c)


"""求平方, [里面直接计算]"""
s = [-6, -5, -2, 0, 1, 3]
print([x ** 2 for x in s])

print('*'*9)
print([x ** 2  for x in range(5)])

"""拆开"""
vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])

"""pi的演示"""
from math import pi
cc = [str(round(pi, i)) for i in range(0,3)]
print(cc)


"""矩阵的表示1"""
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
m = [[row[i] for row in matrix] for i in range(4)]
print(m)

"""矩阵的表示2"""
t = []
for i in range(4):
    t.append([row[i] for row in matrix])
print(t)

"""矩阵表示3"""
print(list(zip(*matrix)))


"""del"""
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
#del a[2:4]
#del a[:]
print(a)