'''
使用方法：
    直接运行run_foo.py 正常情况下回报错 ：
    File "run_foo.py", line 8, in <module>
    print(waz)
    NameError: name 'waz' is not defined
    此时将__all__ = ['bar', 'baz']改为__all__ = ['bar', 'baz', 'waz']
    将会正确
'''
#foo.py
__all__ = ['bar', 'baz', 'waz']

waz = 5
bar = 10
def baz():
    return 'baz'