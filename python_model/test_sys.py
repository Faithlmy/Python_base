import sys

#获取正在执行的参数列表
#注意：执行时候输入 ： python test_sys.py a1 a2 a3
print(sys.argv[0])
for i in sys.argv:
    print(i)
print(len(sys.argv))

print(sys.platform)

#查找第三方扩展模块
#print(sys.path)

#返回内键模块的名字
#print(sys.builtin_module_names)

print(sys.version)
print('8'*50)
