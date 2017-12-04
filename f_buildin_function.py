

"""
abs()   all()   any()   ascii()
bin()   bool()  bytearray()  bytes()
callable()  chr()   classmethod()   compile()   compliex()
"""
def faith_a():

    # abs
    print(abs(0.9), '\n',
          abs(-0.7), '\n',
          )

    # all ( All of object is not 0, '', false, None , the result is ture )
    print('""is: ', all(''), '\n',
          '" "is: ', all(' '), '\n',
          '0 is: ', all('0'), '\n',
          '[]is: ', all([]), '\n',
          '()is: ', all(()), '\n',
          ' """""" is:  ', all(""""""), '\n',

          '[0] is: ', all([0]), '\n',
          '(0) is: ', all(('0')), '\n',
          'one (' ') is: ', all(('')), '\n',
          'more () is: ', all(('', '')), '\n',

          '[1,3,2]is: ', all([1, 3, 2]), '\n',
          '[1,3,0]is: ', all([1, 3, 0]), '\n',
          '[1,3,""]is: ', all([1, 3, '']), '\n',
          '[1,3," "]is: ', all([1, 3, ' ']), '\n',

          '["a", "b", "c"] is: ', all(['a', 'b', 'c']), '\n',
          '["a", "b", ""] is: ', all(['a', 'b', '']), '\n',
          '["a", "b", " "] is: ', all(['a', 'b', ' ']), '\n',

          '(1,3,2)is: ', all((1, 3, 2)), '\n',
          '(1,3,0)is: ', all((1, 3, 0)), '\n',
          '(0) is: ', all((0,)), '\n',
          '(1,3,"")is: ', all((1, 3, '')), '\n',
          '(1,3," ")is: ', all((1, 3, ' ')), '\n',
          '(1,3, None)is: ', all((1, 3, None)), '\n',

          )

    # any
    print(
        'all[1, 3, 0]is: ', all([1, 3, 0]), '\n',
        'any[1, 3, 0]is: ', any([1, 3, 0]), '\n',

        'all[1, 3, ""]is: ', all([1, 3, '']), '\n',
        'any[1, 3, ""]is: ', any([1, 3, '']), '\n',

        'all[1, 3, ""]is: ', all([1, 3, ' ']), '\n',
        'any[1, 3, ""]is: ', any([1, 3, ' ']), '\n',

        'all(1, 3, "")is: ', all((1, 3, '')), '\n',
        'any(1, 3, "")is: ', any((1, 3, '')), '\n',
        'any(1, 3, "")is: ', any(('', '', '')), '\n',
        'any(1, 3, "")is: ', all(('', '', '')), '\n',
    )

def faith_b():

    # bin
    print(
        'bin(2)is: ', bin(2), '\n',

        'bool(0)is: ', bool(0), '\n',
        'bool(1)is: ', bool(1), '\n',
        'bool(134)is: ', bool(134), '\n',
        'bool("ad")is: ', bool('ad'), '\n',

        'bool(bool([]))is: ', bool([]), '\n',
        'bool(bool(()))is: ', bool(()), '\n',
        'bool(bool(""))is: ', bool(''), '\n',

        'bool(bool([1]))is: ', bool([1]), '\n',
        'bool(bool(("a")))is: ', bool(('a')), '\n',
        'bool(bool("b"))is: ', bool('b'), '\n',
    )

    # bytearray()
    print(
        'bytearray()is: ', bytearray(), '\n',
        # 'bytearray("a")is: ', bytearray('a'), '\n',
        'bytearray(2)is: ', bytearray(2), '\n',
        'bytearray()is: ', bytearray([1, 3, 4]), '\n',
        'bytearray(utf-8)is: ', bytearray('run', 'utf-8'), '\n',
        'bytearray("run",GBK)is: ', bytearray('run', 'gbk'), '\n',
    )

    # bytes()
    print(
        'bytes("run", "utf-8")is :', bytes('run', 'utf-8'), '\n',
        'bytes("和", "utf-8")is :', bytes('和', 'utf-8'), '\n',
        'bytes("run", "utf-8")is :', bytes('run'.encode('utf-8')), '\n',
        'bytes("哈", "utf-8")is :', bytes('哈'.encode('utf-8')), '\n',
        'bytes("哈", "GBK")is :', bytes('哈'.encode('GBK')), '\n',
        'bytes(2)is :', bytes(2), '\n',
        'bytes(12)is :', bytes(12), '\n',
    )


