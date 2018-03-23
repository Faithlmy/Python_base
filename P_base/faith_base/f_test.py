class A:
    pass

class B:
    def __call__(self):
        print('h')

def ab():
    print('h')
    pass
a=A()
b=B()
n = ab()
print(callable(A))
print(callable(a))
print(callable(B))
print(callable(b))
print(callable(ab()))
print(callable(n))