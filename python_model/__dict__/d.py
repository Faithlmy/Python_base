#d.py
class p:
    """#discrabe __dict"""
    country = 'China'
    def __init__(self, name, con):
        self.name = name
        self.con = con

    def f(self, *args, **kwargs):
        print('f')

    def fp(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        return self

print(p.__dict__)
print(p.__doc__)

ob1 = p('hebei',100)
ob2 = p.fp('shanxi', 90)
print('*'*50)
print(ob1.__dict__)
print(ob2)