def faith_c():
    """
    Four funtions such as:
    char():
    classmethod():
    complie():
    complex():

    :return:
    """

    # chr()
    for i in range(97, 100):
        print(chr(i))

    # complex()
    print(
        'complex(1, 9)', complex(1, 9), '\n',
        'complex(1, 0)', complex(1, 0), '\n',
        'complex(1)', complex(1), '\n',
        'complex(0, 1)', complex(0, 1), '\n',
    )


class A:
    def __init__(self, name):
        self.name = name
    def H(self):
        print(self.name)

import os
def faith_d():
    """
    delattr()
    dict()
    dir()
    divmod()

    :return:
    """
    a = A
    # delattr(a, a.name)
    print(
        a.H
    )

    # dir()
    print(
        dir(os)
    )

    # dict() made dict()

    # divmod()
    print(
        'divmod(2, 4)is: ', divmod(2, 4), '\n',
        'type(divmod(2, 4))is: ', type(divmod(2, 4)), '\n',
    )
    pass

def faith_e():
    """
    enumerate()
    eval()
    exec

    :return:
    """
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    print(
        list(enumerate(seasons))
    )

    # exec()
    i = 2
    j = 5
    exec("print(i + j)")
    exec('print("faith")')


def is_odd(x):
    return x % 2 == 0
def faith_f():
    """

    filter()
    float()
    format()
    frozenset()

    :return:
    """
    # filter()
    f = filter(is_odd, [2, 5, 7, 4])
    print(
        tuple(f)
    )

    # float()
    print(
        'float(2)', float(2), '\n',
        'float()', float(), '\n',
        'float()', float(-3.999999999999999), '\n',
        'float()', float(-3.9999999999999999), '\n',
        'float(int(2.0))', float('nan'), '\n',
    )
    # format
    m = ['faith', 23]
    fm = '{0:.50f}'.format(188*456678)
    print(
        # fm,
        '1my name is {}, age is {}'.format('faith', 23), '\n',
        '2my name is {1}, age is {0}'.format('faith', 23), '\n',

        '3my name is {b}, age is {n}'.format(b='faith', n=23), '\n',
        '4my name is {n}, age is {b}'.format(b='faith', n=23), '\n',

        '5my name is {}, age is {}'.format(*m), '\n',
        '6my name is {1}, age is {0}'.format(*m), '\n',

        '{0:*>10}'.format(5), '\n',
        '{0:*<5}'.format(10), '\n',
        '{0:*^10}'.format(10), '\n',

        '{0:.5f}'.format(1/3), '\n',
        '{0:.50f}'.format(1/3), '\n',
        # "{0:,}".format(fm), '\n',
        '{0:b}'.format(3), '\n',
        '{0:o}'.format(10), '\n',
        '{0:x}'.format(10), '\n',
        '{0:,}'.format(12345678901), '\n',
        '{0:,}'.format(0.12345678901), '\n',
    )

   # frozenset()
    print(
        frozenset(range(10)), '\n',
        set(range(10)), '\n',
    )



class f_g():
    name = 'faith'
    def run(self):
        return 'hello'


def faith_g():
    """

    getattr() hasattr() setattr()
    globals()
    :return:
    """
    a = f_g()
    print(
        hasattr(a, 'name'), '\n', # get properties of object, print turn or false
        hasattr(a, 'run'), '\n',# get method of object, print turn or false
        getattr(a, 'name'), '\n',# get properties of object, print value of object
        getattr(a, 'run'), '\n',# get method of object, print memory address of object method
    )
    print(hasattr(a, 'age'), '\n', )
    setattr(a, 'age', 23)# Attribute assignment for objects ,if the object is not exist, it will built a object
    print(getattr(a, 'age'), '\n', )
    print(hasattr(a, 'age'), '\n', )


def faith_h():
    """
    hash()
    hasattr()
    help()
    hex()
    :return:
    """
    print(
        hash(2), '\n',
        hash('2'), '\n',
        hash(str(['abc'])), '\n',
        hash(str(sorted({2: 'q'}))), '\n',
        hex(5), '\n',
    )

    # print(
    #     help(os.path)
    # )
    pass


