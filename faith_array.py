import numpy as np
a = np.arange(15).reshape(5,3)
print(a)
print(a.shape)
print(a.ndim)
print(a.itemsize)
print(a.size)
print(type(a))

colours = ["red","green","blue"]
for i in range(0, len(colours)):
    print (i, colours[i])


c1 = [1, 2, 3]
c2 = [4, 5, 6]
c3 = {3, 5, 7}
c4 = ['1', '2', '3']
c5 = [7, 1, 6, 9]
c6 = [1, 2, 5]
c = np.array([c1, c2, c6])
print('*' * 10)
print(c)
print(type(c))
# for x in c:#遍历整个数组
#     print(x)

# for y in c.flat:#遍历每一个元素，最好元素都相同
#     print(y)

print(c[1][:])

l = []
for x in c[0][:]:
    for y in c[2][:]:
        if(x == y):
            l.append(c[1][x-1])

print(l)
# print(c.T)


print('*' * 50)
fp = [2, 3, 2, 5, 1, 3, 4, 5]

l2 = list(set(fp))
print(l2)