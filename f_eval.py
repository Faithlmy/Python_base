"""
eval()
1. contral using variable of globals or locals
2. Globals variable can be changed, but local varable is not
"""

# test eval() and locals()
x = 1
y = 2
num1 = eval("x+y", globals())
num11 = eval("x+y", locals())
print(
    'num1: ', num1,
    'num11: ', num11,
    )
def g():
    x = 3
    y = 4
    num3 = eval("x+y")
    print('num3: ', num3)
    num2 = eval("x+y", globals())
    print('num2:', num2)
    num22 = eval("x+y",locals())
    print('num22: ', num22)

    print('locals()["x"] + globals()["y"]: ', locals()['x'] + globals()['y'])
    print('x + globals()["y"]: ', x + globals()['y'])
    print('x + globals()["x"]: ', x + globals()['x'])

    globals()['x'] = 10
    print(
        'x + x: ', x + x, '\n',
        'x + globals()["x"]: ', x + globals()['x'], '\n',
    )

g()

print(locals()["x"])
print(locals()["y"])
print(globals()["x"])
print(globals()["y"])