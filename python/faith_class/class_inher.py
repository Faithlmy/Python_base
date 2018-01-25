
class A:
    name = 'A'
    __num = 1
    _a = 9

    def __init__(self):
        self.__num = None
        self._a = None

    def show(self):
        print(self.name)
        print(self.__num)

    def set_num(self, num):
        self.__num = num


class B:
    name_b = 'B'
    __numb = 2

    def __init__(self):
        self.__num = None

    def show(self):
        print(self.name_b)
        print(self.__numb)

    def set_num(self, numb):
        self.__num = numb


class C(A, B):

    def show_all(self):
        print(self.name)
        print(self.name_b)
        print(self)


def t_len():
    a = 'meng'
    print("len(a)", len(a))
    print('a.__len__()', a.__len__())


class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)


class test_p():
    """
    _ 该方法或属性不应该去调用，它并不属于API。
    __ 用来避免子类覆盖其内容
    __xx__ 经常是操作符或本地函数调用的magic methods
    """

    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.h = None
        self._h = None

    def _sum(self):
        s = self.m + self.n
        return s

    def show(self):  # 变量中只有h可以被类外部引用, 函数也一样
        self.h = 1000
        self._h = 100
        self._sum()
        self.__sum()

        a_sum = self._sum()
        asum = self.sum(self.h)
        a__sum = self.__sum()
        print(asum)
        return a_sum, asum, a__sum

    def sum(self, k):
        ap = 90
        s = self.n * self.m + k
        return {s: ap}

    def __sum(self):
        s = self.n / self.m
        return s


if __name__ == '__main__':

    # a = test_p(2, 3)
    # a.h = 6
    # res = a.show()
    # print(type(res))
    # print(res)
    res = C.show
    res


