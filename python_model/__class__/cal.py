
class A:
    """#cal.py"""
    def __init__(self, url):
        self.url = url

    def out(self):
        return self.url
a = A('www.baidu.com')
# print(a)
# print(a.url)
print(a.out())

b = a.__class__('www,bbc.com')
print(b.out())

print(A)
print(a.__class__)
print(b.__class__)
print(A.__doc__)
print(a.__doc__)