class fa():
    pass
class fb(fa):
    pass
class fc():
    pass
def faith_i():
    """

    id()
    int()
    input()
    isinstance()
    issubclass()
    iter()
    len()
    list()
    locals()

    :return:
    """
    # id() --> get the memory address of object
    a = 1
    print(
        id(a)
    )
    # int()
    print(
        int(2.67)
    )
    #input()

    #isinstance()
    a = fa()
    b = 3
    c = 'abc'
    f = ()
    print(
        isinstance(a, fa), '\n',
        isinstance(b, int), '\n',
        isinstance(b, float), '\n',
        isinstance(c, str), '\n',
        isinstance(f, tuple), '\n',
    )
    # issubclass() 判断 fb 是 fa 的子类
    print(
        issubclass(fa, fb), '\n',
        issubclass(fb, fa), '\n',
        isinstance(fa, fc), '\n',
    )
    #iter()
    m = [1, 3, 5, 6]
    for i in iter(m):
        print(i)

    # len()
    # len()
    # locals()


def s(x):
    return x*x
def add(a, b):
    return (a + b)
def faith_m():
    """

    map()
    max()
    memoryview()
    min()
    module()
    :return:
    """
    p = [1, 3, 0, 4]
    print(
        list(map(s, [2, 3, 6])), '\n',
        list(map(lambda x: x*x, ([2, 5, 9]))), '\n',
        list(map(add, 'faith', 'meng')), '\n',
        max(p)
    )

    v= memoryview(b'abcefg')
    print(
        v[0], '\n',
        v[1], '\n',
        bytes(v[1:3]), '\n',
    )

def faith_n():
    """
    next()
    :return:
    """
    it = iter([1, 3, 6,9])
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            break

def faith_o():
    """
    object()
    oct()
    open()
    ord()
    :return:
    """
    print(
        oct(10), '\n',
        ord('a')
    )
import math
def faith_p():
    """
    pow()
    print()
    property()
    :return:
    """
    print(
        pow(2,3), '\n',
        pow(2,3,5), '\n',# 2*2*2%5
    )

def faith_r():
    """
    range()
    repr()
    reversed()
    round()
    :return:
    """
    #range()

    # repr() convict object for interpreter
    s = 'vic'
    aList = [123, 'xyz', 'zara', 'abc', 'xyz'];
    aList.reverse()
    print(
        repr(s), '\n',
        aList, '\n',
        round(1.45622, 2), '\n',
        round(1.45622, 4), '\n',
        round(1.255, 2), '\n',
        round(1.257, 2), '\n',
    )
    pass
def faith_s():
    """
    set()
    setattr() #please view getattr()
    slice()
    sorted()
    staticmethod() #返回函数的静态方法
    str()
    sum()
    super() #类的继承
    :return:
    """

    # set()
    x = set('bootg')
    y = set('google')
    z = ['google', 'boot', 'boot', 'app', 'goo']
    m = ('google', 'boot', 'boot', 'app', 'goo')
    print(
        x, '\n',
        z, '\n',
        set(m), '\n',
        x&y, '\n',
        x|y, '\n',
        x-y, '\n',
        y-x, '\n',
    )
    myslice = slice(3)
    a = range(8)
    l = [13, 9, 4, 5, 11]
    print(
        myslice, '\n',
        list(a[myslice]), '\n',
        l, '\n',
        sorted(l), '\n',
    )
    pass

def faith_t():
    """
    tuple()
    type()
    :return:
    """
    pass

def faith_v():
    print(
        vars(os), '\n',
    )
    pass
def faith_z():
    a = [1, 2, 3]
    b = [11, 22, 33]
    c = [11, 22, 55, 44]
    d = zip(a, b)
    print(
        list(d), '\n',
        list(zip(a, c)), '\n',
        # list(zip(*d)), '\n',
    )
    pass

if __name__=='__main__':
    # faith_a()
    # faith_b()
    # faith_c()
    # faith_d()
    # faith_e()
    # faith_f()
    # faith_g()
    # faith_h()
    # faith_i()
    # faith_m()
    # faith_n()
    # faith_o()
    # faith_p()
    # faith_r()
    # faith_s()
    # faith_v()
    faith_z()
    pass