"""python的if就是这样的结构"""
def A(x):
    if x>0:
        print('正数')
    elif x == 0:
        print('0')
    else:
        print('负数')
A(-9)