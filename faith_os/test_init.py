


class X:
    pass
#print(X.__class__)
#print(X.__name__)

class Re:
    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    r = Re()
    r.length, r.width = 2, 4
    print(r.area())

from p1.m12 import fun_m12
print(fun_m12())