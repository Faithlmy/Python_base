from faith_all.kk import *
from faith_all.nn import fun1_n



if __name__ == '__main__':
    a = A('a', 23)
    b = B('b', 24)
    print(
          a, '\n',
          a.name, '\n',
          a.age, '\n',
          b, '\n',
          b.name, '\n',
          b.id, '\n',
          )
    fun2()
    fun1()
    fun1_n()
