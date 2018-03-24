# comparison of __init__ __str__ and __repr__


class TestInit(object):
    def __init__(self):
        self.value = 'faith'


class TestRepr(TestInit):  # rewrite TestInit
    """
    After rewrite TestInit, the result will show all formats that rewrite TestInit.
    """
    def __repr__(self):
        return 'TestRepr (%s)' % self.value


class TestStr(TestInit):
    def __str__(self):
        return 'TestReprTwo (%s)' % self.value


class Test(object):
    """
    1. __repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员
    2. 用于交互模式下提示回应以及repr函数，如果没有使用__str__，会使用print和str
    """
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'test_repr (%s)' % self.value

    def __str__(self):
        return 'test_str (%s)' % self.value


if __name__ == '__main__':
    # c = TestInit()
    # print(c)
    # print(TestRepr())
    # c = TestRepr()
    # print(c)
    print(TestStr())
    # d = TestStr()
    # print(d)
    # print(d)
    # f = Test('meng')
    # print(f)
