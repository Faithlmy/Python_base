class faith_ascii():
    def __init__(self, n):
        self.n = n
        print('__init__', self.n)
    def __del__(self):
        print('__del__')
    def num(self):
        l = []
        for i in range(0, 127):
            l.append(chr(i))
            # print(chr(i))
        return l

class faith_add():
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return self.v + other
    def __sub__(self, other):
        return self.v - other

class faith_next():
    def __init__(self, date=1):
        self.date = date
    def __iter__(self):
        return self

    def __next__(self):
        print('__next__call')
        if self.date < 5:
            self.date += 1
        else:
            raise StopIteration
        return self.date

class faith_str():
    def __str__(self):
        return '__str__called'
    def __repr__(self):
        return '__repr__called'


class faith_index():
    date = [1, 3, 5, 2, 9]
    def __getitem__(self, item):
        return self.date[item]
    def __setitem__(self, key, value):
        self.date[key] = value
        return self.date

class faith_getset():
    def __init__(self, ax, bx):
        self.ax = ax
        self.bx = bx

    def f(self):
        print(self.__dict__)

    def __getattr__(self, item):
        print('__getattr__')
    def __setattr__(self, item, value):
        print('__setattr__')
        self.__dict__[item] = value

if __name__ == '__main__':
    a = faith_ascii('hal')
    b = a.num()
    # a.num()
    print(a, '\n',)

    add = faith_add(5)
    print(
        add + 5, '\n',
        add - 3, '\n',
    )

    for i in faith_next(9):
        print(i)


    print('*' * 50)
    n = faith_next(3)
    i = iter(n)
    while True:
        try:
            print(next(i))
        except Exception as e:
            break


    print('*' * 50)
    s = faith_str()
    print(str(s), '\n',
          repr(s), '\n',
          )

    print('*' * 50)
    i = faith_index()
    i[4] = 100
    print(
        i[0], '\n',
        i[0:3], '\n',
        i[0:5], '\n',
    )

    print('*' * 50)
    fa = faith_getset(1, 2)
    fa.f()
    print(fa.ax)
    fa.bx = 90
    fa.f()