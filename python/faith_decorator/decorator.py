a_string = "g_variable"


def fun1():
    """
    当在函数体中遇到变量时，Python 会首先在该函数的命名空间中寻找变量名。
    :return:
    """
    print(locals())


def fun2():
    """
    Python 的作用域规则是， 变量的创建总是会创建一个新的局部变量但是变量的
    访问（包括修改）在局部作用域查找然后是整个外层作用域来寻找匹配。

    此函数中的a_string, 先从fun2()中找，没有找到，然后在变量的外面找到了a_string
    :return:
    """
    print(a_string)


def fun3():
    """
    创建了一个和全局变量相同名字的局部变量，并且“覆盖”了全局变量。通过在函数
    fun3() 中打印局部命名空间可以印证这一点，并且发现局部命名空间有了一项数据,
    但是此时的 a_string 的值没有改变
    :return:
    """
    a_string = "faith"
    print(locals())


def fun4():
    """
    函数 fun() 的命名空间在每次函数被调用时重新创建，在函数结束时销毁。
    故, 下面的fun4()函数中并没有 x
    :return:
    """
    x = 1


def fun5(x):
    """
    形参名在函数里为局部变量
    :param x:
    :return:
    """
    print(locals())


def fun6(x, y=1):
    return x - y


def outer1():
    """
    x 先从inner()局部搜索，没有结果后，到 outer()搜索
    :return:
    """
    x = 1

    def inner1():
        print(x)
    # print(x)
    inner1()


def outer2():
    x = 1

    def inner2():
        x = 2
        print(x)

    inner2()


def fun7():
    """

    :return:
    """
    x = 3
    return fun7()


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def fun8(func, x, y):
    return func(x, y)


def outer3():
    def inner3():
        print("inner")
    return inner3()  # 没有return, inner3()将结束他的生命周期，即 不会有结果返回


def outer4():
    """
    Python 支持一种名为函数闭包的特性，意味着 在非全局作用域定义的 inner
    函数在定义时记得外层命名空间是怎样的。inner 函数包含了外层作用域变量，
    通过查看它的 func_closure 属性可以看出这种函数闭包特性。

    每次调用函数 outer 时，函数 inner 都会被重新定义
    :return:
    """
    x = 1

    def inner4():
        print(x)
    return inner4()


def outer5(x):
    """
    函数记住其外层作用域的事实——可以用来构建本质上有一个硬编码参数的自定义函数。
    虽然没有直接给 inner 函数传参 1 或 2，但构建了能“记住”该打印什么数的 inner 函数自定义版本。
    :param x:
    :return:
    """
    def inner5():
        print(x)
    return inner5()


# 装饰器
def outer6(fun):
    def inner6():
        print("inner")
        res = fun()
        return res + 1
    # print("inner6()", inner6())
    # print("inner6", inner6)
    return inner6


def foo():
    return 1

# ==========装饰器=================

# 针对特定函数
class Site(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "res: " + str(self.__dict__)


def my_wrapper(fun):
    """
    my_sum 和 my_sub 函数的装饰器， 限制的是 Site()
    :param fun:
    :return:
    """
    def check(a, b):  # 对函数进行限制/修饰
        if a.x < 0 or a.y < 0:
            a = Site(a.x if a.x > 0 else 0, a.y if a.y > 0 else 0)

        if b.x < 0 or b.y < 0:
            b = Site(b.x if b.x > 0 else 0, b.y if b.y > 0 else 0)

        res = fun(a, b)
        if res.x < 0 or res.y < 0:
            res = Site(res.x if res.x > 0 else 0, res.y if res.y > 0 else 0)
        return res  # 首先返回的是传进来的参数
    return check  # 再返回 inner 函数


@my_wrapper
def my_sum(a, b):
    return Site(a.x + b.x, a.y + b.y)


@my_wrapper
def my_sub(a, b):
    return Site(a.x - b.x, a.y - b.y)


# 针对通用函数
def new_sum(a, b):
    return a + b


def new_dict(**kwargs):
    return kwargs


def log_er(fun):
    def inner(*args, **kwargs):
        print('args = %s, kwargs = %s' % (args, kwargs))
        return fun(*args, **kwargs)
    return inner


@log_er
def faith_sum(x, y):
    return x + y


if __name__ == "__main__":
    # fun1()
    # print(a_string)
    # print(fun1())
    # print(globals())

    # fun2()
    # fun2()

    # fun3()
    # fun3()

    # fun4()
    # fun4()
    # print(x)  # NameError: name 'x' is not defined

    # fun5()
    # fun5(1)  # {'x': 1}

    # fun6()
    # res1 = fun6(3)
    # print(res1)
    # res2 = fun6(8, 2)
    # print(res2)
    # outer1()
    # outer2()

    # fun7()
    # print(issubclass(int, object))
    # print(fun7.__class__)
    # print(issubclass(fun7.__class__, object))

    # fun8()
    # res1 = fun8(add, 2, 3)
    # print(res1)

    # outer3()

    # f = outer4()
    # print(f.func_closure)

    # print(outer5(2))

    # decorator = outer6(foo)
    # print(decorator())

    # res1 = Site(1, 2)
    # res2 = Site(3, 2)
    # res3 = Site(-1, -1)
    # # res = my_sum(res1, res2)
    # # my_sum = wrapper(my_sum)  # 自己将调用装饰器， 用@就可以不用写这两句
    # # my_sub = wrapper(my_sub)
    #
    # res_1 = my_sum(res1, res3)  # 试着将上面的 @ 符号去掉看结果
    # res_2 = my_sub(res1, res2)
    #
    # print(res_1)
    # print(res_2)

    # my_list = [2, 4]
    # res = new_sum(*my_list)  # *my_list 表示取出list里面的所有位置参数
    # print(res)

    # print(new_dict(x=1, y=2))
    # new_d = {'b': 5, 'u': 8}
    # print(new_dict(**new_d))

    my_list1 = [3, 6]
    my_list2 = [3, 7]
    # my_dict = {'p': 3, 'm': 8}
    my_dict = {}
    print(faith_sum(*my_list1, **my_dict))
