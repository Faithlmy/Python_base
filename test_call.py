
f = 3
print(f.__add__(4))

#对比两个类
class person():
    def __init__(self):
        pass
    def __call__(self, friend, age):
        self.friend = friend
        self.age = age
        #print('name is : %s, %s' %(self.name, self.age))
        print('friend is : %s, %s' %(friend, age))
p = person()#这句必须的写不写将会报错，参数不用填
p('n','23')
print('*'*200)


class person():
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __call__(self, friend):
        print('name is : %s, %s' %(self.name, self.age))
        print('friend is : %s' %friend)

p = person('me','5', 'm')#这句的写，不写将会报错，参数也必须的填
p('n')



class Fib(object):
    def __init__(self):
        pass

    def __call__(self, num):
        a, b = 0, 1;
        self.l = []

        for i in range(num):
            self.l.append(a)
            a, b = b, a + b
        return self.l

    def __str__(self):
        return str(self.l)

    __rept__ = __str__


f = Fib()
print(f(10))